altura = int(input())
comprimento = int(input())
largura = int(input())

area = largura * comprimento
volume = altura * comprimento * largura
areaparede = (2 * altura * largura) + (2 * altura * comprimento)

print(f' {area} \n {volume} \n {areaparede}')
