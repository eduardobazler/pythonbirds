class Pessoa:
    def __init__(self, nome = None, idade = 23):
        self.nome = nome
        self.idade = idade
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa()
    p.nome = 'eduardo'
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)