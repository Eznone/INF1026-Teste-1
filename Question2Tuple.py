'''
Exercicio TUPLA/DIC
Ex2)

Em uma administradora de condomínios, um condomínio é representado por:
 	(nomeDoCondominio, CPFdoSindico, salarioSindico, despesaMensal, valorMensalEsperado, num de unidades, num de unidades_inadimplentes , bairro, 
    quantidade de empregados) em que:
 	  - nomeDoCondominio: string com o nome do condomínio
 	  - CPFdoSindico: string com o CPF do síndico
 	  - despesaMensal: valor da despesa do condomínio em um mês
 	  - valorMensalEsperado: valor total que o condomínio deve arrecadar em um mês, mediante  pagamento feito por todas as unidades
 	  - num de unidades: número de unidades do condomínio
 	  - num de unidades_inadimplentes: unidades que não pagaram conta(s) de condomínio

As informacoes dos condominios que comecaram a ser admistrados somente a partir do ano 2020 encontram-se 
na tupla de condominios a seguir:
ttCondominios=(('Condomínio VISCONDE', '057191184-71', 4164.75, 105610.56, 116494.84, 166, 25, 'Bangu', 6),
                ('Condomínio PRINCESA', '637634807-56', 3322.16, 187001.86, 233222.87, 134, 17, 'Centro', 1),
                ('Condomínio SOLAR', '748923456-05', 3055.0, 302781.28, 306556.84, 173, 17, 'Joatinga', 43),
                ('Condomínio ROSAS', '065970727-49', 1276.84, 11339.07, 12765.88, 31, 9, 'Bangu', 47),
                ('Condomínio JARDIM', '127953269-60', 1506.83, 110682.02, 150864.27, 48, 8, 'Leblon', 39),
                ('Condomínio IMPERADOR', '475118871-93', 5599.77, 71044.9, 75992.33, 28, 8, 'Joatinga', 47),
                ('Condomínio ALAMANDA', '115749372-38', 2408.44, 42109.16, 42408.33, 186, 42, 'Centro', 22),
                ('Condomínio VIOLETA', '447030779-35', 3620.82, 7340.92, 16200.64, 54, 5, 'Leblon', 46),
                ('Condomínio GERANIO', '998052813-65', 9777.69, 93324.52, 97776.62, 28, 3, 'Leblon', 41),
                ('Condomínio PEDRA', '757394517-39', 6278.59, 597623.84, 632783.78, 191, 80, 'Barra', 2),
                ('Condomínio TURQUESA', '021105794-45', 6982.39, 226243.09, 269824.97, 128, 35, 'Joatinga', 18),
                ('Condomínio ROCCA', '009173228-94', 4784.41, 42932.66, 47840.1, 26, 12, 'Santa Cruz', 11),
                ('Condomínio AMARELO', '524241695-96', 5447.25, 329434.67, 354471.42, 149, 49, 'Ipanema', 39),
                ('Condomínio CAMPOS', '915711983-44', 6798.22, 459950.99, 467984.22, 176, 58, 'Bangu', 7),
                ('Condomínio RIOS', '569898403-21', 3144.08, 209803.81, 231440.92, 176, 23, 'Leblon', 11),
                ('Condomínio SELVA', '360418037-34', 6533.89, 115232.99, 165336.03, 166, 17, 'Santa Cruz', 5),
                ('Condomínio SOLARIO', '630196508-33', 3359.7, 327700.75, 335590.29, 185, 20, 'Leblon', 50),
                ('Condomínio MADEIRA', '249274956-24', 1316.07, 10529.43, 13164.33, 6, 0, 'Copacabana', 22),
                ('Condomínio TORA', '851201254-65', 1101.4, 9915.54, 11017.69, 23, 9, 'Centro', 33),
                ('Condomínio MARES', '455006768-98', 7129.67, 257344.45, 271296.54, 157, 22, 'Barra', 34))

'''
'''
# Ex2.A)
# Escreva uma função, denominada condominiosDeUmBairro,  que:
# 	o	receba uma tupla de condomínios (ou seja, uma tupla de tuplas) e um bairro,
# 	o	retorne uma tupla de 2 elementos:
# 	 a quantidade total de condomínios do bairro e uma tupla somente com as tuplas correspondentes aos condomínios do bairro recebido.
'''

#Solucao 2A)

def condominiosDeUmBairro(tupla, bairro):
    total = 0
    lBairros = []
    for el in tupla:
        if el[7] == bairro:
            total += 1
            lBairros.append(el)
    return (total, tuple(lBairros))

ttCondominios=(('Condomínio VISCONDE', '057191184-71', 4164.75, 105610.56, 116494.84, 166, 25, 'Bangu', 6),
                ('Condomínio PRINCESA', '637634807-56', 3322.16, 187001.86, 233222.87, 134, 17, 'Centro', 1),
                ('Condomínio SOLAR', '748923456-05', 3055.0, 302781.28, 306556.84, 173, 17, 'Joatinga', 43),
                ('Condomínio ROSAS', '065970727-49', 1276.84, 11339.07, 12765.88, 31, 9, 'Bangu', 47),
                ('Condomínio JARDIM', '127953269-60', 1506.83, 110682.02, 150864.27, 48, 8, 'Leblon', 39),
                ('Condomínio IMPERADOR', '475118871-93', 5599.77, 71044.9, 75992.33, 28, 8, 'Joatinga', 47),
                ('Condomínio ALAMANDA', '115749372-38', 2408.44, 42109.16, 42408.33, 186, 42, 'Centro', 22),
                ('Condomínio VIOLETA', '447030779-35', 3620.82, 7340.92, 16200.64, 54, 5, 'Leblon', 46),
                ('Condomínio GERANIO', '998052813-65', 9777.69, 93324.52, 97776.62, 28, 3, 'Leblon', 41),
                ('Condomínio PEDRA', '757394517-39', 6278.59, 597623.84, 632783.78, 191, 80, 'Barra', 2),
                ('Condomínio TURQUESA', '021105794-45', 6982.39, 226243.09, 269824.97, 128, 35, 'Joatinga', 18),
                ('Condomínio ROCCA', '009173228-94', 4784.41, 42932.66, 47840.1, 26, 12, 'Santa Cruz', 11),
                ('Condomínio AMARELO', '524241695-96', 5447.25, 329434.67, 354471.42, 149, 49, 'Ipanema', 39),
                ('Condomínio CAMPOS', '915711983-44', 6798.22, 459950.99, 467984.22, 176, 58, 'Bangu', 7),
                ('Condomínio RIOS', '569898403-21', 3144.08, 209803.81, 231440.92, 176, 23, 'Leblon', 11),
                ('Condomínio SELVA', '360418037-34', 6533.89, 115232.99, 165336.03, 166, 17, 'Santa Cruz', 5),
                ('Condomínio SOLARIO', '630196508-33', 3359.7, 327700.75, 335590.29, 185, 20, 'Leblon', 50),
                ('Condomínio MADEIRA', '249274956-24', 1316.07, 10529.43, 13164.33, 6, 0, 'Copacabana', 22),
                ('Condomínio TORA', '851201254-65', 1101.4, 9915.54, 11017.69, 23, 9, 'Centro', 33),
                ('Condomínio MARES', '455006768-98', 7129.67, 257344.45, 271296.54, 157, 22, 'Barra', 34))

#print(condominiosDeUmBairro(ttCondominios, 'Centro'))


'''
# Ex2.B)
# Para o item B considere o dicionario com bairros e quantidade de condominios por bairro
# dessa administradora ate o ano de 2020 a seguir:
#     dicBairrosQtdCond={'Leblon': 12, 'Gavea': 12, 'Copacabana': 25, 
#                        'Ipanema': 12, 'Jardim Botanico':16, 'Botafogo':25, 'Barra':23}
    
# Escreva uma função, denominada atualizaDicPorBairro,  que:
# 	o	receba a tupla de condominios ja utilizada no item A e um dicionario como o acima, em que 
#         cada elemento/item eh:
#                           BAIRRO: qtd de condominios do bairro  (ate o ano de 2020)
# 	o	faca a atualizacao do dicionario a partir das informacoes da tupla

'''
#Solucao do 2B:

def atualizaDicPorBairro(tupla, dic):
    bairro = tupla[1][0][7]
    
    dic[bairro] = 0
    for el in tupla[1]:
        dic[bairro] += el[8]
    return dic
    

dicBairrosQtdCond={'Leblon': 12, 'Gavea': 12, 'Copacabana': 25, 'Ipanema': 12, 'Jardim Botanico':16, 'Botafogo':25, 'Barra':23}

updatedDic = atualizaDicPorBairro(condominiosDeUmBairro(ttCondominios, 'Centro'), dicBairrosQtdCond)
print(updatedDic)


