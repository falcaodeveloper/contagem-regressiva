from time import sleep
from winsound import Beep
import pygame

msnValor = 'Digite o valor para a contagem regressiva:\n'
msnInvalido = ' Valor Inválido! '.center(100, '*')

while True:
    try:
        valor = int(input(msnValor))
        break
    except:
        print(msnInvalido)

contador = valor

print()
while valor > 0:
    valor -= 1
    print(valor)
    sleep(1)

'''
Referência: https://pythonin1minute.com/how-to-beep-in-python/    
Emite um som, (sinal de alerta), apenas no terminal. É um caractere de código de controle não imprimível.
print('\a')

O método Beep específica uma valor em Hz e um outro valor em milissegundos.
Beep(1000, 550)
'''

#Music by Luis Humanoide from Pixabay: https://pixabay.com/music/main-title-cinematic-violin-uplifting-music-147713/
pygame.mixer.init()
pygame.mixer.music.load('cinematic-violin-uplifting-music-147713.mp3')
pygame.mixer.music.play()