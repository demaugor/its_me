import sqlite3  
import logging  
from datetime import datetime  
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler  
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup  

# Настройка логирования  
logging.basicConfig(  
    level=logging.INFO,  
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  
    handlers=[logging.FileHandler("calc_db.log"), logging.StreamHandler()]  
)  
logger = logging.getLogger(__name__)  

def init_db():  
    try:  
        conn = sqlite3.connect("bot.db")  
        cursor = conn.cursor()  
        cursor.execute('''  
            CREATE TABLE IF NOT EXISTS history (  
                id INTEGER PRIMARY KEY AUTOINCREMENT,  
                user_id INTEGER,  
                timestamp TEXT,  
                expression TEXT,  
                result TEXT  
            )  
        ''')  
        conn.commit()  
        logger.info("Таблица history создана или уже существует")  
    except sqlite3.Error as e:  
        logger.error(f"Ошибка создания базы данных: {e}")  
    finally:  
        conn.close()  

def save_history(user_id, expression, result):  
    try:  
        conn = sqlite3.connect("bot.db")  
        cursor = conn.cursor()  
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
        cursor.execute(  
            "INSERT INTO history (user_id, timestamp, expression, result) VALUES (?, ?, ?, ?)",  
            (user_id, timestamp, expression, result)  
        )  
        conn.commit()  
        logger.debug(f"Запись добавлена в историю для user_id {user_id}: {expression} = {result}")  
    except sqlite3.Error as e:  
        logger.error(f"Ошибка сохранения истории: {e}")  
    finally:  
        conn.close()  

def get_history(user_id):  
    try:  
        conn = sqlite3.connect("bot.db")  
        cursor = conn.cursor()  
        cursor.execute(  
            "SELECT timestamp, expression, result FROM history WHERE user_id = ? ORDER BY id DESC LIMIT 5",  
            (user_id,)  
        )  
        rows = cursor.fetchall()  
        return rows  
    except sqlite3.Error as e:  
        logger.error(f"Ошибка чтения истории: {e}")  
        return []  
    finally:  
        conn.close()  

def start(update, context):  
    user_id = update.message.from_user.id  
    user_name = update.message.from_user.first_name  
    keyboard = [[InlineKeyboardButton("Калькулятор", callback_data="calc_menu")]]  
    reply_markup = InlineKeyboardMarkup(keyboard)  
    update.message.reply_text(f"Привет, {user_name}! Я бот-калькулятор с базой данных.", reply_markup=reply_markup)  
    logger.info(f"Пользователь {user_id} ({user_name}) запустил /start")  

def history(update, context):  
    user_id = update.message.from_user.id  
    rows = get_history(user_id)  
    if rows:  
        response = "Ваша история (последние 5):\n"  
        for timestamp, expr, res in rows:  
            response += f"{timestamp}: {expr} = {res}\n"  
        update.message.reply_text(response)  
    else:  
        update.message.reply_text("История пуста или произошла ошибка.")  
    logger.info(f"Пользователь {user_id} запросил историю")  

def calculate(num1, num2, operation):  
    try:  
        if operation == "+": return num1 + num2  
        elif operation == "-": return num1 - num2  
        elif operation == "*": return num1 * num2  
        elif operation == "/":  
            if num2 == 0: raise ZeroDivisionError("Деление на ноль!")  
            return num1 / num2  
        else: raise ValueError("Неверная операция!")  
    except (ZeroDivisionError, ValueError) as e:  
        logger.error(f"Ошибка вычисления: {e}")  
        return str(e)  

def handle_num1(update, context):  
    if context.user_data.get("step") != "num1": return  
    user_id = update.message.from_user.id  
    text = update.message.text  
    try:  
        context.user_data["num1"] = float(text)  
        update.message.reply_text("Введи второе число.")  
        context.user_data["step"] = "num2"  
        logger.debug(f"Пользователь {user_id} ввел первое число: {text}")  
    except ValueError:  
        update.message.reply_text("Пожалуйста, введи число!")  
        logger.warning(f"Пользователь {user_id} ввел неверное первое число: {text}")  

def handle_num2(update, context):  
    if context.user_data.get("step") != "num2": return  
    user_id = update.message.from_user.id  
    text = update.message.text  
    try:  
        context.user_data["num2"] = float(text)  
        keyboard = [["+", "-"], ["*", "/"]]  
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)  
        update.message.reply_text("Выбери операцию:", reply_markup=reply_markup)  
        context.user_data["step"] = "operation"  
        logger.debug(f"Пользователь {user_id} ввел второе число: {text}")  
    except ValueError:  
        update.message.reply_text("Пожалуйста, введи число!")  
        logger.warning(f"Пользователь {user_id} ввел неверное второе число: {text}")  

def handle_operation(update, context):  
    if context.user_data.get("step") != "operation": return  
    user_id = update.message.from_user.id  
    num1 = context.user_data["num1"]  
    num2 = context.user_data["num2"]  
    operation = update.message.text.strip()  
    result = calculate(num1, num2, operation)  
    expression = f"{num1} {operation} {num2}"  
    if isinstance(result, str):  
        update.message.reply_text(f"Ошибка: {result}")  
    else:  
        update.message.reply_text(f"Результат: {expression} = {result}")  
        save_history(user_id, expression, str(result))  
        logger.info(f"Пользователь {user_id} выполнил вычисление: {expression} = {result}")  
    context.user_data["step"] = None  

def button(update, context):  
    query = update.callback_query  
    user_id = query.from_user.id  
    query.answer()  
    if query.data == "calc_menu":  
        query.edit_message_text("Введи первое число.")  
        context.user_data["step"] = "num1"  
        logger.info(f"Пользователь {user_id} начал вычисления")  

def unknown(update, context):  
    user_id = update.message.from_user.id  
    text = update.message.text  
    update.message.reply_text("Напиши /start, чтобы начать!")  
    logger.warning(f"Пользователь {user_id} отправил неизвестное сообщение: {text}")  

def main():  
    init_db()  # Инициализация базы  
    TOKEN = "123456789:AAF-abc123xyz456def789ghi"  # Замените на свой токен  
    updater = Updater(TOKEN, use_context=True)  
    dp = updater.dispatcher  

    dp.add_handler(CommandHandler("start", start))  
    dp.add_handler(CommandHandler("history", history))  
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command & Filters.regex(r'^-?\d*\.?\d+$'), handle_num1))  
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command & Filters.regex(r'^-?\d*\.?\d+$'), handle_num2))  
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command & Filters.regex(r'^[+\-*/]$'), handle_operation))  
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, unknown))  
    dp.add_handler(CallbackQueryHandler(button))  

    logger.info("Бот с SQLite запущен")  
    updater.start_polling()  
    updater.idle()  

if __name__ == "__main__":  
    main()  
