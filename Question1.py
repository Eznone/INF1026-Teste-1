"""
Created on Wed Sep  9 03:51:24 2020

@author: Joisa

Exercicios Basicos de Dicionário
Turmas 33C, 33D
"""

'''
Exercício 1)
Considere os seguintes dicionários com informações sobre as turmas de uma determinada 
disciplina:
  dAlunoETurma : dicionário em que cada elemento  chave:valor  é ALUNO:TURMA
  dTurmaEProf : dicionário em que cada elemento  chave:valor  é TURMA:PROFESSOR

1.A) Escreva uma função, denominada qualTurma, que receba um dicionário com alunos e 
suas turmas e o nome de um aluno, exibindo o nome do aluno e a sua turma.
Considere duas possibilidades: 
  Versão 1: o aluno obrigatoriamente está cursando a disciplina
  Versão 2: o aluno pode não estar cursando a disciplina.


1.B) Escreva uma função, denominada qualProfessor, que receba dois dicionários como 
 descritos acima e o nome de um aluno, e retorne o nome do professor desse aluno.
 Obs: o aluno pode não estar cursando a disciplina
'''

def qualTurmaVS1(dicAl, aluno):
    group = dicAl.get(aluno)
    print(f"{aluno} is in group {group}!")


def qualTurmaVS2(dicAl, aluno):
    group = dicAl.get(aluno)
    if group is None:
        print(f"{aluno} is not in any group!")
    else:
        print(f"{aluno} is in group {group}!")


def qualProfessor(dicAl, dicPro, aluno):
    group = dicAl.get(aluno)
    professor = dicPro.get(group)
    print(f"{aluno} is in group {group} with {professor}")


# Para testes da questao 1:
    
dAlunoETurma = {'Nina': '33A', 'Dudu':'33E', 'Gigi':'33A', 'Vava':'33C', 'Kaka':'33C', 
                'Zeze': '33B', 'Tata':'33D', 'Duda':'33A', 'Buba':'33C', 'Nena':'33E',
                'Vivi': '33A', 'Kadu':'33B', 'Tita':'33A', 'Lele':'33A', 'Lulu':'33C'}

dTurmaEProf= {'33A': 'LEO', '33B':'VIK', '33C':'MIA', '33D':'EDU', '33E':'AMY'}

print('\nTestes da Questao 1')
qualTurmaVS1(dAlunoETurma, 'Dudu')
qualTurmaVS1(dAlunoETurma, 'Tata')
qualTurmaVS2(dAlunoETurma, 'Nuno')
qualTurmaVS2(dAlunoETurma, 'Tata')
qualTurmaVS2(dAlunoETurma, 'Vivi')