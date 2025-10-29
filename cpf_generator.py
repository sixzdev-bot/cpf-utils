import random
import sys

#Defini quantos cpf o programa vai gerar
quantidade_de_cpf = input("Quantos cpf você quer gerar: ")

#Algoritimo que checa se o input digitado é um número ou não
try:
    quantidade_de_cpf_int = int(quantidade_de_cpf)
except ValueError:
    print("Você não digitou um caractere válido")
    sys.exit()

#Nove números iniciais aleatórios
for i in range (quantidade_de_cpf_int):
    cpf_random = ''
    for digito in range (9):
        cpf_random += str(random.randint(0, 9))#Converte os números aleatórios para string para concatenar 

    entrada_e_sequencial = cpf_random == cpf_random[0] * len(cpf_random)

    #Proibe cpfs sequenciais como 11111111111 ou 99999999999 
    if entrada_e_sequencial: 
        print("Você enviou dados sequênciais")
        sys.exit()     

    #Adicionando os nove numeros separados em uma lista
    cpf_lista = []
    for digito in cpf_random:
        cpf_lista.append(digito)

    #Conta do décimo digito 
    contagem_regressiva_1 = 10
    soma_total_digito1 = 0

    for digito_1 in cpf_lista:
        soma_total_digito1 += int(digito_1) * contagem_regressiva_1
        contagem_regressiva_1 -= 1

    primeiro_digito = (soma_total_digito1 * 10) % 11

    primeiro_digito = 0 if primeiro_digito > 9 else primeiro_digito

    #Adiconando o décimo digito na lista dos outros  9
    cpf_lista.append(str(primeiro_digito))

    #Criando o décimo primeiro e ultimo digito
    contagem_regressiva_2 = 11  
    soma_total_digito2 = 0

    for digito_2 in cpf_lista:
        soma_total_digito2 += int(digito_2) * contagem_regressiva_2
        contagem_regressiva_2 -= 1

    segundo_digito = (soma_total_digito2 * 10) % 11

    segundo_digito = 0 if segundo_digito > 9 else segundo_digito

    #cpf sem formatação
    cpf_gerado = f"{cpf_random}{primeiro_digito}{segundo_digito}"
    #cpf formatado
    cpf_formatado = f"{cpf_gerado[:3]}.{cpf_gerado[3:6]}.{cpf_gerado[6:9]}-{cpf_gerado[9:]}"

    print(f"\nCpf número {i+1}:")
    print(cpf_gerado)
    print(cpf_formatado)

