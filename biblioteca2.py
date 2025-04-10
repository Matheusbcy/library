class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        
    def __str__(self):
        return f"{self.titulo} - {self.autor} - {self.ano}"
    
class Biblioteca:
    def __init__(self):
        self.livros = []
        
    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro {livro.titulo} adicionado com sucesso!")
    
    def listar_livro(self):
        if not self.livros:
            print("Nenhum livro cadastrado.")
        else:
            print("Lista de livros:")
            for i, livro in enumerate(self.livros, start=1):
                print(f"{i}. {livro}")
                
    def remover_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo:
                self.livros.remove(livro)
                print(f"Livro: {titulo} removido com sucesso!")
                return
        print(f"Livro {titulo} não encontrado na biblioteca")
        
bib = Biblioteca()

livro1 = Livro("Cem Anos de Solidão", "Gabriel García Márquez", 1967)
livro2 = Livro("1984", "George Orwell", 1949)
livro3 = Livro("A Coragem de Ser Imperfeito", "Brené Brown", 2012)

bib.adicionar_livro(livro1)
bib.adicionar_livro(livro2)
bib.adicionar_livro(livro3)

bib.listar_livro()

titulo_remover = input("\nDigite o título do livro que deseja remover: ").strip()
bib.remover_livro(titulo_remover)

bib.listar_livro()