

def quant_horas(minutos):
    return minutos // 60

def quant_min(minutos):
    return minutos % 60

minutos = int(input())

x = quant_horas(minutos)
y = quant_min(minutos)


print(f"{x}:{y}")



