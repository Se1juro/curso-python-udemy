def pedir_pizza():
    print("Pedir pizza")


pedir_pizza()


def validar_entrada(edad):
    if edad < 18:
        print("No puedes entrar")
    elif edad >= 21:
        print("Puedes entrar y beber")
    else:
        print("Puedes entrar al bar, pero no puedes beber")


validar_entrada(21)
