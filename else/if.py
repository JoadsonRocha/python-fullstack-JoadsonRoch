saldo = 1200
valor = 150.0
if valor < saldo:
    saldo -= valor
    print("compra realizada com sucesso!")
else:
    print("saldo insuficiente para realizar a compra!")
print(f"saldo atual: R${saldo:.2f}")

