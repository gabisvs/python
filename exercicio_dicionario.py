contatos = {
    "Vanderlei": 11999999999,
    "Gabrielli" : [11988888888, 119888888887], #caso uma pessoa tenha mais que um contato
    "Luis" : 11977777777
}

contatos["Erica"] = 11966666666

removed = contatos.pop("Luis")

contatos.update({"Vanderlei" : 12999999999})
"""
outro jeito de atualizar:
contatos["Gabrielli"][0] = 11988888886 

muda o numero de index 0
"""


print("----------Lista Telefônica----------")
print("Nome: Vanderlei, Número:", contatos["Vanderlei"])
print("Nome: Gabrielli, Número:", contatos["Gabrielli"])
print("Nome: Erica, Número:", contatos["Erica"])

print()
print(contatos)
print(f"Número removido: {removed}")

