def count_a(s):
    count = s.lower().count('a')  # Converte a string para minúsculas e conta 'a'
    return f"A letra 'a' aparece {count} vez(es) na string."

# Exemplo de uso
texto = input("Digite uma string: ")
print(count_a(texto))
