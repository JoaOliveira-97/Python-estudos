#MODO 1
a=10
b=20
if(a>b):
    maior=a
else:
    maior=b
print(f'Maior: {maior}')

#MODO 2
c=20
d=30
maior=c
if(d>maior):
    maior=d
print(f'Maior: {maior}')

#EXERCICIO 1
e=int(input('Digite o valor a ser verificado: '))
resultado='é impar'
if(e%2==0):
    resultado='é par'
print(f'O Valor digitado é {resultado}.')

#EXERCICIO 2
f=int(input('Digite a nota do aluno: '))
situacao='Aprovado!'
if(f>=5 and f<7):
    situacao='de Recuperação.'
if(f<5):
    situacao='Reprovado.'
print(f'O aluno está {situacao}')

f=int(input('Digite a nota do aluno: '))
if(f>=7): # se for maior ou igual a 7
    situacao='Aprovado!'
elif(f>=5): # se nao se só rodara se nao atender a condicao no if, logo nao precisa colocar o menor que sete
    situacao='de Recuperação.'
else:
    situacao='Reprovado.'
print(f'O aluno está {situacao}')

#EXERCICIO 3
prun=10
qnt=eval(input('Quantos produtos foram comprados? ')) # pode ser usado eval ou int para transformar a string do input em numero
desconto=0
if(qnt>=11):
    desconto=10
if(qnt>=20):
    desconto=20
valtotal=qnt*(prun*(1-desconto/100))
print(f'O valor do desconto será de {desconto}%, ficando o valor total R${valtotal:,.2f}')

#EXERCICIO 4
lista = [10,2,5,7,6,3]
n=len(lista) # lê quantos elementos tem a lista
soma=0
for i in range(n): # range(3) cria uma sequencia 0, 1, 2. range(2,4) cria (2,3). range(2,9,3) cria (2,5,8)
    if(lista[i]%2==0):
        soma=soma+lista[i]
print(f'O Somatorio dos numeros pares é {soma}')

lista = [10,2,5,7,6,3]

soma=0
for num in lista: # for é dado por: for {variavel} in {variavel}
    if(num%2==0):
        soma=soma+num
print(f'O Somatorio dos numeros pares é {soma}')

#EXEMPLOS
idade = eval(input('Informe a idade da criança: \n')) # \n é para a resposta ser dada na proxima linha
if idade < 5:
    print('A criança deve ser vacinada contra a gripe.')
    print('Procure o posto de saúde mais próximo.')
elif idade == 5:
    print('A vacina estará disponível em breve.')
    print('Aguarde as próximas informações.')
else:
    print('A vacinação só ocorrerá daqui a 3 meses.')
    print('Informe-se novamente neste prazo.')
print('Cuide da saúde sempre. Até a próxima.')

nome=input('Qual o seu nome? ')
for letra in nome:
    print(letra)

nomes=['Laura','Roberto','Maria']
for nome in nomes:
    print(nome)

palavra=input('Digite uma palavra: ')
while palavra != 'sair':
    palavra=input('Repetira ate digitar sair: ')

while True: # é um laço infinito, que nao acabara
    palavra=input('Digite uma palavra: ')
    if palavra == 'sair':
        break
    #açao sera repetida indefinitivamente, caso nao tivesse a condicao break
while True: # é um laço infinito, que nao acabara
    num=int(input('Digite um numero: '))
    if num == 5:
        continue
    else:
        print(num)
    break
    # contrario a break, ela continuara enquanto for correto

for num in range(1, 11):
    if num % 2 == 0:
        pass # ele passara e nao ira realizar acao quando o numero for par, imprimindo apenas os impares
    else:
        print(num)
print('Laço encerrado')