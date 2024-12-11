# Modos de Print
variavel1 = 12345  # essa é uma variavel de valor 12345
print(12345)
print('valor', 12345)  # pode ser utilizado tando aspas simples como duplas.
print('valor = {}'.format(12345))  # aqui o valor no format vai ser colocado dentro das {} na string.
print(f"valor = {variavel1}")  # f string serve para adicionar variavel dentro de um texto
print(
    f"valor = {variavel1:,.2f}")  # aqui temo formatacao com , na casa de milhar e .2f é para colocar 2 casa decimais tipo float

x = 5  # variavel x como valor 5
print(x, type(x))
# print(dir(int)) #Apresenta todos os atributos e métodos disponíveis para determinado tipo de dado, usado com ou sem print
# (help(int)) #Apresenta a documentação relativa a determinado tipo de dado, pode ser usado com ou sem print

# Blocos
a = 0
for i in range(30):  # os : abrem um bloco, que sao linhas dentro desse comando
    if a % 2 == 0:  # para demonstrar que esta dentro do bloco, da-se 4 espacos no comeco da linha. esse espaco no inicio se chama indentacao
        a += 1  # essa linha esta dentro da linha 17, que esta dentro da linha 16
        continue
    else:
        if a % 5 == 0:
            break
        else:
            a += 3
print(a)

"""para realizar comentarios em mais de uma linha, usa-se tres aspas duplas
podendo assim tornar o codigo mais explicativo e defacil acesso"""
# na linguagem C é feito com // para uma linha e /* e */ para comentarios em varias linhas

# Caracteristicas de Variaveis
nome = 'exemplo de string'  # v. string é uma variavel de texto
print(nome, type(nome))

# variaveis nao podem iniciar com numeros
# 9variavel=3 ,por exemplo, da erro
# letras maiusculas e minusculas importam

a, b = 1, 2  # a recebe 1 e b recebe 2
print(a, type(a))
print(b, type(b))
x = 3
print(f"x={x}")
x += 2  # soma
print(f"x={x}")
x -= 2  # subtracao
print(f"x={x}")
x *= 2  # multiplicacao
print(f"x={x}")
x /= 2  # divisao
print(f"x={x}")
x %= 2  # modulo, resto da divisao por 2
print(f"x={x}")
x = 2 ** 3  # exponencial
print(f'x={x}')

# Amarracoes "binding" é a associacao entre entidades de programacao
# amarracao de tipo: vincula a variável ao tipo de dado, podendo ser estáticas(ling. C, C++ e java) ou dinâmicas(python)
# estaticas: Ocorre antes da execução, e ficou inalteradas
# dinamicas: ocorrem durante a execucao e podem seralteradas
tipo = 10
print(type(tipo))  # tipo tem valor 10 e sera tipo int
tipo = 'a'
print(type(tipo))  # alterado o valor de tipo para "a", sera tipo str

# Escopos e Tempo de vida
# escopo é a parte que uma variavel sera visivel, podendo ser uma variavel global ou local
# global: toda variavel definida fora de qualquer funcao
variavel_global = 4


# local: variaveis definidas dentro de funcoes
def multiplicador(numero):
    variavel_local = 2
    print(f'dentro da funcao a variavel vale {variavel_local}')
    return variavel_local * numero


variavel_local = 3
b = multiplicador(5)
print(f'fora da funcao a variavel vale {variavel_local}')
# caso tenha uma variável global e uma variável local com mesmo nome, para chamar a variável global dentro da função se coloca  "global" nome da variável

a = 4
print(a)


def multiplicador(numero):
    global a
    a = 2
    print(a)
    return a * numero


a = 3
b = multiplicador(5)
print("fora da funcao, a=", a)
print("dentro da funcao, a=", b)

# O Escopo podeser dinamico ou estatico, e é um conceito textual
# estatico: ocorrem na compilacao
# dinamico: ocorrem em sequencia de chamada dos modulos (ou funcoes), sendo, assim, feitas em tempo de execuçao
# O tempo de vida é um conceito temporal, as globais tem o tempo de vida que é o do programa, as locais sao no intervalo da execucao da funcao ou bloco que limitam

# Constantes nao existem em python, devendo estabelecer uma variavel e nao alterar ela durante o codigo

# tipos sequenciais e dicionarios
# listas sequenciais:
print('Exemplo de Listas')
lista = [101, 202, 303, 404, 505]  # entre cochetes
print(f'lista[1] = {lista[1]}')
print(f'lista[2] = {lista[2]}')
print(f'lista completa = {lista}')
# dicionarios:
print('Exemplo de Dicionario')
dicionario = {1111: ['joao'], 2222: ["maria"], 3333: ['roberto']}
print(dicionario)
print(f'Primeira pessoa = {dicionario[1111]}')