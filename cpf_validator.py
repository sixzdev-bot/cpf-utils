import re
import sys
cpf_enviado = input('Digite um CPF: ')
cpf_enviado = re.sub(r'[^0-9]', '', cpf_enviado)#Tudo que não está entre 0-9 essa função tira da string

if len(cpf_enviado) < 11:
    print("Não é um cpf válido.")
    sys.exit()#Encerra o python   

entrada_e_sequencial = cpf_enviado == cpf_enviado[0] * len(cpf_enviado)

if entrada_e_sequencial: #Proibe cpfs sequenciais como 11111111111 ou 99999999999 
    print("Você enviou dados sequênciais")
    sys.exit() 
    
cpf_lista = []

for unidade in cpf_enviado: 
    try:
        cpf_int = int(unidade)
    except ValueError:
        print("Não é um número")

    cpf_lista.append(cpf_int)

cpf_lista_salva = cpf_lista.copy()
cpf_lista.pop(10)   
cpf_lista.pop(9)   
 
contagem_regressiva_1 = 10
contagem_regressiva_2 = 11
soma_total_digito1 = 0
soma_total_digito2 = 0
contagem_temporaria = 0

for digito_1 in cpf_lista:
    soma_total_digito1 += digito_1 * contagem_regressiva_1
    contagem_regressiva_1 -= 1

primeiro_digito = (soma_total_digito1 * 10) % 11

primeiro_digito = 0 if primeiro_digito > 9 else primeiro_digito

cpf_lista_salva.pop(10)

for digito_2 in cpf_lista_salva:
    soma_total_digito2 += digito_2 * contagem_regressiva_2
    contagem_regressiva_2 -= 1

segundo_digito = (soma_total_digito2 * 10) % 11

segundo_digito = 0 if segundo_digito > 9 else segundo_digito

cpf_gerado = f"{cpf_enviado[:9]}{primeiro_digito}{segundo_digito}"

if cpf_enviado == cpf_gerado:
    print(f'{cpf_enviado} é válido')
else:
    print('CPF não é válido')

