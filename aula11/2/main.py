from FilaBanco import FilaBanco

fila = FilaBanco()

fila.imprimir()
fila.adicionaFila( "João", "N" )
fila.adicionaFila( "Maria", "P" )
fila.adicionaFila( "José", "P" )

fila.atenderCliente()
fila.atenderCliente()

fila.adicionaFila( "Ana", "N" )

fila.atenderCliente()
fila.atenderCliente()

#2) Implemente um sistema de gestão de fila de um 
#  banco que tem uma fila normal e uma prioritária