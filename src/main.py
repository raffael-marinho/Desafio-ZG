#-*- coding: utf-8 -*-
import pygame

pygame.mixer.init()

refrao1 = "Erguei as mãos e dai glória a Deus\nErguei as mãos e dai glória a Deus\nErguei as mãos\nE cantai como os filhos do Senhor\n"
animais = ["O elefante","E os passarinhos","A minhoquinha","E os pinguins","O canguru","E o sapinho"]
strof1 = f"Os animaizinhos subiram de dois em dois\nOs animaizinhos subiram de dois em dois\n{0}\n"
strof2 = f"{0}, como os filhos do Senhor"
strof_completa = []
strof3 = "Deus disse a Noé: Constrói uma arca\nDeus disse a Noé: Constrói uma arca\nQue seja feita\nDe madeira para os filhos do Senhor\n"
parte1 = "Por isso...!\n"
parte2 = "E atenção agora, porque"
refrao2 = "\nO senhor tem muitos filhos\nMuitos filhos ele tem\nEu sou um deles, você também\nLouvemos ao senhor\n"
membros_acoes = ["Braço direito",", braço esquerdo\n","Perna direita",", perna esquerda\n","Balanca a cabeça",", dá uma voltinha\n","Dá um pulinho","e abraça o irmão"]

def tocar_musica():
    print(refrao1)
    for indice,animal in enumerate(animais):
        if indice%2==0:
            strof_completa = f"Os animaizinhos subiram de dois em dois\nOs animaizinhos subiram de dois em dois\n{animal}"
        elif indice%2==1:
            strof_completa = f"{animal}, como os filhos do Senhor\n"
        print(strof_completa)
    print(strof3)
    print(parte1)
    for _ in range(3):
        print(refrao1)
    print(parte2)
    for i in range(1, len(membros_acoes)+1):
        print("\n" + refrao2)
        for j in range(i):
            print(membros_acoes[j],end=" ")

tocar_musica()

pygame.mixer.music.load("musica/musica.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)