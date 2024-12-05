class Turma:
    def __init__(self):
        self.turma = []
        self.menorNota = None
        self.maiorNota = None

    def cadastrarAlunos(self, alunos):
        for aluno in alunos:
            # Verificar se a nota é válida antes de cadastrar
            if aluno.nota < 0:
                print(f"Nota inválida para o aluno {aluno.nome}: {aluno.nota}. Não será cadastrado.")
                continue
            self.turma.append(aluno)

            # Atualizar a menor nota
            if self.menorNota is None or aluno.nota < self.menorNota.nota:
                self.menorNota = aluno

            # Atualizar a maior nota
            if self.maiorNota is None or aluno.nota > self.maiorNota.nota:
                self.maiorNota = aluno

    def mostrarAlunos(self):
        print('Quantidade de alunos:', len(self.turma))
        for aluno in self.turma:
            print(aluno.mostrarAluno())
