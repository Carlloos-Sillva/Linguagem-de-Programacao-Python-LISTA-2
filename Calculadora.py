# calculadora em Python

operacao = ''
while operacao != "sair":

    operacao = input(" Qual operacao desejada (soma, sub, mult, div e sair):")
    numero_1 = input("  Digite primeiro número: ")
    numero_2 = input("  Digite segundo número: ")

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
    elif operacao == "sair":
        break
    else:
        resultado = "Operador não valido. Utilizar apenas SOMA, SUB, MULT, DIV e SAIR. "

    print(resultado, 'Resultado dessa operação')
operacao = input(" Qual operacao desejada (soma, sub, mult, div e sair):")