# Emprego de funçoes: modular o programa, usando "def"
def encontrar_minimo (lista):
    minimo = lista[0]
    for elemento in lista:
        if elemento < minimo:
            minimo = elemento
    return minimo

def ehpar(n):
    r = (n % 2 == 0) # vai retornar true ou false
    return r
def somar(lista):
    soma = 0
    for elemento in lista:
        if ehpar(elemento):
            soma += elemento
    return soma

def fatorial_1(x):
    fatorial = 1
    for i in range(1,x + 1):
        fatorial = fatorial*i
    return fatorial
def fatorial_2(x):
    if((x==0) or (x==1)):
        return 1
    return x*fatorial_2(x-1)

def eh_primo(x):
    if(x<2):
        return False
    i = x//2 # // é divisão inteira
    while(i>1):
        if(x%i==0):
            return False
        i=i-1
    return True
def imprimir_primo(numero,resultado):
    mensagem = f'O numero {numero} não é primo'
    if(resultado):
        mensagem = f'O numero {numero} é primo'
    return mensagem

lista_teste = [54,3,5,40,33]
menor = encontrar_minimo(lista_teste)
soma = somar(lista_teste)
print(f'O menor valor encontrado foi {menor}')
print(f'A soma dos pares é de {soma}')

fat = int(input('Digite o numero para o fatorial: '))
print(f'O fatorial de {fat} é {fatorial_1(fat)}')
print(f'O fatorial de {fat} é {fatorial_2(fat)}')

pri = int(input('Digite o numero para ver se é primo: '))
resultado = eh_primo(pri)
msg = imprimir_primo(pri,resultado)
print(msg)