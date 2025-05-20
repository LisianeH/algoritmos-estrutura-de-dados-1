from abc import ABC, abstractmethod

class Pessoa( ABC ):

    def __init__( self, id, nome, _cpf ):
        self.id = id
        self.nome = nome
        self._cpf = _cpf

    @abstractmethod
    def marcarPresenca( self ):
        pass

    def matricular( self ):
        pass
    
    def str( self ):
        desc = f'''
            ID: { self.id }
            Aluno: { self.nome }
            CPF: { self._cpf }
        '''
        return desc
