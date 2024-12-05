import unittest
import aluno as a
import turma as t

class turmaTest(unittest.TestCase):

    def setUp(self):
        print('\nTeste', self._testMethodName, 'sendo executado...')
        self.alunos = []

        self.alunos.append(a.Aluno('Fabio', 'Teixeira', 10))
        self.alunos.append(a.Aluno('Fabiano', 'Teixeira', 8))
        self.alunos.append(a.Aluno('Melissa', 'Teixeira', 7))
        self.alunos.append(a.Aluno('Angela', 'Teixeira', 7))

        self.turmaObject = t.Turma()
        self.turmaObject.cadastrarAlunos(self.alunos)

    def tearDown(self):
        print('Teste', self._testMethodName, 'finalizado.')

    def testMaior(self):
        self.assertEqual(10, self.turmaObject.maiorNota.nota, 'Erro ao encontrar maior nota')

    def testMenor(self):
        self.assertEqual(7, self.turmaObject.menorNota.nota, 'Erro ao encontrar menor nota')

    # Implementação do teste pra verificar se as notas dos alunos acima se estão no range de 0 a 10
    def testIntervalo(self):
        print('\nTestar se o intervalo de notas está correto.')
        for aluno in self.turmaObject.turma:
            self.assertTrue(0 <= aluno.nota <= 10, f"Nota fora do intervalo para o aluno {aluno.nome}: {aluno.nota}")

    # Implementação adicional de verificação se o sistema efetivamente recusa cadastros se forem negativos
    def testNotasNegativas(self):
        print('\nTestar se notas negativas são rejeitadas.')
        alunosInvalidos = [
            a.Aluno('Teste1', 'Sobrenome', -5),
            a.Aluno('Teste2', 'Sobrenome', -1)
        ]
        turmaTestObject = t.Turma()
        turmaTestObject.cadastrarAlunos(alunosInvalidos)
        self.assertEqual(len(turmaTestObject.turma), 0, "Notas negativas não foram rejeitadas corretamente.")

if __name__ == "__main__":
    unittest.main()
