pessoa = {

    'Nome': 'Gustavo Amaral',
    'Idade': 40,
    'Profissão': 'Músico',
    'Empresa': 'EMB',
    'Gênero': 'Masculino',
    'Cidade': 'Taguatinga'


}

del pessoa[input('Infomre o nome da chave a ser deletada: ')]

for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')
