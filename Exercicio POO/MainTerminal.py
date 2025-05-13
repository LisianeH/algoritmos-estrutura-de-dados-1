from Categoria import Categoria
from Desktop import Desktop
from Notebook import Notebook

categoria_gamer = Categoria( 1, "Gamer" )

desktop = Desktop( "Dell XPS", "Preto", 4500.0, categoria_gamer, "500W" )
print( "Desktop - Potência da Fonte:", desktop.getPotenciaDaFonte() )

desktop.setPotenciaDaFonte( "550W" )
print( "Potência Atualizada:", desktop.getPotenciaDaFonte() )

desktop.cadastrar()

notebook = Notebook( "Acer Aspire", "Prata", 3200.0, categoria_gamer, "8h" )
print( "Notebook - Tempo de Bateria:", notebook.getTempoDeBateria() )

notebook.setTempoDeBateria( "10h" )
print( "Tempo Atualizado:", notebook.getTempoDeBateria() )

notebook.cadastrar()