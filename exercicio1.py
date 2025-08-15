def soma(a, b):
    return a + b

if __name__ == "__main__":
    print("=== Soma de dois números ===")
    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print(f"Soma: {soma(a, b)}")
    except ValueError:
        print("Entrada inválida. Por favor, digite números (ex.: 10, 3.5).")
