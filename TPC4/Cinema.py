python


def inserirCinema(listac,sala) :
    for s in listac:
        if s[0]== sala:
            print(f"A sala {sala} já existe")
            return listac
    lugares = int(input("Quantos lugares terá a sala?:"))
    filme = input("Qual o filme que será exibido?:")
    nova_sala = [sala,lugares,[],filme]
    listac.append(nova_sala)
    print(f"Sala {sala} foi adicionada")
    return listac


def retirarCinema(listac,filme):
    for sala in listac :
        if sala[3] == filme:
            listac.remove(sala)
            return listac
    print("Esta sala não existe.")
    return listac


def listarCinema (listac):
    i = 0
    for i,sala in enumerate(listac):
        print(f"Sala: {sala[0]}-{sala[3]}")
    return 



def disponibilidadeCinema(listac, filme, lugar ) :
    res = False
    for sala in listac :
        if filme == sala[3]:
            if lugar <= sala[1]:
                if lugar not in sala[2] :
                    res = True
                else:
                    print(f"O teu lugar {lugar} já está ocupado")
            else :
                print(f"O lugar {lugar} não existe nesta sala")
    return res


def vendabilheteCinema(listac, filme, lugar) :
    for sala in listac:
        if filme == sala[3]:
            if lugar <= sala[1] and lugar > 0 :
                if lugar not in sala[2]:
                    sala[2].append(lugar)
                    sala[2].sort()
                    print(f"O lugar {lugar} está agora ocupado")
                else :
                    print("Este lugar já está preenchido")
            else :
                print(f"O lugar {lugar} não existe nesta sala")
    return listac


def listarsessoesCinema(listac):
    for sala in listac :
        disp = (sala [1] - len(sala[2]))
        print(f"{sala[3]} -> {disp} lugares disponíveis")
    return 


def sairCinema():
    global programa
    cont = True
    while cont == True :
        resp = input("De certeza que prentende sair?:")
        if resp.lower().strip() == "sim":
            cont = False
            programa = False
        elif resp.lower().strip() not in ["sim","nao","não"]:
            print("Resposta inválida.")
        elif resp.lower().strip() in ["nao","não"]:
            cont = False
    return programa


programa = True
listac = []
while programa == True :
    print("""
(1) Inserir nova sala
(2) Retirar sala
(3) Listar filmes disponíveis
(4) Verificar disponibilidade de lugares na sala
(5) Ocupar lugar de uma sala
(6) Listar o número de lugares disponíveis em cada sala
(7) Sair
""")
    sel = input("Qual a função que pretende desempenhar?:")
    if sel == "1" :
        sala = input("Insira o nome da sua nova sala:")
        inserirCinema(listac,sala)
    elif sel == "2" :
        filme = input("Indique o filme em exibição da sala que pretende retirar?").lower().strip()
        retirarCinema(listac,filme)
    elif sel == "3" :
        listarCinema(listac)
    elif sel == "4" :
        filme = input("Qual o filme da sala?:")
        lugar = int(input("Qual o lugar que pretende verificar?:"))
        res = disponibilidadeCinema(listac, filme, lugar )
        if res == True:
            print("Este lugar está disponível")
        else:
            print("Este lugar não está disponível")
    elif sel == "5" :
        filme = input("Qual o filme da sala?:")
        lugar = int(input("Qual o lugar a ocupar?:"))
        vendabilheteCinema(listac, filme, lugar)
    elif sel == "6" :
        listarsessoesCinema(listac)
    elif sel == "7":
        sairCinema()
    else:
        print("Escolha inválida")
