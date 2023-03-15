
def percentual(valor,porcentagem):
    return valor * (porcentagem / 100)

def percentual_acrescimo(valor,percentual):
    return valor + percentual

valor = float(input())
porcentagem = float(input())

y = percentual(valor,porcentagem)

z = percentual_acrescimo(valor,porcentagem)

print(f"{y+valor:.2f}")

print(f"{valor-y:.2f}")








