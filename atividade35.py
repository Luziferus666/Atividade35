#Ler uma lista de 10 números reais e mostre-os na ordem inversa.
numeros = [float(input(f"Digite o número {i + 1}: ")) for i in range(10)]
print("Números na ordem inversa:")
for num in reversed(numeros):
    print(num)