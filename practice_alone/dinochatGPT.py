import pygame
import random

# Definição das constantes do jogo
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 300
GROUND_HEIGHT = 280
FPS = 60
GRAVITY = 1

# Inicialização do Pygame
pygame.init()

# Criação da janela do jogo
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo do Dinossauro")

# Criação do dinossauro
class Dinossauro(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("dino.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.bottom = GROUND_HEIGHT
        self.velocity = 0
        self.jump_power = 15

    def update(self):
        # Atualiza a posição do dinossauro
        self.velocity += GRAVITY
        self.rect.bottom += self.velocity
        if self.rect.bottom >= GROUND_HEIGHT:
            self.rect.bottom = GROUND_HEIGHT
            self.velocity = 0

    def jump(self):
        # Faz o dinossauro pular
        if self.rect.bottom >= GROUND_HEIGHT:
            self.velocity = -self.jump_power

# Criação dos obstáculos
class Obstaculo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("obstaculo.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.bottom = GROUND_HEIGHT
        self.velocity = -5

    def update(self):
        # Atualiza a posição do obstáculo
        self.rect.left += self.velocity
        if self.rect.right < 0:
            self.kill()

# Criação dos grupos de sprites
all_sprites = pygame.sprite.Group()
obstaculos = pygame.sprite.Group()

# Criação do dinossauro
dinossauro = Dinossauro()
all_sprites.add(dinossauro)

# Loop principal do jogo
running = True
clock = pygame.time.Clock()
while running:
    # Eventos do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dinossauro.jump()

    # Criação dos obstáculos aleatórios
    if random.randint(0, 60) == 0:
        obstaculo = Obstaculo()
        all_sprites.add(obstaculo)
        obstaculos.add(obstaculo)

    # Atualização dos sprites
    all_sprites.update()

    # Detecção de colisão
    if pygame.sprite.spritecollide(dinossauro, obstaculos, False):
        running