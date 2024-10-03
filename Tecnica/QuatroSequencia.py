# a) Números ímpares
def next_odd_number(sequence):
    return sequence[-1] + 2

# b) Potências de 2
def next_power_of_two(sequence):
    return sequence[-1] * 2

# c) Quadrados perfeitos
def next_square(sequence):
    return (len(sequence) + 1) ** 2

# d) Quadrados perfeitos de números pares
def next_even_square(sequence):
    return (len(sequence) * 2) ** 2

# e) Sequência de Fibonacci
def next_fibonacci(sequence):
    return sequence[-1] + sequence[-2]

# f) Sequência com padrão específico
def next_specific_sequence(sequence):
    return sequence[-1] + 1 if len(sequence) % 2 == 0 else sequence[-1] + 2

# Testando as funções
print("Próximo elemento a):", next_odd_number([1, 3, 5, 7]))
print("Próximo elemento b):", next_power_of_two([2, 4, 8, 16, 32, 64]))
print("Próximo elemento c):", next_square([0, 1, 4, 9, 16, 25, 36]))
print("Próximo elemento d):", next_even_square([4, 16, 36, 64]))
print("Próximo elemento e):", next_fibonacci([1, 1, 2, 3, 5, 8]))
print("Próximo elemento f):", next_specific_sequence([2, 10, 12, 16, 17, 18, 19]))
