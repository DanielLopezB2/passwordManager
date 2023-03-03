from cryptography.fernet import Fernet


def escribir_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def cargar_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

print()
master_password = input("Cual es la contraseña maestra? ")
key = cargar_key() + master_password.encode()
fer = Fernet(key)
print()


def ver():
    with open('contraseñas.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            usuario, password = data.split("|")
            print("Usuario: ",usuario, "| Contraseña: ",fer.decrypt(password.encode()).decode())


def añadir():
    nombre = input("Usuario de la cuenta: ")
    password = input("Contraseña: ")

    with open('contraseñas.txt', 'a') as f:
        f.write(f"{nombre} | {fer.encrypt(password.encode()).decode()}" "\n")


while True:

    print()
    modo = input("Quiere añadir una nueva contraseña o ver las contraseñas existentes? (añadir, ver) - Ingrese S para salir: ").lower()

    if modo == "s":
        break

    elif modo == "ver":
        print()
        ver()

    elif modo == "añadir":
        print()
        añadir()

    else:
        print()
        print("Opción inválida")
        continue
