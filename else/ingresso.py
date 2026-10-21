idade = int(input("Digite a sua idade: "))
estn= input("Você é estudante? (s/n): ") == "s"
if idade < 12 or idade >= 60:
    preco = 10
elif estn:
    preco = 15
else:
    preco = 20
print(f"O preço do ingresso é: R${preco:.2f}")