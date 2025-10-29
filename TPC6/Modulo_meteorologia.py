def medias(tabMeteo):
    res = []
    for d in tabMeteo :
        media = (d[1] + d[2])/2
        data = d[0]
        res.append((data,media))
    return res


def guardaTabMeteo(t, fnome):
    f = open(fnome, "w", encoding = "utf-8")
    for i in t:
        f.write(f"{i[0][0]};{i[0][1]};{i[0][2]};{i[1]};{i[2]};{i[3]}\n")
    f.close()
    return


def carregaTabMeteo(fnome):
    res = []
    f = open(fnome, "r", encoding= "utf-8")
    for linha in f:
        campos = linha.split(";")
        res.append((((int(campos[0]),int(campos[1]),int(campos[2])),float(campos[3]),float(campos[4]),float(campos[5]))))
    f.close()
    return res


def minMin(tabMeteo):
    minima = tabMeteo[0][1]
    for d in tabMeteo[1:]:
        if d[1] < minima:
            minima = d[1]
    return minima


def maxMax(tabMeteo):
    maxima = tabMeteo[0][2]
    for d in tabMeteo[1:]:
        if d[2] > maxima:
            maxima = d[2]
    return maxima


def amplTerm(tabMeteo):
    res = []
    for d in tabMeteo:
        res.append((d[0],d[2]-d[1]))
    return res 


def maxChuva(tabMeteo):
    max_prec = tabMeteo[0][3]
    max_data = tabMeteo[0][0]
    for d in tabMeteo[1:]:
        if d[3] > max_prec:
            max_prec = d[3]
            max_data = d[0]
    return (max_data, max_prec)


def diasChuvosos(tabMeteo, p):
    res = []
    for d in tabMeteo:
        if d[3] > p :
            res.append((d[0],d[3]))
    return res

def diasSecos(tabMeteo, p):
    res = []
    for d in tabMeteo:
        if d[3] < p :
            res.append((d[0],d[3]))
    return res


def maxPeriodoCalor(tabMeteo, p):
    i = 1
    count = 0
    count_max = 0
    while i < len(tabMeteo):
        if tabMeteo[i][3] < p :
            if tabMeteo[i-1][3] < p:
                count = count + 1
                if count > count_max:
                    count_max = count
            else :
                count = 1
        else : 
            count = 0
        i = i + 1
    return count_max


def maxPeriodoChuva(tabMeteo, p):
    i = 1
    count = 0
    count_max= 0
    while i < len(tabMeteo):
        if tabMeteo[i][3] > p :
            if tabMeteo[i-1][3] > p:
                count = count + 1
                if count > count_max:
                    count_max = count
            else :
                count = 1
        else : 
            count = 0
        i = i + 1
    return count_max


def grafTabMeteo(tabMeteo):

    import matplotlib.pyplot as plt

    def datasTabMeteo(t):
        res = []
        for data,_,_,_ in t :
            res.append(data[2])
        return res

    
    def extraiMinTemp(t):
        res = []
        for _,tmin,_,_ in t :
            res.append(tmin)
        return res
    

    def extraiMaxTemp(t):
        res = []
        for _,_,tmax,_ in t:
            res.append(tmax)
        return res
    

    def extraiPrecip(t):
        res = []
        for _,_,_,precip in t:
            res.append(precip)
        return res
    

    def maiorTempMax(t):
        lista = extraiMaxTemp(t)
        maior = lista[0]
        for r in lista[1:]:
            if r > maior:
                maior = r
        return maior
    

    def menorTempMin(t):
        lista = extraiMinTemp(t)
        menor = lista[0]
        for r in lista[1:]:
            if r < menor:
                menor = r
        return menor
    

    x1 = datasTabMeteo(tabMeteo)
    y1 = extraiMinTemp(tabMeteo)
    plt.plot(x1,y1, label = "Temperatura mínima", color = "blue", linewidth= 2, marker = "o" )

    x2 = datasTabMeteo(tabMeteo)
    y2 = extraiMaxTemp(tabMeteo)
    plt.plot(x2,y2,label = "Temperatura máxima", color = "red", linewidth = 2, marker = "v")

    x3 = datasTabMeteo(tabMeteo)
    y3 = extraiPrecip(tabMeteo)
    plt.plot(x3,y3,label = "Precipitação", color = "green", linewidth = 1, marker = "*")

    plt.title("Registos diários de meteorologia")
    plt.xlabel("Dia do registo")
    plt.ylabel("Valor")
    plt.yticks([x for x in range (round(menorTempMin(tabMeteo)-3),round(maiorTempMax(tabMeteo)+3))])
    plt.legend(title = "Legenda" , loc = "best", fontsize = 14, facecolor = "white", edgecolor = "black")
    plt.show()

    return


def sairTabMeteoIn():
    cont = True
    res = True
    while cont:
        esc = input("De certeza que pretende sair?").lower().strip()
        if esc == "sim":
            res = False
            cont = False
        elif esc in ["não","nao"]:
            cont = False
        else :
            print("Resposta inválida")
    return res
