# Exercício - Estrutura de decisão

# Questão 01 da lista de exercício:

valor = float(input("Digite um valor: "))
if valor > 10:
    print("O valor digitado é maior que 10.")
else:
    print("O valor digitado é menor ou igual a 10.")
print("O valor digitado foi:", valor)



# Questão 02 da lista de exercício:

valor = float(input("Digite um valor: "))
if valor >= 0:
    print("O valor digitado é positivo.")
else:
    print("O valor digitado é negativo.")



# Questão 03 da lista de exercício:

quantidade = int(input("Digite o número de maçãs compradas: "))
if quantidade < 12:
    preco = 1.30
else:
    preco = 1.00
custo_total = quantidade * preco
print("O custo total da compra é R$", custo_total)



# Questão 04 da lista de exercício:

nota1 = float(input("Digite o valor da 1° avaliação"))
nota2 = float(input("Digite o valor da 2° avaliação"))
media = (nota1 + nota2) / 2
print(" a medida aritmética das notas é:", media)
if media >= 6:
    print("O aluno foi aprovado!")
else:
    print("O aluno não foi aprovado!")



# Questão 05 da lista de exercício:

valor1 = float(input("Digite o primeiro valor:"))
valor2 = float(input("Digite o segundo valor:"))
if valor1 > valor2:
    print("O maior valor é:", valor1)
else:
    print("O maior valor é:", valor2)



# Questão 06 da lista de exercício:

a = float(input("Digite o primeiro valor:"))
b = float(input("Digite o segundo valor:"))
if a < b:
    menor = a 
    maior = b
else:
    menor = b
    maior = a
print("Valores em ordem crescente:", menor, maior)



# Questão 07 da lista de exercício:

num_conta = int(input("Digite o número da conta do cliente:"))
saldo = float(input("Digite o saldo da conta:"))
débito = float(input("Digite o débito da conta:"))
crédito = float(input("Digite o crédito da conta:"))

saldo_atual = saldo - débito + crédito
if saldo_atual >=0:
    print("Saldo positivo")
else:
    print("Saldo negativo")



# Questão 08 da lista de exercício:

qtd_atual = int(input("Digite a quantitade atual em estoque:"))
qtd_maxima = int(input("Digite a quantidade máxima em estoque:"))
qtd_mínima = int(input("Digite a quantidade mínima em estoque:"))

qtd_media = (qtd_maxima + qtd_mínima) / 2
if qtd_atual >= qtd_media:
    print("Não efetuar compra")
else:
    print("Efetuar compra")



# Questão 09 da lista de exercício:

nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))

media = (nota1 + nota2) / 2 

if media >= 9.0:
    conceito = "A"
    situação = "Aprovado"

elif media >= 7.5:
    conceito = "B"
    situação = "Aprovado"

elif media >= 6.0:
    conceito = "C"
    situação = "Aprovado"

elif media >= 4.0:
    conceito = "D"
    situação = "Reprovado"

else:
    conceito = "E"
    situação = "Reprovado"

print("notas:", nota1, "e", nota2)
print("média:", media)
print("conceito:", conceito)
print("situação", situação)