def contar_caracteres(texto, caractere):
    contador = 0
    for atual in texto:
        if atual == caractere:
            contador = contador +1
    return contador

string = input("Digite o texto: ")
caractere = input("Qual caractere vocé deseja saber quantas vezes se repete? ")

repete = contar_caracteres(string, caractere)

print(f"A string é: {string}")
print(f"O caractere '{caractere}' aparece {repete} vezes.")