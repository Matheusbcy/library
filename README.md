# 📚 Projeto: Gerenciador de Biblioteca

Este projeto é um mini sistema de gerenciamento de livros feito em Python, utilizando os conceitos de **Programação Orientada a Objetos (POO)**.

---

## 🎯 Objetivo

Praticar:
- Criação de classes
- Atributos e métodos
- Listas de objetos
- Organização de responsabilidades entre classes

---

## 🧱 Estrutura do Código

### 🔤 Classe `Livro`

Armazena informações sobre cada livro:
- Título
- Autor
- Ano de publicação

```python
class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self):
        return f"{self.titulo} - {self.autor} - {self.ano}"
```

---

### 🏛️ Classe `Biblioteca`

Responsável por gerenciar a lista de livros.

#### Métodos:
- `adicionar_livro(livro)`: adiciona um livro à biblioteca
- `listar_livros()`: exibe todos os livros cadastrados
- `remover_livro(titulo)`: remove um livro pelo título

```python
class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro cadastrado.")
        else:
            for i, livro in enumerate(self.livros, start=1):
                print(f"{i}. {livro}")

    def remover_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                self.livros.remove(livro)
                print(f"Livro '{titulo}' removido com sucesso!")
                return
        print(f"Livro '{titulo}' não encontrado na biblioteca.")
```

---

## 🧪 Exemplo de Uso

```python
bib = Biblioteca()

livro1 = Livro("Cem Anos de Solidão", "Gabriel García Márquez", 1967)
livro2 = Livro("1984", "George Orwell", 1949)
livro3 = Livro("A Coragem de Ser Imperfeito", "Brené Brown", 2012)

bib.adicionar_livro(livro1)
bib.adicionar_livro(livro2)
bib.adicionar_livro(livro3)

bib.listar_livros()

titulo_remover = input("Digite o título do livro que deseja remover: ").strip()
bib.remover_livro(titulo_remover)

bib.listar_livros()
```

---

## ✅ Possíveis Melhorias Futuras

- Interface com menu interativo
- Salvamento dos livros em arquivos (`.txt` ou `.json`)
- Leitura automática dos livros ao iniciar o programa

---

Feito com ❤️ em Python!