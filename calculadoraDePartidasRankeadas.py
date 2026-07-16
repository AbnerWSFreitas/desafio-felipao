def calcularSaldo (vitorias, derrotas):
    saldo = vitorias - derrotas
    return saldo

vitorias = int(input("Quantas vitórias? "))
derrotas = int(input("Quantas derrotas? "))

saldoDeVitorias = calcularSaldo(vitorias, derrotas)
print(saldoDeVitorias)

if saldoDeVitorias <= 10:
    nivel = "Ferro"
elif saldoDeVitorias <= 20:
    nivel = "Bronze"
elif saldoDeVitorias <= 50:
    nivel = "Prata"
elif saldoDeVitorias <= 80:
    nivel = "Ouro"
elif saldoDeVitorias <= 90:
    nivel = "Diamante"
elif saldoDeVitorias <= 100:
    nivel = "Lendário"
else:
    nivel = "Imortal"

print(f"O Herói tem um saldo de {saldoDeVitorias} vitórias e está no nível {nivel}")