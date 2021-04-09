class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome = None, idade = 23):  #atibutos de instância
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_da_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homen(Pessoa):  #A classe pessoa Herda os atribudos da classe Pessoa
    def cumprimentar(self):
        cumprementar_classe_Pessoa = super().cumprimentar()
        return f'{cumprementar_classe_Pessoa}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 7

if __name__ == '__main__':
    eduardo = Mutante(nome='Eduardo')
    claudio = Homen(eduardo, nome='Claudio')
    print(Pessoa.cumprimentar(eduardo))
    print(id(eduardo))
    print(claudio.cumprimentar())
    print(claudio.nome)
    eduardo.sobrenome = 'Bazler'
    print(eduardo.__dict__)
    del eduardo.idade
    print(eduardo.__dict__)

    Pessoa.olhos = 4 #agora, quando eu troco na classe, todos os objetos, exceto eduardo, terá o valor de 4
    print(Pessoa.olhos)
    print(eduardo.olhos)
    print(eduardo.__dict__)
    print(id(Pessoa.olhos), id(eduardo.olhos))
    print(Pessoa.metodo_estatico(), eduardo.metodo_estatico())
    print(Pessoa.nome_e_atributos_da_classe(), eduardo.nome_e_atributos_da_classe())
    print(eduardo.olhos)
    print(eduardo.cumprimentar())
    print(claudio.cumprimentar())