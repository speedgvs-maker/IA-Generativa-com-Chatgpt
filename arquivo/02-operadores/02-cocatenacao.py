# 1. concatenação simples de váriaveis
nome = "Iago"
sobrenome = "Santos"
nome_completo = nome + " " + sobrenome

print("Nome completo:", nome_completo )

# 2. concatenação combinando texto com número
idade = 16
mensagem = "Olá, meu nome é  " + nome_completo + " e eu tenho " + str(idade) + " anos"

print(mensagem)

# 3. números inseridos pelo usúario
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a sua terceira nota: "))
media = (nota_1+nota_2+nota_3) / 3

print("a média das notas é: ", media)
print(f"a média das notas é: {media:.2f}")
print(f"a média das notas é: {round(media,2)}")