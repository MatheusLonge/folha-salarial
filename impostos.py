def irf(n): # Imposto de Renda
    if n <= 2428.81 :
        aliquota = 0.0
        deducao  = 0.0
    elif n <= 2826.66:
        aliquota = 0.075
        deducao  = 182.16
    elif n <= 3751.06:
        aliquota = 0.15
        deducao  = 
    elif n <= 4664.68:
        aliquota=0.225
    elif n > 4664.68:
        aliquota=0.275
    else:
        print('Valor inválido')
    resultado = n / aliquota
    print(resultado)
irf(5000)

