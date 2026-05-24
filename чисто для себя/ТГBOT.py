import asyncio  
import logging  
import sqlite3  
from datetime import datetime  
from aiogram import Bot, Dispatcher, types  
from aiogram.dispatcher import FSMContext  
from aiogram.dispatcher.filters.state import State, StatesGroup  
from aiogram.contrib.fsm_storage.memory import MemoryStorage  
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup  

logging.basicConfig(  
    level=logging.INFO,  
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  
    handlers=[logging.FileHandler("pizza_bot.log"), logging.StreamHandler()]  
)  
logger = logging.getLogger(__name__)  

TOKEN = "123456789:AAF-abc123xyz456def789ghi"  

bot = Bot(token=TOKEN)  
storage = MemoryStorage()  
dp = Dispatcher(bot, storage=storage)  

class PizzaOrder(StatesGroup):  
    type = State()  
    size = State()  
    extra = State()  
    confirm = State()  

def init_db():  
    try:  
        conn = sqlite3.connect("pizza_orders.db")  
        cursor = conn.cursor()  
        cursor.execute('''  
            CREATE TABLE IF NOT EXISTS orders (  
                id INTEGER PRIMARY KEY AUTOINCREMENT,  
                user_id INTEGER,  
                pizza_type TEXT,  
                size TEXT,  
                extra TEXT,  
                timestamp TEXT  
            )  
        ''')  
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_orders_user_id ON orders(user_id)")  
        conn.commit()  
        logger.info("База данных инициализирована")  
    except sqlite3.Error as e:  
        logger.error(f"Ошибка инициализации базы: {e}")  
    finally:  
        conn.close()  

async def save_order(user_id, pizza_type, size, extra):  
    try:  
        conn = sqlite3.connect("pizza_orders.db")  
        cursor = conn.cursor()  
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
        cursor.execute(  
            "INSERT INTO orders (user_id, pizza_type, size, extra, timestamp) VALUES (?, ?, ?, ?, ?)",  
            (user_id, pizza_type, size, extra, timestamp)  
        )  
        conn.commit()  
        logger.info(f"Заказ сохранен для user_id {user_id}: {pizza_type}, {size}, {extra}")  
    except sqlite3.Error as e:  
        logger.error(f"Ошибка сохранения заказа: {e}")  
    finally:  
        conn.close()  

async def get_orders(user_id):  
    try:  
        conn = sqlite3.connect("pizza_orders.db")  
        cursor = conn.cursor()  
        cursor.execute(  
            "SELECT id, pizza_type, size, extra, timestamp FROM orders WHERE user_id = ? ORDER BY timestamp DESC LIMIT 5",  
            (user_id,)  
        )  
        return cursor.fetchall()  
    except sqlite3.Error as e:  
        logger.error(f"Ошибка получения заказов: {e}")  
        return []  
    finally:  
        conn.close()  

@dp.message_handler(commands=["start"])  
async def start_command(message: types.Message):  
    user_id = message.from_user.id  
    user_name = message.from_user.first_name  
    await message.reply(f"Привет, {user_name}! Я помогу заказать пиццу.\n/order — начать заказ\n/history — история заказов")  
    logger.info(f"Пользователь {user_id} ({user_name}) запустил /start")  

@dp.message_handler(commands=["order"])  
async def order_pizza(message: types.Message):  
    user_id = message.from_user.id  
    keyboard = InlineKeyboardMarkup()  
    keyboard.add(  
        InlineKeyboardButton("Маргарита", callback_data="type_margarita"),  
        InlineKeyboardButton("Пепперони", callback_data="type_pepperoni")  
    )  
    await message.reply("Выбери тип пиццы:", reply_markup=keyboard)  
    await PizzaOrder.type.set()  
    logger.info(f"Пользователь {user_id} начал заказ пиццы")  

@dp.callback_query_handler(lambda c: c.data.startswith("type_"), state=PizzaOrder.type)  
async def process_type(callback: types.CallbackQuery, state: FSMContext):  
    user_id = callback.from_user.id  
    pizza_type = callback.data.split("_")[1].capitalize()  
    await state.update_data(pizza_type=pizza_type)  
    keyboard = InlineKeyboardMarkup()  
    keyboard.add(  
        InlineKeyboardButton("Маленькая", callback_data="size_small"),  
        InlineKeyboardButton("Средняя", callback_data="size_medium"),  
        InlineKeyboardButton("Большая", callback_data="size_large")  
    )  
    keyboard.add(InlineKeyboardButton("Отмена", callback_data="cancel"))  
    await callback.message.edit_text(f"Ты выбрал {pizza_type}. Какой размер?", reply_markup=keyboard)  
    await PizzaOrder.size.set()  
    logger.info(f"Пользователь {user_id} выбрал тип: {pizza_type}")  
    await callback.answer()  

@dp.callback_query_handler(lambda c: c.data.startswith("size_"), state=PizzaOrder.size)  
async def process_size(callback: types.CallbackQuery, state: FSMContext):  
    user_id = callback.from_user.id  
    size = callback.data.split("_")[1].capitalize()  
    await state.update_data(size=size)  
    keyboard = InlineKeyboardMarkup()  
    keyboard.add(  
        InlineKeyboardButton("Сыр", callback_data="extra_cheese"),  
        InlineKeyboardButton("Соус", callback_data="extra_sauce"),  
        InlineKeyboardButton("Ничего", callback_data="extra_none")  
    )  
    keyboard.add(InlineKeyboardButton("Назад", callback_data="back_to_type"),  
                 InlineKeyboardButton("Отмена", callback_data="cancel"))  
    await callback.message.edit_text(f"Твой заказ: {size}. Добавить что-то?", reply_markup=keyboard)  
    await PizzaOrder.extra.set()  
    logger.info(f"Пользователь {user_id} выбрал размер: {size}")  
    await callback.answer()  

@dp.callback_query_handler(lambda c: c.data.startswith("extra_"), state=PizzaOrder.extra)  
async def process_extra(callback: types.CallbackQuery, state: FSMContext):  
    user_id = callback.from_user.id  
    extra = callback.data.split("_")[1].capitalize() if callback.data != "extra_none" else "Ничего"  
    await state.update_data(extra=extra)  
    data = await state.get_data()  
    pizza_type = data["pizza_type"]  
    size = data["size"]  
    keyboard = InlineKeyboardMarkup()  
    keyboard.add(  
        InlineKeyboardButton("Подтвердить", callback_data="confirm_yes"),  
        InlineKeyboardButton("Отмена", callback_data="cancel")  
    )  
    await callback.message.edit_text(f"Твой заказ: {pizza_type}, {size}, {extra}. Подтвердить?", reply_markup=keyboard)  
    await PizzaOrder.confirm.set()  
    logger.info(f"Пользователь {user_id} выбрал дополнение: {extra}")  
    await callback.answer()  

@dp.callback_query_handler(lambda c: c.data == "back_to_type", state=PizzaOrder.extra)  
async def back_to_type(callback: types.CallbackQuery, state: FSMContext):  
    user_id = callback.from_user.id  
    keyboard = InlineKeyboardMarkup()  
    keyboard.add(  
        InlineKeyboardButton("Маргарита", callback_data="type_margarita"),  
        InlineKeyboardButton("Пепперони", callback_data="type_pepperoni")  
    )  
    await callback.message.edit_text("Выбери тип пиццы:", reply_markup=keyboard)  
    await PizzaOrder.type.set()  
    logger.info(f"Пользователь {user_id} вернулся к выбору типа")  
    await callback.answer()  

@dp.callback_query_handler(lambda c: c.data == "confirm_yes", state=PizzaOrder.confirm)  
async def process_confirm(callback: types.CallbackQuery, state: FSMContext):  
    user_id = callback.from_user.id  
    data = await state.get_data()  
    pizza_type = data["pizza_type"]  
    size = data["size"]  
    extra = data["extra"]  
    await save_order(user_id, pizza_type, size, extra)  
    await callback.message.edit_text(f"Заказ принят: {pizza_type}, {size}, {extra}. Спасибо!")  
    await state.finish()  
    logger.info(f"Пользователь {user_id} подтвердил заказ: {pizza_type}, {size}, {extra}")  
    await callback.answer()  

@dp.callback_query_handler(lambda c: c.data == "cancel", state="*")  
async def process_cancel(callback: types.CallbackQuery, state: FSMContext):  
    user_id = callback.from_user.id  
    await callback.message.edit_text("Заказ отменен.")  
    await state.finish()  
    logger.info(f"Пользователь {user_id} отменил заказ")  
    await callback.answer()  

@dp.message_handler(commands=["history"])  
async def show_history(message: types.Message):  
    user_id = message.from_user.id  
    orders = await get_orders(user_id)  
    if not orders:  
        await message.reply("У тебя пока нет заказов.")  
    else:  
        response = "Твои последние заказы (до 5):\n"  
        for order_id, pizza_type, size, extra, timestamp in orders:  
            response += f"ID {order_id}: {pizza_type}, {size}, {extra} ({timestamp})\n"  
        await message.reply(response)  
    logger.info(f"Пользователь {user_id} запросил историю заказов")  

async def main():  
    init_db()  
    logger.info("Бот запущен!")  
    await dp.start_polling()  

if __name__ == "__main__":  
    asyncio.run(main())  