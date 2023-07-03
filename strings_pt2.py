#variáveis
nome = 'João da Silva'
cidade = 'São Paulo'
cpf = '123.456.789-00'

##função upper(letra maiúscula)
nome = nome.upper()
cidade = cidade.upper()
cpf = cpf.upper()
print(nome,cidade,cpf)

##função upper(letra minúscula)
nome = nome.lower()
cidade = cidade.lower()
cpf = cpf.lower()
print(nome,cidade,cpf)

#função find(localizar)
print(nome.find('ã'))
print(cidade.find('ã'))
print(cpf.find('ã'))

#função len(contar número de caracteres)
print(len(nome))
print(len(cidade))
print(len(cpf))

#função replace(substituir)
cpf = cpf.replace('.','')
cpf = cpf.replace('-','')
print(cpf)