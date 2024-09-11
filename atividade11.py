# Crie um programa que receba a idade de uma pessoa e classifique-a de acordo com as seguintes faixas etárias:
idade =eval(input("digite a idade"))
if idade >=0 and idade <= 12:
    print("0-12 anos")
    elif idade >= 13 and idade <=17:
    print("adolecente")
    elif idade >= 18 and idade <= 59:
        print("adulto")
        elif idade >= 60:
            print("idoso")

