
class Banco:

    def __init__( self, nome, prioridade="N" ):
        self.nome = nome
        self.prioridade = prioridade
        self.proximo = None

    def __str__(self):
        return "Nome: " + self.nome + " - Prioridade: " + self.prioridade