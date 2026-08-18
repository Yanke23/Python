from filme import Filme
from serie import Serie

def main():
    # Array de tamanho 10 igual no Java
    catalogo = [None] * 10
    
    catalogo[0] = Filme("Filme", "A culpa é das estrelas", 140)
    catalogo[0].Descricao()
    
    catalogo[1] = Serie("Série", "The 100", 40, 12, 2)
    catalogo[1].Descricao()
    
    catalogo[2] = Filme("Filme", "Efeito Borboleta", 210)
    catalogo[2].Descricao()
    
    catalogo[3] = Serie("Série", "The Walking Dead", 60, 15, 8)
    catalogo[3].Descricao()
    
    catalogo[4] = Filme("Filme", "Forest Gump", 200)
    catalogo[4].Descricao()
    
    catalogo[5] = Serie("Série", "Sabrina", 52, 8, 2)
    catalogo[5].Descricao()
    
    catalogo[6] = Filme("Filme", "O Bombardeiro", 225)
    catalogo[6].Descricao()
    
    catalogo[7] = Serie("Série", "Sandman", 62, 11, 1)
    catalogo[7].Descricao()
    
    catalogo[8] = Filme("Filme", "O amanhã", 175)
    catalogo[8].Descricao()
    
    catalogo[9] = Serie("Série", "Flash", 53, 23, 5)
    catalogo[9].Descricao()

if __name__ == "__main__":
    main()