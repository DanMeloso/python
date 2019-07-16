#Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
#O programa encerrará quando ele disser que quer mostrar 0 termos.
termo = int(input('Informe o primeiro termo: '))
razao = int(input('Razão: '))
c = 0
i = 0
cont = 0
while c < 11:
    if c == 10:
        termo = int(input('Quantos termos mais? '))
        i = 0
        if termo == 0:
            print(f'FIM → Foram exibidos {cont} números')
            break
        else:
            while i < termo:
                cont += 1
                numero = numero + razao
                print(numero, end=' → ')
                i += 1
    else:
        c += 1
        if c == 1:
            numero = termo
        else:
            numero = numero + razao
        print(numero, end=' → ')
        cont += 1
