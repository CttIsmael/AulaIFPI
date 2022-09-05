#Imprimir valor do total de segundos ao inserir a hora, minutos e segundos.

segundo = 1
minuto = 60
hora = 3600
horaatual = int(input())
minutoatual = int(input())
segundoatual = int(input())
print(f'{(hora*horaatual)+(minuto*minutoatual)+(segundo*segundoatual)}')
