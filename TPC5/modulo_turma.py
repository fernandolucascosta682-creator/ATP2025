turma = []
programa = True


def criarTurmaIn(nalunos,turma):
    turma = []
    while nalunos > 0:
        teste = True
        TPC = True
        proj = True
        nome_aluno = input("Insira o nome do aluno:").strip()    
        id_aluno = input("Insira o id do aluno").lower().strip()
        while teste :
            nota_teste = int(input("Insira a nota do teste do aluno:"))
            if nota_teste > 20 or nota_teste < 0:
                print("Nota inválida. Por favor, insira um valor entre 0 e 20.")
            else :
                teste = False
        while TPC:
            nota_TPC = int(input("Insira a nota do TPC do aluno:"))
            if nota_TPC < 0 or nota_TPC > 20:
                print("Nota inválida. Por favor, insira um valor entre 0 e 20.")
            else:
                TPC = False
        while proj:
            nota_projeto = int(input("Insira a nota de projeto do aluno:"))
            if nota_projeto < 0 or nota_projeto > 20:
                print("Nota inválida. Por favor, insira um valor entre 0 e 20.")
            else:
                proj = False
        aluno = (nome_aluno, id_aluno, [nota_teste, nota_TPC, nota_projeto])
        turma.append(aluno)
        nalunos -= 1
    return turma


def inserirTurmaIn(turma):
    teste = True
    TPC = True
    proj = True
    nome_aluno = input("Insira o nome do aluno:").strip()    
    id_aluno = input("Insira o id do aluno").lower().strip()
    while teste :
        nota_teste = int(input("Insira a nota do teste do aluno:"))
        if nota_teste > 20 or nota_teste < 0:
            print("Nota inválida. Por favor, insira um valor entre 0 e 20.")
        else :
            teste = False
        while TPC:
            nota_TPC = int(input("Insira a nota do TPC do aluno:"))
            if nota_TPC < 0 or nota_TPC > 20:
                print("Nota inválida. Por favor, insira um valor entre 0 e 20.")
            else:
                TPC = False
        while proj:
            nota_projeto = int(input("Insira a nota de projeto do aluno:"))
            if nota_projeto < 0 or nota_projeto > 20:
                print("Nota inválida. Por favor, insira um valor entre 0 e 20.")
            else:
                proj = False
        aluno = (nome_aluno, id_aluno, [nota_teste, nota_TPC, nota_projeto])
        turma.append(aluno)
        return turma
        

def listarTurma(turma):
    for a in turma:
        print(f"Aluno: {a[0]}  id: {a[1]}")
    return


def procurarTurmaIn(turma):
    proc_id = input("Insira o id do aluno que pretende procurar:")
    res = False
    for a in turma:
        if proc_id == a [1]:
            print(F"O id {proc_id} pertence ao aluno {a[0]}")
            res = True
    if res == False:
        print(f"Não existe um aluno com o id {proc_id} nesta turma.")
    return


def guardarTurma(turma,nficheiro):
    f = open(f"./ficheiros_turma/{nficheiro}.txt","w")
    for a in turma:
        f.write(f"{a[0]}; {a[1]}; {a[2][0]}; {a[2][1]}; {a[2][2]}\n")
    f.close()
    return


def abrirTurma(turma,nficheiro):
    f = open(f"./ficheiros_turma/{nficheiro}.txt","r")
    for linha in f:
        campos = linha.split(";")
        aluno = (campos[0], campos[1], [int(campos[2]), int(campos[3]), int(campos[4])])
        turma.append(aluno)
    return turma


def sairTurmaIn():
    cont = True
    prog = True
    while cont == True :
        resp = input("De certeza que prentende sair?:")
        if resp.lower().strip() == "sim":
            cont = False
            prog = False
        elif resp.lower().strip() not in ["sim","nao","não"]:
            print("Resposta inválida.")
        elif resp.lower().strip() in ["nao","não"]:
            cont = False
    return prog





