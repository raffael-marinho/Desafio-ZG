#-*- coding: utf-8 -*-
import pygame

pygame.init()

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

def trocar_animal(animais):
    resposta = input("Você gostaria de trocar o nome de algum animal? (sim/não): ").strip().lower()
    if resposta == 'sim':
        animal_para_trocar = input("Qual animal você gostaria de trocar?: ").strip()
        
        if animal_para_trocar in animais:
            novo_animal = input(f"Qual é o novo nome para {animal_para_trocar}?: ").strip()
            
            indice = animais.index(animal_para_trocar)
            
            animais[indice] = novo_animal
            
            print(f"A lista atualizada de animais é: {animais}")
        else:
            print(f"O animal {animal_para_trocar} não foi encontrado na lista.")
    else:
        print("Nenhuma alteração foi feita.")

def tocar_musica1():
    trocar_animal(animais)
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

def tocar_musica2():
    print(parte2)
    for i in range(1, len(membros_acoes)+1):
        print("\n" + refrao2)
        for j in range(i):
            print(membros_acoes[j],end=" ")

def tocar_musica_completa():
    tocar_musica1()
    tocar_musica2()

while True:
    print("Escolha uma opção:")
    print("1 - Tocar a primeira música")
    print("2 - Tocar a segunda música")
    print("3 - Tocar a música completa")
    print("0 - Sair")
    
    escolha = input("Digite sua escolha: ")
    
    if escolha == '1':
        tocar_musica1()
    elif escolha == '2':
        tocar_musica2()
    elif escolha == '3':
        tocar_musica_completa()
    elif escolha == '0':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")


pygame.mixer.music.load("musica/musica.mp3")
pygame.mixer.music.play()
input()
pygame.event.wait()
