lista = [1,2,3,4,5,6,7,8,9,10,11,12,13]
lista_impar = []
for n in lista:
  if (n %2) != 0:
      lista_impar.append(n)
print(lista_impar)

def maior_impar(lista)-> list:
  return print(max(lista_impar))

def menor_impar(lista_impar) -> list:
  return print(min(lista_impar))

def menor_maior_impar(lista_impar) -> list:
  return print('O menor é',min(lista_impar),'e o maior é',max(lista_impar))

menor_impar(lista_impar)
maior_impar(lista_impar)
menor_maior_impar(lista_impar)

