import pygame
import pygame_menu

class Hero:
    def __init__(self, race: str, profession: str, weapon: str):
        self.race = race
        self.profession = profession
        self.weapon = weapon

        race_modifiers = {
            'Человек': {'hp': 100, 'damage': 5},
            'Эльф':   {'hp': 80,  'damage': 8},
            'Орк':    {'hp': 120, 'damage': 4}
        }
        profession_modifiers = {
            'Воин':   {'hp': 20, 'damage': 2},
            'Лучник':  {'hp': 0,  'damage': 3},
            'Маг':     {'hp': -10, 'damage': 5}
        }
        weapon_modifiers = {
            'Меч':     {'damage': 2},
            'Лук':     {'damage': 3},
            'Посох':   {'damage': 4}
        }

        base = race_modifiers.get(race, {'hp': 0, 'damage': 0})
        self.hp = base['hp']
        self.damage = base['damage']

        pm = profession_modifiers.get(profession, {'hp': 0, 'damage': 0})
        self.hp += pm.get('hp', 0)
        self.damage += pm.get('damage', 0)

        wm = weapon_modifiers.get(weapon, {'damage': 0})
        self.damage += wm.get('damage', 0)

    def get_text(self):
        return (f"Герой:\n"
                f"  Раса: {self.race}\n"
                f"  Профессия: {self.profession}\n"
                f"  Оружие: {self.weapon}\n"
                f"  HP: {self.hp}\n"
                f"  Урон: {self.damage}")

def main():
    pygame.init()
    window_size = (600, 400)
    surface = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Регистрация героя")

    # Переменные выбора
    selected = {
        'race': 'Человек',
        'profession': 'Воин',
        'weapon': 'Меч'
    }

    def set_race(_, race):
        selected['race'] = race

    def set_profession(_, profession):
        selected['profession'] = profession

    def set_weapon(_, weapon):
        selected['weapon'] = weapon

    hero = None
    show_hero = False  # флаг отображения экрана героя

    # Функция “Создать героя”
    def create_hero():
        nonlocal hero, show_hero
        hero = Hero(selected['race'], selected['profession'], selected['weapon'])
        show_hero = True

    # Функция “Назад к меню”
    def back_to_menu():
        nonlocal show_hero
        show_hero = False

    # Меню выбора
    menu = pygame_menu.Menu('Создать героя', 600, 400,
                             theme=pygame_menu.themes.THEME_DARK)
    menu.add.selector('Раса :', [('Человек', 'Человек'), ('Эльф', 'Эльф'), ('Орк', 'Орк')], onchange=set_race)
    menu.add.selector('Профессия :', [('Воин', 'Воин'), ('Лучник', 'Лучник'), ('Маг', 'Маг')], onchange=set_profession)
    menu.add.selector('Оружие :', [('Меч', 'Меч'), ('Лук', 'Лук'), ('Посох', 'Посох')], onchange=set_weapon)
    menu.add.button('Создать героя', create_hero)
    menu.add.button('Выход', pygame_menu.events.EXIT)

    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    while True:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                return

        surface.fill((30, 30, 30))

        if not show_hero:
            # Показываем меню
            menu.update(events)
            menu.draw(surface)
        else:
            # Показываем характеристики героя + кнопку “Назад”
            text = hero.get_text()
            lines = text.split('\n')
            y = 50
            for line in lines:
                txt_surf = font.render(line, True, (255, 255, 255))
                surface.blit(txt_surf, (50, y))
                y += 40

            # Рисуем кнопку “Назад” вручную
            back_text = font.render("Назад", True, (200, 200, 200))
            back_rect = back_text.get_rect()
            back_rect.topleft = (50, window_size[1] - 60)
            surface.blit(back_text, back_rect)

            # Обработка клика на “Назад”
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if click[0] == 1:
                # Проверка, если курсор над текстом Назад
                if back_rect.collidepoint(mouse):
                    back_to_menu()

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
