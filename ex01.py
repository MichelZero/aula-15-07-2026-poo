# autor: michel
# data: 15/07/2026

# aula 2-1 - class
# Definição da Classe (exemplo da Aula 1)
class Carro:
    def __init__(self, cor, portas):
        self.cor = cor
        self.portas = portas
        
    def acelerar(self):
        return f"O carro {self.cor} está acelerando!"


#################################################
# Criando Objetos (Instâncias)
carro_azul = Carro("azul", 4)     # Criando um objeto 'carro_azul'
carro_vermelho = Carro("vermelho", 2) # Criando outro objeto 'carro_vermelho'

print(carro_azul.cor)          # Acessando atributo: "azul"
print(carro_vermelho.portas)   # Acessando atributo: 2
print(carro_azul.acelerar())   # Chamando método: "O carro azul está acelerando!"