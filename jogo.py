import random

def sorteio(palavras):
    for i in palavras:
        lista_palavra.append(i)
    x=random.choice(lista_palavra)
    return x

palavras = {'BRASIL': 'País', 'BICICLETA': 'Veículo', 'NATAÇÃO': 'Esporte', 'MARROM': 'Cor', 'BONÉ': 'Acessório', 
            'MONITOR': 'Peça de computador', 'MESA': 'Tem na cozinha'}
lista_palavra = []
palavra_sorteada = sorteio(palavras)
erros = 0
letra_descobertas = ['_'] * len(palavra_sorteada)
palavra = ""

print('Dica: {}'.format(palavras[palavra_sorteada]))
while erros != 6 and '_' in letra_descobertas:

    letra = input('Digite uma letra: ').upper()
    
    if len(letra) > 1:
        print('Uma letra por vez. Tente de novo!')

    for x in range(len(palavra_sorteada)):
        if letra == palavra_sorteada[x]:
            letra_descobertas[x] = letra
            palavra= " ".join(letra_descobertas)

    if letra not in palavra_sorteada:
        erros += 1
        print(f'Você errou pela {erros}° vez. Tente de novo!')

    if palavra != "":
        print(f'A palavra é: {palavra}')

if erros == 6:
    print('\nGAME OVER! Você perdeu.')
    print(f'A palavra era {palavra_sorteada}')
if '_' not in letra_descobertas:
    print('\nParabéns, você ganhou o jogo!')