# **Função de Saída**

###**Print/Escrever**
print('Olá, mundo!')
print(2+3)
print('2+3')

###**Símbolo de Atribuição**
nota=8.5
disciplina='Lógica de Programação'
print(nota)
print(disciplina)

###**Variável Lógica**
a=1
b=5
resposta = (a==b)
print(resposta)

a=1
b=5
resposta=a!=b
print(resposta)

###**Concatenação de Strings**
s1='Lógica de Programação'
s1=s1+' e Algoritmos'
print(s1)

s1='A'+'-'*10+'B'
print(s1)

###**Composição**
nota=8.5
s1='Voce tirou %f na disciplina de Algoritmos'%nota
print(s1)

s1='Você tirou %.2f na disciplina de Algoritmos'%nota
print(s1)

###**Composição Moderna**
nota=8.5
disciplina='Algoritmos'
s1='Você tirou {} na disciplina de {}'.format(nota,disciplina)
print(s1)

###**Fatiamento**
s1='Lógica de Programação e Algoritmos'
print(s1[0:6])

print(s1[0])

###**Tamanho**
s1='Lógica de Programação e Algoritmos'
tamanho=len(s1)
print(tamanho)

# **Função de Entrada**

###**Input/Ler**
idade=input('Qual sua idade?')
print(idade)

nome=input('Qual seu nome?')
print('Olá {}, seja bem-vindx!'.format(nome))

###**Convertendo dados de entrada**
nota=float(input('Qual nota você recebeu na disciplina?'))
print('Você tirou nota {}'.format(nota))

nota=int(input('Qual nota você recebeu na disciplina?'))
print('Você tirou nota {}'.format(nota))