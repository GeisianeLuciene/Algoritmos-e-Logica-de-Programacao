def media(notas):
    return sum(notas) / len(notas) if notas else 0.0

if __name__ == "__main__":
    print("=== Média de notas ===")
    try:
        qtd = int(input("Quantas notas deseja inserir? "))
        if qtd <= 0:
            print("A quantidade deve ser maior que zero.")
        else:
            notas = []
            for i in range(qtd):
                while True:
                    try:
                        nota = float(input(f"Nota {i+1}: "))
                        notas.append(nota)
                        break
                    except ValueError:
                        print("Entrada inválida. Tente novamente com um número.")
            print(f"Média: {media(notas):.2f}")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro para a quantidade.")
