# autor: michel
# data: 15/07/2026

class Livro:
    def __init__(self, titulo):
        self.titulo = titulo

    def ler(self):
        print(f"Lendo {self.titulo}")

##########################################

livro1 = Livro("O Pequeno Príncipe")
livro2 = Livro("Dom Casmurro")


livro1.ler()  # Imprime: Lendo O Pequeno Príncipe
livro2.ler()  # Imprime: Lendo Dom Casmurro
