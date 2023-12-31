import random

def sortear_numeros(qtd_sorteios):
    for _ in range(qtd_sorteios):
        numeros_sorteio = []
        
        while len(numeros_sorteio) < 6:
            # Gera um número aleatório entre 1 e 60
            numero = random.randint(1, 60)
            
            # Verifica se o número já foi sorteado
            if numero not in numeros_sorteio:
                numeros_sorteio.append(numero)

        # Ordena os números em ordem crescente
        numeros_sorteio.sort()
        
        # Exibe os números sorteados
        print("Números sorteados: ", numeros_sorteio)

# Pede ao usuário a quantidade de sorteios desejada
qtd_sorteios = int(input("\nQuantos sorteios você deseja realizar? "))

# Chama a função para realizar os sorteios
sortear_numeros(qtd_sorteios)
print()
