# Crie um programa que receba os dados de um usuário, armazene-os em um dicionário, e os informe na tela. Os dados cadastrais serão os mesmos encontrados no gerador de pessoas do site 4 devs (em anexo). Ao terminar, envie o link do repositório.

usuario = {    
    'Nome':'',
    'CPF':'',
    'RG':'',
    'Data de Nascimento':'',
    'Sexo':'',
    'Signo':'',
    'Mãe':'',
    'Pai':'',
    'E-mail':'',
    'Senha':'',
    'CEP':'',
    'Endereço':'',
    'Número':'',
    'Bairro':'',
    'Cidade':'',
    'Estado':'',
    'Telefone':'',
    'Celular':'',
    'Altura':'',
    'Peso':'',
    'Tipo Sanguineo':'',
    'Cor Favorita':'',
} 

#adicionar informacoes 
usuario['Nome'] = input('Informe seu Nome: ')
usuario['CPF'] = input('Informe seu CPF: ')
usuario['RG'] = input('Informe seu RG: ')
usuario['Data de Nascimento'] = input('Informe sua Data de Nascimento: ')
usuario['Sexo'] = input('Informe seu Sexo: ')
usuario['Signo'] = input('Informe seu Signo: ')
usuario['Mãe'] = input('Informe o nome da sua Mãe: ')
usuario['Pai'] = input('Informe o nome de seu Pai: ')
usuario['E-mail'] = input('Informe seu E-mail: ')
usuario['Senha'] = input('Informe a Senha: ')
usuario['CEP'] = input('Informe o CEP: ')
usuario['Endereço'] = input('Informe seu Endereço: ')
usuario['Número'] = input('Informe o Número: ')
usuario['Bairro'] = input('Informe seu Bairro: ')
usuario['Cidade'] = input('Informe sua Cidade: ')
usuario['Estado'] = input('Informe seu Estado: ')
usuario['Telefone'] = input('Informe seu Telefone: ')
usuario['Celular'] = input('Informe seu Celular: ')
usuario['Altura'] = input('Informe sua Altura: ').replace(',','.')
usuario['Peso'] = input('Informe seu Peso: ').replace(',','.')
usuario['Tipo Sanguineo'] = input('Informe seu Tipo Sanguineo: ')
usuario['Cor Favorita'] = input('Informe sua Cor Favorita: ')

print('\n')

#exibir dicionario 
for chave in usuario:
    print(f'{chave}: {usuario.get(chave)}')