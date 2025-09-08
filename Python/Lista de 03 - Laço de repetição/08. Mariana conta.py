# Criado por: [Bruno Neemias Alves Mota]

#Exibição do título
print("=== Música: Mariana Conta ===")

# Leitura do número final
limite = int(input("Até que número Mariana irá contar? "))

print("\n--- Música ---\n")

# Repete a contagem de Mariana de 1 até o limite, exibindo cada número duas vezes
for i in range(1, limite + 1):
    print(f"Mariana conta {i}")
    print(f"Mariana conta {i}")

    # Monta a frase de contagem até o número atual, concatenando "é j" para cada valor
    contagem = ""
    for j in range(1, i + 1):
        contagem += f"é {j}, "

    # Exibe a contagem formatada sem o espaço extra no final e imprime a saudação final
    print(contagem.strip())  # Remove o espaço extra no final
    print("É Ana Viva Mariana, Viva Mariana\n")
