'''
Exercício 2):
Uma academia oferece diversas atividades. A tabela de preços das atividades é 
representada fazendo uso de um dicionário. Cada elemento do dicionário de 
atividades (dativ) é um par:
                 ATIVIDADE: preço mensal
Dicionário a ser considerado no exercício:
dativ= {'ioga':120.0, 'spinning':100, 'musculacao':150, 'judo':150,
        			'alongamento:':120, 'aerobica':120, 'todas':420}
Escreva a função precoTotal que recebe uma lista com as atividades desejadas por um 
aluno e a tabela de precos, e retorna o valor total mensal a ser pago pelo aluno. 
Caso alguma atividade 
solicitada pelo aluno não exista o valor da atividade deve ser considerado 0.0 e 
uma mensagem informando que tal atividade não existe deve ser exibida na tela.

Teste sua função chamando-a para diferentes listas de atividades e exibindo as 
respostas na tela.
Pode considerar que a lista passada é sempre coerente, ou seja, se o aluno desejar 
fazer todas as atividades, será fornecida a lista apenas com ‘todas’.
'''

def precoTotal (lAt, precos):
    tot = 0
    for At in lAt:
        if At in precos:
            preco = precos.get(At)
            tot += preco
    return tot


dativ= {'ioga':120.0, 'spinning':100, 'musculacao':150, 'judo':150,
        			'alongamento':120, 'aerobica':120, 'todas':420}


lat1=['ioga','spinning','alongamento']
lat2=['musculacao','spinning','natacao','judo']

print('\nTestes da Questao 2')
totAc= precoTotal(lat1,dativ)
print("Total na academia: %.2f" %totAc)
totAc= precoTotal(lat2,dativ)
print("Total na academia: %.2f" %totAc)