import math

# Dicionário que mapeia nomes de funções para operações matemáticas correspondentes
func_map = {
    'sen': math.sin,
    'cos': math.cos,
    'tg': math.tan,
    'sec': lambda x: 1 / math.cos(x),
    'cosec': lambda x: 1 / math.sin(x),
    'tang': math.tan,
    'e': math.e,
    'raiz': lambda x: x ** 0.5,
    'log': math.log,
    'ln': math.log
}

def bisseccao(a, b, n, k, precisao, func, decimal_places):
    while abs(b - a) > precisao and k < n:
        k += 1
        x = a
        y = (a + b) / 2
        z = func(y)
        if func(x) * z < 0:
            b = y
        else:
            a = y
        print("Número de iterações:", k)
        print("Raiz:", round(y, decimal_places))

def secante(x0, x1, precisao, max_iter, func, decimal_places):
    k = 1
    x2 = x1 - func(x1) * (x1 - x0) / (func(x1) - func(x0))
    while k <= max_iter:
        x2 = x1 - func(x1) * (x1 - x0) / (func(x1) - func(x0))
        if abs(func(x2)) < precisao or abs(x2 - x1) < precisao:
            return round(x2, decimal_places), k
        x0, x1 = x1, x2
        k += 1
    print("Número máximo de iterações atingido. Última aproximação:", round(x2, decimal_places))
    return x2, k

def MIL(x0, precisao, func, decimal_places):
    k = 1
    while abs(func(x0)) > precisao and k < 100:
        x0 = func(x0)
        k += 1
    print("Número de iterações:", k)
    print("Raiz:", round(x0, decimal_places))

def newton(x0, precisao, iteracao_max, func, derivada, decimal_places):
    fx = func(x0)
    f_linha = derivada(x0)
    iteracao = 0
    while abs(fx) > precisao and iteracao < iteracao_max:
        iteracao += 1
        x0 = x0 - (fx / f_linha)
        fx = func(x0)
        f_linha = derivada(x0)
    raiz = round(x0, decimal_places)
    print("Raiz aproximada:", raiz)
    print("Número de iterações:", iteracao)

def regula_falsi(a, b, delta1, delta2, maxIter, func, decimal_places):
    if func(a) * func(b) >= 0:
        print("A condição f(a) * f(b) < 0 não é satisfeita. Saindo.")
        return
    x_prev = a
    for iter in range(maxIter):
        x = (a * func(b) - b * func(a)) / (func(b) - func(a))
        if abs((x - x_prev) / x) < delta2:
            print(f"Raiz aproximada encontrada: {round(x, decimal_places)}")
            print(f"Número total de iterações: {iter + 1}")
            return
        x_prev = x
        if func(a) * func(x) < 0:
            b = x
        else:
            a = x
    print("Número máximo de iterações atingido sem encontrar a raiz com a precisão desejada.")

def main():
    print("Digite a função (ex: x**2 - 2):")
    func_str = input()
    func_name = func_str.split('(')[0].strip()
    func = lambda x: func_map.get(func_name, lambda x: eval(func_str))(x)

    print("Escolha o método:")
    print("1. Bissecção")
    print("2. Secante")
    print("3. MIL")
    print("4. Newton")
    print("5. Regula Falsi")
    escolha = int(input("Digite a opção: "))
    decimal_places = int(input("Digite o número de casas decimais: "))

    if escolha == 1:
        a = float(input("Digite o intervalo a: "))
        b = float(input("Digite o intervalo b: "))
        precisao = float(input("Digite a precisão: "))
        bisseccao(a, b, 50, 0, precisao, func, decimal_places)
    elif escolha == 2:
        x0 = float(input("Digite x0: "))
        x1 = float(input("Digite x1: "))
        precisao = float(input("Digite a precisão: "))
        max_iter = int(input("Digite o número máximo de iterações: "))
        raiz, k = secante(x0, x1, precisao, max_iter, func, decimal_places)
        print("Raiz encontrada:", raiz)
    elif escolha == 3:
        x0 = float(input("Digite x0: "))
        precisao = float(input("Digite a precisão: "))
        MIL(x0, precisao, func, decimal_places)
    elif escolha == 4:
        x0 = float(input("Digite x0: "))
        precisao = float(input("Digite a precisão: "))
        derivada_str = input("Digite a derivada da função: ")
        derivada = eval("lambda x: " + derivada_str)
        newton(x0, precisao, 100, func, derivada, decimal_places)
    elif escolha == 5:
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        delta1 = float(input("Digite a precisão delta1: "))
        delta2 = float(input("Digite a precisão delta2: "))
        regula_falsi(a, b, delta1, delta2, 100, func, decimal_places)
    else:
        print("Opção inválida. Saindo.")

if __name__ == "__main__":
    main()
