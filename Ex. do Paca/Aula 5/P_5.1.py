#  Dado N > 0 e uma sequência de números inteiros positivos, calcular a média

# entrada de N
N = int(input("Quantos números você gostaria de calcular a média? "))

# inicia o contador e a soma
contador = 0
soma = 0

# consistência dos dados

while N <= 0:
    N = int(input("Insira um valor maior que zero\nDigite um novo valor: "))

# repete N vezes o trecho do programa que faz a soma
while contador < N:
    x = int(input("Digite um número para ser somado: "))
    soma = soma + x
    contador = contador + 1

# imprime a média da soma

print("A média da soma dos números é", soma/N)

