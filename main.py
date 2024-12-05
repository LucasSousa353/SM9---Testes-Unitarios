import aluno as a;
import turma as t;

alunos = []
alunos.append(a.Aluno('Fabio', 'Teixeira', 0));
alunos.append(a.Aluno('Fabiano', 'Teixeira', 10));
alunos.append(a.Aluno('Melissa', 'Teixeira', 9));

turmaObject = t.Turma();
turmaObject.cadastrarAlunos(alunos);

turmaObject.mostrarAlunos();
print('*'*30)
print('Aluno com menor nota:', turmaObject.menorNota.mostrarAluno())
print('Aluno com maior nota:', turmaObject.maiorNota.mostrarAluno())