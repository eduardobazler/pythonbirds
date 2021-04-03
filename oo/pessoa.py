class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 23):  #atibutos de instância
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    eduardo = Pessoa(nome='Eduardo')
    claudio = Pessoa(eduardo, nome='Claudio')
    print(Pessoa.cumprimentar(eduardo))
    print(id(eduardo))
    print(claudio.cumprimentar())
    print(claudio.nome)
    eduardo.sobrenome = 'Bazler'
    print(eduardo.__dict__)
    del eduardo.idade
    print(eduardo.__dict__)