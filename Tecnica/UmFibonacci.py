def fibonacci_check(n):
    # Gera a sequência de Fibonacci até n
    fib_sequence = [0, 1]
    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        if next_fib > n:
            break
        fib_sequence.append(next_fib)

    # Verifica se n está na sequência
    if n in fib_sequence:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} NÃO pertence à sequência de Fibonacci."


# Exemplo de uso
numero = int(input("Informe um número: "))
print(fibonacci_check(numero))
