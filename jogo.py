import pygame

# inicializar
pygame.init()

tamanho_tela = (800, 800)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("Brick Breaker Youtube")

tamanho_bola = 15
bola = pygame.Rect(100, 500, tamanho_bola, tamanho_bola)
tamanho_jogador = 100
jogador = pygame.Rect(0, 750, tamanho_jogador, 15)

qtde_blocos_linha = 8
qtde_linhas_blocos = 5
qtde_total_blocos = qtde_blocos_linha * qtde_linhas_blocos 

def criar_blocos(qtde_blocos_linha, qtde_linhas_blocos):
    blocos = []
    # criar os blocos
    return blocos 

cores ={
    "branca": (255, 255, 255),
    "preta": (0, 0, 0),
    "amarela": (255, 255, 0),
    "azul": (0, 0, 255),
    "verde": (0, 255, 0)
}

fim_jogo = False
potuacao = 0
movimento_bola = [1, 1]

# criar as fuções de jogo

# desenhar as coisas na tela
tela.fill(cores["preta"])

# ciar um loop infinito
while not fim_jogo:
    for evento in pygame.event.get():
        if evento.type == pygame.