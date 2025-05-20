from Pessoa import Pessoa

class Aluno( Pessoa ):

    def __init__( self, id, nome, cpf, matricula ):
        super().__init__( id, nome, cpf )
        self.__matricula = matricula

    @property
    def matricula( self ):
        return f"A matrícula do aluno é: {self.__matricula}"

    @matricula.setter
    def matricula( self, matricula ):
        self.__matricula = matricula

    def marcarPresenca( self ):
        super().marcarPresenca
        input = f"Aluno(a) {self.nome} está presente: S/N"
        if ( input == "S" ):
            return "Presença confirmada"
        else:
            return "Aluno não presente"

    def matricular( self ):
        self.id = int( input( "Digite o ID: " ) )
        self.nome = input( "Digite o nome: " )
        self.cpf = input( "Digite o CPF: " )
        self.__matricula = input( "Digite a matrícula: " )

    def __str__( self ):
        return super().str() + f"    Matrícula:  { self.__matricula }"
