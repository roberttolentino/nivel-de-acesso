administrador = input("Você é um administrador? ").upper()
if administrador == "SIM":
    generoAdm = input("Digite o genero do administrador: ").upper()
    if generoAdm == "MASCULINO":
        print("Olá, administrador")
    else:
        print("Olá, administradora")
else:
    guest = input("Você é um convidado? ").upper()
    if guest == "SIM":
        generoGuest = input("digite o genero do convidado: ")
        if generoGuest == "MASCULINO":
            print("Olá, convidado")
        else:
            print("Olá, convidada")
    else:
        user = input("Você é um usuário? ").upper()
        if user == "SIM":
            generoUser = input("digite o genero do usuário: ")
            if generoUser == "MASCULINO":
                print("Olá, usuário")
            else:
                print("Olá, usuária")
        else:
            print("Seja bem vindo, desconhecido(a) ")
