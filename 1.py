def soma_elementos(lista):
    return sum(lista)
numeros = []
quantidade = int(input("Quantos números você quer na lista? "))
for i in range(quantidade):
    valor = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(valor)
print(f"A lista é: {numeros}")
print(f"A soma dos elementos é: {soma_elementos(numeros)}")

# ou 

def soma_elementos(lista):
  return sum(lista)

numeros = [10, 20, 30, 40, 50]

print(f"A lista é: {numeros}")
print(f"A soma dos elementos é: {soma_elementos(numeros)}")