"""
Variáveis:

nome_da_variavel = valor_da_variavel

Vantagens:
- Tornam o código dinâmico;
- Armazenam dados;
- Auxiliam no processamento de informações;
"""

a = 11
print(a, id(a))
print(a + 2)
print(a + 3)
print(a + 4)
print(a + 5)

"""
Nomes de variáveis:

Recomendações:
✅ Devem dizer exatamente o que aquele valor representa;
✅ Usar snake_case para nomear variáveis;
✅ sempre usamos letras minúsculas (maiúsculas somente para Classes); 

Regras:
❌ Não pode ter espaço ' ';
❌ Não pode iniciar com número;
❌ Não pode ter char espeial (!@#$%¨&*(), etc);
❌ Não pode ter nome de palavra reservada


Informação 🐍:
- Python é case sensitive;
Portanto a variável com nome quantidade é diferente da variável Quantidade
"""

# ✅ Devem dizer exatamente o que aquele valor representa;
# ✅ Usar snake_case para nomear variáveis;
a = 27
idade_professor = 27

# ❌ Não pode iniciar com número;
# 1berto = True
codugo_produto1 = "#33"

# ❌ Não pode ter char espeial (!@#$%¨&*(), etc)
# *quantidade* = 100

# - Python é case sensitive;
quantidade = 100
Quantidade = 200
print(quantidade, id(quantidade))
print(Quantidade, id(Quantidade))

from keyword import kwlist
print(kwlist)

# if  = "oi"