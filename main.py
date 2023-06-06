import pygame
import random

# Dimensiones de la ventana del juego
WIDTH = 800
HEIGHT = 600

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
LIGHT_BLUE = (135, 206, 250)

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(" Juego de Adivinanza de Palabras JAP")

# Función para mostrar el texto en la pantalla
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# Clase para representar las opciones del menú
class Option:
    def __init__(self, text, x, y):
        self.text = text
        self.x = x
        self.y = y
        self.font = pygame.font.Font(None, 36)
        self.color = WHITE

    def draw(self):
        draw_text(self.text, self.font, self.color, self.x, self.y)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.is_mouse_over():
                self.color = LIGHT_BLUE
            else:
                self.color = WHITE
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_mouse_over():
                return True
        return False

    def is_mouse_over(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.x - 75 <= mouse_pos[0] <= self.x + 75 and self.y - 20 <= mouse_pos[1] <= self.y + 20:
            return True
        return False

# Clase para representar las categorías
class Category:
    def __init__(self, name, words):
        self.name = name
        self.words = words

    def select_word(self):
        return random.choice(self.words)

# Lista de categorías
categories = [
    Category("Cultura General", ["palabra1", "palabra2", "palabra3", ..., "palabra50"]),
    Category("Naturaleza", ["palabra1", "palabra2", "palabra3", ..., "palabra50"]),
    Category("Cambio Climático", ["palabra1", "palabra2", "palabra3", ..., "palabra50"]),
    Category("Historia", ["palabra1", "palabra2", "palabra3", ..., "palabra50"]),
    Category("Astronomía", ["palabra1", "palabra2", "palabra3", ..., "palabra50"])
]

# Opciones del menú
options = [
    Option("Nuevo juego", WIDTH // 2, HEIGHT // 2 - 40),
    Option("Configurar jugador", WIDTH // 2, HEIGHT // 2),
    Option("Salir", WIDTH // 2, HEIGHT // 2 + 40)
]

# Función para mostrar la pantalla principal
def show_main_screen():
    running = True

    while running:
        screen.fill(BLACK)

        # Mostrar el título
        title_font = pygame.font.Font(None, 100)
        draw_text("JAP", title_font, WHITE, WIDTH // 2, HEIGHT // 4)
        title_font = pygame.font.Font(None, 40)
        draw_text("Juego de Adivinaza de Palabras", title_font, WHITE, WIDTH // 2, HEIGHT // 3)
        # Mostrar las opciones del menú
        for option in options:
            option.draw()

        pygame.display.flip()

        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for option in options:
                    if option.handle_event(event):
                        if option.text == "Nuevo juego":
                            show_category_selection()
                        elif option.text == "Configurar jugador":
                            show_player_configuration()
                        elif option.text == "Salir":
                            running = False

    pygame.quit()

# Función para mostrar la selección de categoría
def show_category_selection():
    running = True

    while running:
        screen.fill(BLACK)

        # Mostrar las opciones de categoría
        category_font = pygame.font.Font(None, 36)
        draw_text("Selecciona una categoría:", category_font, WHITE, WIDTH // 2, HEIGHT // 4)
        for i, category in enumerate(categories):
            draw_text(category.name, category_font, WHITE, WIDTH // 2, HEIGHT // 4 + (i + 1) * 40)

        pygame.display.flip()

        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, category in enumerate(categories):
                    if category_font.render(category.name, True, WHITE).get_rect(center=(WIDTH // 2, HEIGHT // 4 + (i + 1) * 40)).collidepoint(event.pos):
                        show_game_screen(category)
                        running = False

    pygame.quit()

# Función para mostrar la pantalla de juego
def show_game_screen(category):
    running = True
    word = category.select_word()
    guessed_letters = []
    attempts = 7

    while running:
        screen.fill(BLACK)

        # Mostrar el título
        title_font = pygame.font.Font(None, 48)
        draw_text("Juego de Adivinanza de Palabras", title_font, WHITE, WIDTH // 2, 50)

        # Mostrar la palabra oculta
        word_font = pygame.font.Font(None, 72)
        masked_word = ""
        for letter in word:
            if letter in guessed_letters:
                masked_word += letter + " "
            else:
                masked_word += "_ "
        draw_text(masked_word, word_font, WHITE, WIDTH // 2, HEIGHT // 2)

        # Mostrar los intentos restantes
        attempts_font = pygame.font.Font(None, 36)
        draw_text(f"Intentos restantes: {attempts}", attempts_font, WHITE, WIDTH // 2, HEIGHT - 100)

        pygame.display.flip()

        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    show_category_selection()
                elif event.key == pygame.K_RETURN:
                    show_game_screen(category)
                elif event.key == pygame.K_BACKSPACE:
                    if guessed_letters:
                        guessed_letters.pop()
                elif event.key >= pygame.K_a and event.key <= pygame.K_z:
                    letter = chr(event.key)
                    if letter not in guessed_letters:
                        guessed_letters.append(letter)

    pygame.quit()

# Función para mostrar la configuración del jugador
def show_player_configuration():
    running = True

    while running:
        screen.fill(BLACK)

        # Mostrar el título
        title_font = pygame.font.Font(None, 48)
        draw_text("Configuración del Jugador", title_font, WHITE, WIDTH // 2, 50)

        pygame.display.flip()

        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

# Función principal para ejecutar el juego
def main():
    show_main_screen()

if __name__ == "__main__":
    main()
