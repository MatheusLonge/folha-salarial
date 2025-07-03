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
def inss(salario):
    salario = float(input("Digite o salário bruto: "))
    if salario <= 1518 :
         aliquota = 0.075
         deducao  = 0.0
    if salario <= 2793.88 :
         aliquota = 0.09
         deducao  = 22.77
    if salario <= 4190.83:
         aliquota = 0.12
         deducao  = 106.59
    if salario >= 8157.41:
         aliquota = 0.14
         deducao  = 190.40
    resultado = salario * aliquota -  deducao
    print("Será descontado R$", round(resultado, ndigits=2), "de inss")
inss(0)
