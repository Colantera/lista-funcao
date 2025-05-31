def maior_elemento(lista):
    return max(lista)
numeros = []
quantidade = int(input("Quantos números você quer na lista? "))
for i in range(quantidade):
    valor = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(valor)
print(f"A lista é: {numeros}")
print(f"O maior elementos é: {maior_elemento(numeros)}")