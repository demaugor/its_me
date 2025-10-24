import pygame
import pygame_menu

pygame.init()

screen = pygame.display.set_mode("600x600")
pygame.display.set_caption("Крестики-нолики")
screen.fill("#000000")

if event.key == pygame.K_n:
    mainmenu.enable()

field = [
    ["","",""],
    ["","",""],
    ["","",""]
]
mainmenu.add.selector("сторона:", [("нолики", True), ("крестики", False)], onchange = set_side)