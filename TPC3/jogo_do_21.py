''''python
print("Bem vindo ao jogo dos 21. As regras são simples:")
print("1º Tens de escolher um número de 1 a 4")
print("2º Retira esse valor ao total;")
print("3º O total começa no 21")
print("4º O jogador que não conseguir retirar ao total, ou seja, quando este for igual a 1, perde!")
print("5º Podes escolher se queres ser o 1º ou o 2º a jogar.")
print("Estás pronto?")
fim1 = True # Variável que controla jogo 1
fim2 = True # Variável que controla jogo 2
usuario=input("Escolha o seu jogador (jogador 1/ jogador 2):")
if usuario == "jogador 1" or usuario == "Jogador 1" or usuario == "1" or usuario == "jogador1" or usuario == "Jogador1" :
    print("Jogador 1 selecionado")
    n = 21
    while n > 1 and fim1 == True :
        num1 = int(input("Escolhe um número: 1, 2, 3, 4:"))
        if num1 == 1 or num1 == 2 or num1 == 3 or num1 == 4 :
            print(f"Escolheste {num1}")
            n = n - num1
            print(f"Faltam {n} pontos")
            num2 = 5 - num1
            print(f"O computador escolheu {num2}")
            n = n - num2
            print(f"Faltam {n} pontos")
        else :
            print("Escolha inválida.")
        if n == 1 :
            print("Fim do jogo")
            fim1 = False
    # Fim do jogador 1
elif usuario == "jogador 2" or usuario == "Jogador 2" or usuario == "2" or usuario == "jogador2" or usuario == "Jogador2" :
    print("Jogador 2 selecionado")
    n = 21
    num1 = 1
    print(f"O computador escolheu {num1}")
    n = n - num1
    print(f"Faltam {n} pontos")
    num2 = int(input("Escolhe um número: 1, 2, 3, 4:"))
    if num2 == 1 or num2 == 2 or num2 == 3 or num2 == 4 :
        print(f"Escolheste {num2}")
        n = n - num2
        print(f"Faltam {n} pontos")
        # Se usuário erra
        while n > 1 and fim2 == True:
            if n == 1 :
                        print("Fim do jogo")
                        fim2 = False
            if num1 + num2 != 5 and num1 + num2 != 10 :
                if num1 + num2 < 5 :
                    num1 = 5 - (num1 + num2)
                    print(f"O computador escolheu {num1}")
                    n = n - num1
                    print(f"Faltma {n} pontos")
                    num2 = int(input("Escolhe um número: 1, 2, 3, 4:"))
                    print(f"Escolheste {num2}")
                    if num2 == 1 or num2 == 2 or num2 == 3 or num2 == 4 :
                        n = n - num2
                        print(f"Faltam {n} pontos")
                    while n >= 1 and fim2 == True :
                        num1 = 5 - num2 
                        print(f"O computador escolheu {num1}")
                        n = n - num1
                        print(f"Faltam {n} pontos")
                        num2 = int(input("Escolhe um número: 1, 2, 3, 4:"))
                        print(f"Escolheste {num2}")
                        if num2 == 1 or num2 == 2 or num2 == 3 or num2 == 4 :
                            n = n - num2
                            print(f"Faltam {n} pontos")
                        else : 
                            print("Escolha inválida")
                    if n == 1 :
                        print("Fim do jogo")
                        fim2 = False
                    # Fim da soma ser != 5
                elif num1 + num2 > 5 :
                    num1 = 10 - (num1 + num2)
                    print(f"O computador escolheu {num1}")
                    n = n - num1
                    print(f"Faltam {n} pontos")
                    num2 = int(input("Escolhe um número: 1, 2, 3, 4:"))
                    if num2 == 1 or num2 == 2 or num2 == 3 or num2 == 4 :
                        print(f"Escolheste {num2}")
                        n = n - num2
                        print(f"Faltam {n} pontos")
                    else :
                        print("Escolha inválida")
                    while n >= 1 and fim2 == True :
                        num1 = 5 - num2 
                        print(f"O computador escolheu {num1}")
                        n = n - num1
                        print(f"Faltam {n} pontos")
                        num2 = int(input("Escolhe um número: 1, 2, 3, 4:"))
                        if num2 == 1 or num2 == 2 or num2 == 3 or num2 == 4 :
                            print(f"Escolheste {num2}")
                            n = n - num2
                            print(f"Faltam {n} pontos")
                        else : 
                            print("Escolha inválida")
                    if n == 1 :
                        print("Fim do jogo")
                        fim2 = False
                    # Fim da soma != 10
            # Enquanto não houver erro de cálculo
            else :
                if num1 < 4 :
                    num1 = num1 + 1
                    print(f"O computador escolheu {num1}")
                    n = n - num1
                    print(f"Faltam {n} pontos")
                    num2 = int(input("Escolhe um número: 1, 2, 3, 4:"))
                    print(f"Escolheste {num2}")
                    if num2 == 1 or num2 == 2 or num2 == 3 or num2 == 4 :
                        n = n - num2
                        print(f"Faltam {n} pontos")
                    else :
                        print("Escolha inválida")
                else :
                    num1 = num1 - 1
                    print(f"O computador escolheu {num1}")
                    n = n - num1
                    print(f"Faltam {n} pontos")
                    num2 = int(input("Escolhe um número: 1, 2, 3, 4:"))
                    print(f"Escolheste {num2}")
                    if num2 == 1 or num2 == 2 or num2 == 3 or num2 == 4 :
                        n = n - num2
                        print(f"Faltam {n} pontos")
                    else :
                        print("Escolha inválida")
                if n == 1 :
                    print("Fim do jogo")
                    fim2 = False
else :
    print("Por favor, escolhe um jogador válido.")
'''
