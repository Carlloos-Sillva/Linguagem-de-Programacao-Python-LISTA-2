# Calculadora em Python

operacao = ''
while operacao != "sair":

    print()
    operacao = input(" Qual operacao desejada - soma, sub, mult, div ou sair: ")
    if operacao == "sair":
      break
    numero_1 = float(input("  Digite primeiro número: "))
    numero_2 = float(input("  Digite segundo número: "))

    if operacao == "soma":
        resultado = float(numero_1) + float(numero_2)
        print("{} + {} ".format(numero_1, numero_2))
    elif operacao == "sub":
        resultado = float(numero_1) - float(numero_2)
        print("{} - {} ".format(numero_1, numero_2))
    elif operacao == "mult":
        resultado = float(numero_1) * float(numero_2)
        print("{} * {} ".format(numero_1, numero_2))
    elif operacao == "div":
        resultado = float(numero_1) / float(numero_2)
        print("{} / {} ".format(numero_1, numero_2))
   # elif operacao == "sair":
      #  break
    else:
        resultado = "Operador não valido. Utilizar apenas SOMA, SUB, MULT, DIV ou SAIR. "

    print(resultado, ' -  Resultado dessa operação')
print(" Fim do programa")