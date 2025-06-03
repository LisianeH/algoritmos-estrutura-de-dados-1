from ListaEncadeadaDuplamenteOrdenada import ListaEncadeadaDuplamenteOrdenada

lista = ListaEncadeadaDuplamenteOrdenada()

lista.add( "João" )
lista.add( "Cleber" )
lista.add( "Daniel" )
lista.add( "Adalto" )

lista.remover( "Cleber" )
lista.remover( "Adalto" )
lista.remover( "Cassio" )

lista.imprimirInverso()