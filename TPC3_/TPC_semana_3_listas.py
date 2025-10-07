python
#definição da função (1)
import random

res = []
def aleatLista():
    res.clear()
    N = int(input("Quandos elementos deverá ter a sua lista?"))
    while N > 0 :
        i = random.randrange(1,101)
        res.append(i)
        N = N -1 
    print(f"A sua lista: {res}")
    return res

# definição da função (2)
def lerLista():
    res.clear()
    continuar = "sim"
    while continuar != "não"  :
        res.append(int(input("Acicione um número à lista:")))
        print(f"Os seus números : {res}")
        continuar = input("Pretende adicionar mais números?").lower().strip("")
        while continuar != "sim" and continuar != "não" :
            continuar = input("Escolha inválida. Pretende continuar? (sim ou não)").lower().strip()
    print(f"A sua lista: {res}")
    return res

# definição da função soma (3)
def somaLista() :
    i = 0
    for num in res :
        i = i + num
    print(f"A soma dos números da sua lista é {i}.")
    return i

# definição da função média (4)
def mediaLista() :
    i = 0
    for num in res :
        i = i + num
    i = i / len(res)
    print(f"A média dos números da sua lista é {i}.")
    return i

# definição da função maior da lista (5)
def maiorLista() :
    i = res[0]
    for num in res[1:] :
        if num > i :
            i = num
    print(f"O maior número da sua lista é {i}")
    return i

# definição da função menor da lista (6)
def menorLista() :
    i = res[0]
    for num in res[1:] :
        if num < i :
            i = num
    print(f"O menor número da sua lista é {i}")
    return i
    
# definição da função verificar ordem cresc (7)
def crescLista() :
    cresc = True
    i = 1
    for num in res:   
        while i < len(res):
            if res[i] < res[i - 1]:
                cresc = False
            i = i + 1
    if cresc == True :
        print("A sua lista está ordenada de forma crescente.")
    else :
        print("A sua lista não está ordenada de forma crescente.")
    return

# definição da função ordem decrec(8)
def decrescLista() :
    decresc = True
    i = 1
    for num in res:   
        while i < len(res):
            if res[i] > res[i - 1]:
                decresc = False
            i = i + 1
    if decresc == True :
        print("A sua lista está ordenada de forma decrescente.")
    else :
        print("A sua lista não está ordenada de forma decrescente.")
    return

def procurarLista():
    num = int(input("Escolha um número:"))
    i = 1
    e = 0
    if num in res :
        for n in res:
            if n == num :
                e = i
            i = i + 1
        print(f"{num} está na sua lista e está na posição {e}")
    if num not in res:
        print(f"{num} não está na sua lista.")
    return i

sair = False
while sair != True :
    print("""(1) Criar lista
(2) Ler lista
(3) Soma
(4) Média
(5) Maior
(6) Menor
(7) verificar ordem crescente
(8) verificar ordem decrescente
(9) Procurar
(0) Sair""")
    esc = int(input("Escolha uma função das seguintes opções:"))
    if esc == 1 :
        aleatLista()
    elif esc == 2 :
        lerLista()
    elif esc == 3 :
        somaLista()
    elif esc == 4 :
        mediaLista()
    elif esc == 5 :
        maiorLista()
    elif esc == 6 :
        menorLista()
    elif esc == 7 :
        crescLista()
    elif esc == 8 :
        decrescLista()
    elif esc == 9 :
        procurarLista()
    elif esc == 0 :
        cert = input("Tem a certeza que deseja sair?").lower().strip()
        while cert not in ["sim","não","nao"]:
           cert = input("Escolha inválida. Tem a ceteza que pretende sair?").lower().strip()
        if cert == "sim" :
            sair = True
