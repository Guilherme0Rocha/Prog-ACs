def inc():

    sal = float(input())

    if 0 <= sal <= 400.00:
        ganho = sal * 0.15
        sal = sal + ganho
        print("Novo salario: " + '{:.2f}'.format(sal))
        print("Reajuste ganho: " + '{:.2f}'.format(round(ganho)))
        print("Em percentual: " + "15 %")
    elif 400.01 <= sal <= 800.00:
        ganho = sal * 0.12
        sal = sal + ganho
        print("Novo salario: " + '{:.2f}'.format(sal))
        print("Reajuste ganho: " + '{:.2f}'.format(round(ganho)))
        print("Em percentual: " + "12 %")
    elif 800.01 <= sal <= 1200.00:
        ganho = sal * 0.1
        sal = sal + ganho
        print("Novo salario: " + '{:.2f}'.format(sal))
        print("Reajuste ganho: " + '{:.2f}'.format(round(ganho)))
        print("Em percentual: " + "10 %")
    elif 1200.01 <= sal <= 2000.00:
        ganho = sal * 0.07
        sal = sal + ganho
        print("Novo salario: " + '{:.2f}'.format(sal))
        print("Reajuste ganho: " + '{:.2f}'.format(round(ganho)))
        print("Em percentual: " + "7 %")
    elif sal > 2000.00:
        ganho = sal * 0.04
        sal = sal + ganho
        print("Novo salario: " + '{:.2f}'.format(sal))
        print("Reajuste ganho: " + '{:.2f}'.format(round(ganho)))
        print("Em percentual: " + "4 %")

inc()