'''
EXERCÍCIO DE TUPLA
Ex1) Uma transportadora faz entregas para empresas, transportando caixas contendo os produtos a serem entregues. 
Cada caixa tem identificação, dimensões em cm (comprimento, altura, largura) e peso em Kg. As dimensões são 
representadas por uma tupla de 3 elementos: (comprimento, altura, largura). A caixa é representada por uma tupla 
de 3 elementos: (identificação, dimensões, peso).

O valor cobrado por caixa depende do volume e do peso da caixa, de acordo com a descrição abaixo:
•	volume até 8000 cm3 (inclusive) e peso até 15kg (inclusive) => 30 reais
•	volume até 64000 cm3 (inclusive)  e peso até 30kg (inclusive) => 65 reais
•	volume até 216000 cm3 (inclusive) e peso até 50kg (inclusive)  => 100 reais

Caixas com volume acima de 216000 cm3 ou peso acima de 50kg são rejeitadas, ou seja, não são aceitas pela transportadora.

1.a) Escreva a função avaliaCaixa que:
- recebe uma tupla correspondente a uma caixa
- retorna uma tupla com:
 	(identificação ,'VALIDA', valor a ser pago), caso a caixa possa ser transportada
 	(identificação ,'INVALIDA'), caso a caixa não possa ser transportada.
    
        Saída esperada para as caixas:
('XS1111',(12,21,18),13.4) => ('XS1111', 'VALIDA', 30)
('XX1122',(42,41,45),13.4) => ('XX1122', 'VALIDA', 100)
('RV6677',(62,50,75),25.4) => ('RV6677', 'INVALIDA')

1.b) Escreva a função processaLoteDeCaixas que:
- recebe uma lista de caixas a serem transportadas
- retorna uma tupla de 3 elementos: o valor total a ser pago à transportadora, a lista com as caixas válidas e a lista com as caixas inválidas (rejeitadas)

Essa função usa obrigatoriamente a função avaliaCaixa do item anterior.
Para a lista de caixas lcx a seguir:
lcx=[  ('XS1111',(12,21,18),13.4), ('XX1122',(42,41,45),13.4) ,  ('PS1111',(12,21,18),25.4), 
      ('RV6677',(62,50,75),25.4),  ('MV4444',(30,25,30),21.5), ('RP6677',(32,45,45),55.4) ]
A saída esperada é:
(260.0, [('XS1111', (12, 21, 18), 13.4), ('XX1122', (42, 41, 45), 13.4), ('PS1111', (12, 21, 18), 25.4), 
          ('MV4444', (30, 25, 30), 21.5)], [('RV6677', (62, 50, 75), 25.4), ('RP6677', (32, 45, 45), 55.4)])

Escreva as funcoes pedidas e faca testes com os exemplos dados
'''

def avaliaCaixa(caixa):
    vol = caixa[1][0] * caixa[1][1] * caixa[1][2]
    if vol < 8000 and caixa[2] < 15:
        return tuple([caixa[0], "VALIDA", 30])
    if vol < 64000 and caixa[2] < 30:
        return tuple([caixa[0], "VALIDA", 65])
    if vol < 216000 and caixa[2] < 50:
        return tuple([caixa[0], "VALIDA", 100])
    else:
        return tuple([caixa[0], "INVALIDA"])
    
print(avaliaCaixa(('XS1111',(12,21,18),13.4)))
print(avaliaCaixa(('XX1122',(42,41,45),13.4)))
print(avaliaCaixa(('RV6677',(62,50,75),25.4)))

def processaLoteDeCaixas(lCaixa):
    total = 0
    caixasValidas = []
    caixasInvalidas = []
    for caixa in lCaixa:
        if avaliaCaixa(caixa)[1] == "VALIDA":
            total += avaliaCaixa(caixa)[2]
            caixasValidas.append(caixa)
        else:
            caixasInvalidas.append(caixa)
    return (total, caixasValidas, caixasInvalidas)

lcx=[  ('XS1111',(12,21,18),13.4), ('XX1122',(42,41,45),13.4) ,  ('PS1111',(12,21,18),25.4), 
      ('RV6677',(62,50,75),25.4),  ('MV4444',(30,25,30),21.5), ('RP6677',(32,45,45),55.4) ]

print(processaLoteDeCaixas(lcx))