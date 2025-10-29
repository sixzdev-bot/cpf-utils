import sys
import re

#Nove números iniciais aleatórios
cpf_enviado = input("Digite os 9 primeiros digitos do cpf: ")
cpf_enviado = re.sub(r'[^0-9]', '', cpf_enviado)#Tudo que não está entre 0-9 essa função tira da string

#Checa se tem mesmo nove digitos
menos_ou_mais_9_digitos = len(cpf_enviado) >  9 or len(cpf_enviado) < 8

if menos_ou_mais_9_digitos:
    print("Mais ou menos que nove digitos.")
    sys.exit()

#Checa se tem algum caractere inválido    
cpf_9_digitos = re.sub(r'[^0-9]', '', cpf_enviado)#Tudo que não está entre 0-9 essa função tira da string

if len(cpf_9_digitos) < 9:
    print("Seu cpf possui caracteres inválidos.")
    sys.exit()

#Proibe cpfs sequenciais como 11111111111 ou 99999999999 
entrada_e_sequencial = cpf_9_digitos == cpf_9_digitos[0] * len(cpf_9_digitos)

if entrada_e_sequencial: 
    print("Você enviou dados sequênciais")
    sys.exit()     

#Adicionando os nove numeros separados em uma lista
cpf_lista = []
for digito in cpf_9_digitos:
    cpf_lista.append(digito)

#Conta do 10 digito 
contagem_regressiva_1 = 10
soma_total_digito1 = 0

for digito_1 in cpf_lista:
    soma_total_digito1 += int(digito_1) * contagem_regressiva_1
    contagem_regressiva_1 -= 1

primeiro_digito = (soma_total_digito1 * 10) % 11

primeiro_digito = 0 if primeiro_digito > 9 else primeiro_digito

#Adiconando o 10 digito aos 9
cpf_lista.append(str(primeiro_digito))

#Criando o 11 digito
contagem_regressiva_2 = 11  
soma_total_digito2 = 0

for digito_2 in cpf_lista:
    soma_total_digito2 += int(digito_2) * contagem_regressiva_2
    contagem_regressiva_2 -= 1

segundo_digito = (soma_total_digito2 * 10) % 11

segundo_digito = 0 if segundo_digito > 9 else segundo_digito

cpf_gerado = f"{cpf_9_digitos}{primeiro_digito}{segundo_digito}"

cpf_formatado = f"{cpf_gerado[:3]}.{cpf_gerado[3:6]}.{cpf_gerado[6:9]}-{cpf_gerado[9:]}"

print(f"Os dois ultimos digitos do seu cpf são: {primeiro_digito}{segundo_digito}")

print(f"Seu cpf formatado é: {cpf_formatado}")

