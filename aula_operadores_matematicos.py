""""""

"""
Operadores Matemáticos:
+ ➡️ Soma
- ➡️ Subtração
* ➡️ Multiplicação
/ ➡️ Divisão
// ➡️ Divisão inteira
% ➡️ Módulo (Resto da divisão)
** ➡️ Potenciação

Regra de Sinais:
+ com + = +
+ com - = -
- com + = -
- com - = +

Prioridades:
Ordem de execução em equações:
**
/ e *
+ e -
"""

# Soma
print(10 + 10)
print(10 + -10)
print(-10 + -10)
print(10 + 25.9)

# Subtração
print(10 - 10)
print(10 - (-10))
print(-10 - 10)
print(-10 - (-10))
print(10 - 3.14)

# Multiplicação
print(10 * 2)
print(10 * -2)
print(-10 * -2)
print(10 * 2 + 5)
print(10 * (2 + 5))

# Divisão
print(10 / 2)
print(10 / -2)
print(-10 / -2)
print(10 / 2 + 5)
print(10 / (2 + 5))

# Potenciação
print(10 ** 2)
print(10 ** -2)
print(144 ** .5)
print(10 ** 2 + 5)
print(10 ** (2 + 5))

# Divisão inteira
print()
print(10 / 3)
print(10 // 3)
print(10// 6)
print(10// 6 + 4)

# Mod (Resto da divisão)
print()
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 % 6)
print(10 % 2)


print()
print()
print()
print()


# Exemplo 1

area = float(input("Digite a área que deseja pintar: "))  # m²
rendimento = 15  # m² / L

litros_necessarios = area / rendimento  # L

quantidade_latas_18 = litros_necessarios // 18
quantidade_latas_3_6 = litros_necessarios % 18 // 3.6

print()
print("--- Veja quantas latas serão necessárias ---")
print(f"Área: {area} m²")
print(f"Quantidade de latas de 18L: {quantidade_latas_18}")
print(f"Quantidade de latas de 3.6L: {quantidade_latas_3_6}")


# Exemplo Cálculo de Valor de imóveis

area = float(input("Área do terreno (em m²): "))
valor_metro_quadrado = float(input("Valor por m²: R$ "))

valor_terreno = area * valor_metro_quadrado

print(f"Valor do terreno é: R$ {valor_terreno:,.2f}")