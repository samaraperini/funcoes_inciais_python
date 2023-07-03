#variáveis
inicio = 0
fim = 100
#verifica quais números são divisíveis por cinco, e exibe aqueles que são
for numero in range(inicio, fim):
  if numero % 5 == 0:
    print(numero)

numero = '127957'
soma = 0

for x in numero:
  soma = soma + int(x)
  print(f'O resultado é {soma}')

# relação dos nomes
nomes = ['Maria', 'Julieta', 'Fernando', 'Cristiano', 'Julieta', 'Maria', 'Fernando', 'Cláudio']
# estrutura que irá armazenar o número de letras de cada nome
qtd_letras = {}
# calcula o tamanho de cada nome (em número de letras) e armazena o valor na estrutura
for nome in nomes:
  qtd_letras[nome] = len(nome)
  print(qtd_letras)

print(len(nomes))
print(len(qtd_letras))