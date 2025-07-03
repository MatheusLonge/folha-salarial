def irf(valores): # Imposto de Renda
        valores = float(input("Digite o salário bruto: "))
        if valores <= 2428.81 :
            aliquota = 0.0
            deducao  = 0.0
        elif valores <= 2826.66:
            aliquota = 0.075
            deducao  = 182.16
        elif valores <= 3751.06:
            aliquota = 0.15
            deducao  = 394.16
        elif valores <= 4664.68:
            aliquota = 0.225
            deducao  = 675.49  
        elif valores > 4664.68:
            aliquota = 0.275
            deducao  = 908.73
        else:
            print('Valor inválido')
        resultado = valores * aliquota - deducao
        print("O imposto de renda a ser pago é de R$", round(resultado, ndigits=2)
irf(0)
