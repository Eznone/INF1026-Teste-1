'''
Exercício 3) Considere uma tupla em que cada elemento é uma tupla com nome e ano 
de nascimento de uma pessoa.
3.A) Escreva a função criaDicAnoQtd que recebe uma tupla como a descrita, cria 
e retorna um dicionário em que cada elemento é  
                         ANO: quantidade de pessoas nascidas nesse ano
(Na verdade podemos dizer que isso é um dicionário de frequência dos anos na tupla 
recebida, em que cada elemento é ANO: número de ocorrências do ano na tupla recebida)

3.B) Escreva a função criaDicAnoPessoas que recebe uma tupla como a descrita, cria 
e retorna um dicionário em que cada elemento é  
                         ANO: lista com as pessoas nascidas nesse ano

'''
def criaDicAnoQtd (tup):
    dic = {}
    for l in tup:
        year = l[1]
        if year in dic:
            dic[year] += 1
        else:
            dic[year] = 1
    return dic

def criaDicAnoPessoas(tup):
    dic = {}
    for l in tup:
        year = l[1]
        if year in dic:
            dic[year].append(l[0])
        else:
            list = []
            list.append(l[0])
            dic[year] = list
    return dic

# Para testes da questao 3:
tpessoas= (('Kadu',1994), ('Dudu',2001), ('Tita',2003), ('Vava',1997), ('Kaka',2003), 
           ('Zeze',2004), ('Tata',2001), ('Duda',2003), ('Buba',1997), ('Nena', 2002),
           ('Vivi',1998), ('Lele',2002), ('Lulu',2004))        

print('\nTestes da Questao 3')           
print('Dicionario ANO: Quantidade de pessoas nascidas no ano')
dAnoQuant= criaDicAnoQtd(tpessoas)
print(dAnoQuant)

print('Dicionario ANO: Lista de pessoas nascidas no ano')
dAnoLPe = criaDicAnoPessoas(tpessoas)
print(dAnoLPe)