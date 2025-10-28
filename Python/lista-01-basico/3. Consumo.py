# Criado por: [Bruno Neemias Alves Mota]

# 1. Quantos litros foram abastecidos
litros = float(input("Digite a quantidade de litros abastecidos: "))

# 2. Quantos quilômetros foram percorridos
km = float(input("Digite a quantidade de quilômetros percorridos: "))

# Verifica se os valores inseridos são válidos
if litros <= 0:
    print("\nErro: A quantidade de litros deve ser maior que zero.")
elif km < 0:
      print("\nErro: A quilometragem não pode ser um valor negativo.")
else:
      # 3. Calculo do consumo
      consumo = km / litros

      # 4.  Resultado
      print(f"\nO consumo médio do veículo é de {consumo:.2f} KM/L.")
