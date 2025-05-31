def e_palindromo(texto):
    texto_processado = texto.replace(" ", "").lower()
    return texto_processado == texto_processado[::-1]

frase = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")
if e_palindromo(frase):
    print(f"\nÓtimo! A frase '{frase}' é um palíndromo!")
else:
    print(f"\nQue pena. A frase '{frase}' não é um palíndromo.")