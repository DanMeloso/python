#Cores no terminal
#usa ANSI
#\033[style;text;backgroundm
#estilos de fonte
#0 = None
#1 = Bold
#4 = Underline
#7 = Negative (inverter as cores de fonte com o as cores do background)

#cor do texto
# 30 --> Branco
# 31 --> Vermelho
# 32 --> Verde
# 33 --> Amarelo
# 34 --> Azul
# 35 --> Roxo
# 36 --> Azul claro
# 37 --> Cinza

#Background
# 40 --> Branco
# 41 --> Vermelho
# 42 --> Verde
# 43 --> Amarelo
# 44 --> Azul
# 45 --> Roxo
# 46 --> Azul Claro
# 47 --> Cinza

print('\033[7;30;47mTESTE')
print('\033[1;31;40mTESTE\033[m')