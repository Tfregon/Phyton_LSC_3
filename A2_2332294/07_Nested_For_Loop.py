n = 5

# Primeira metade do padrão (crescente)
for i in range(1, n + 1):#Inicio e fim
    for j in range(i):
        print("*", end="")# aqui o end faz com que o print se mantenha na mesma linha
    print()  # Mudar de linha após cada linha de asteriscos

# Segunda metade do padrão (decrescente)
for i in range(n - 1, 0, -1):#inicio fim e passo
    for j in range(i):
        print("*", end="")
    print()  # Mudar de linha após cada linha de asteriscos

print()

count = 0
for j in range(9):
    if(j<= 9/2):
        count += 1
        symbol = "*"
        print(symbol * count)
    elif(j>9/2):
        count -= 1
        symbol = "*"
        print(symbol * count)
