import re
import sys
#Essa conta foi criada pela receita federal para criar um cpf válido
#Esse código refaz a conta dos 9 primeiros digitos, se os dois ultimos baterem com o digitado pelo o usuário, o cpf é válido

#Cpf enviado pelo usuário
cpf_enviado = input('Digite um CPF: ')

#Valida se oque foi enviado pelo usuário está entre 0-9, ou é um caractere inválido.
cpf_enviado = re.sub(r'[^0-9]', '', cpf_enviado)

#Termina o processo caso nao haja 11 digitos
if len(cpf_enviado) < 11:
    print("Não é um cpf válido.")
    sys.exit()#Encerra o python   

#Proibe cpfs sequenciais como 11111111111 ou 99999999999 
entrada_e_sequencial = cpf_enviado == cpf_enviado[0] * len(cpf_enviado)
if entrada_e_sequencial: 
    print("Você enviou dados sequênciais")
    sys.exit() 

#Cria uma lista vazia    
cpf_lista = []

#Adiciona os digitos a lista
for digito in cpf_enviado: 
    cpf_lista.append(digito)

#É necessário a exclusão dos dois ultimos digitos para que possamos fazer a conta com os 9 outros digitos
#Deleta o décimo primeiro digito do cpf   
cpf_lista.pop(10)

#Deleta o décimo digito do cpf 
cpf_lista.pop(9)

#Conta do décimo digito
contagem_regressiva_1 = 10
soma_total_digito1 = 0

for digito_1 in cpf_lista:
    soma_total_digito1 += int(digito_1) * contagem_regressiva_1
    contagem_regressiva_1 -= 1

primeiro_digito = (soma_total_digito1 * 10) % 11

#Se o primeiro digito foi maior que nove, ele passa a ser 0, se não, ele continua valendo ele mesmo
primeiro_digito = 0 if primeiro_digito > 9 else primeiro_digito

#Adicionando o décimo digito a lista
cpf_lista.append(primeiro_digito)

#Conta do décimo primeiro e ultimo digito
soma_total_digito2 = 0
contagem_regressiva_2 = 11

for digito_2 in cpf_lista:
    soma_total_digito2 += int(digito_2) * contagem_regressiva_2
    contagem_regressiva_2 -= 1

segundo_digito = (soma_total_digito2 * 10) % 11
segundo_digito = 0 if segundo_digito > 9 else segundo_digito

#Os nove primeiros digitos mais os dois gerados
cpf_gerado = f"{cpf_enviado[:9]}{primeiro_digito}{segundo_digito}"

#Se os ultimos dois digitos gerados forem == aos do cpf enviado, então o cpf é válido
if cpf_enviado == cpf_gerado:
    print(f'{cpf_enviado} é válido')
else:
    print('CPF não é válido')
