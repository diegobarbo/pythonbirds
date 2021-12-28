class Pessoa:
    olhos = 2 #atributo de classe

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    diego = Pessoa(nome='Diego') #objeto
    mercia = Pessoa(diego, nome='Mércia')  # objeto
    print(Pessoa.cumprimentar(mercia))
    print(id(mercia))
    print(mercia.cumprimentar()) #forma mais usual
    print(mercia.nome)
    print(mercia.idade)
    for filho in mercia.filhos:
        print(filho.nome)

    mercia.sobrenome = 'Barbosa'
    del mercia.filhos
    mercia.olhos = 1
    print(mercia.__dict__)
    print(diego.__dict__)
    print(Pessoa.olhos)
    print(mercia.olhos)
    print(diego.olhos)
    print(id(Pessoa.olhos), id(mercia.olhos), id(diego.olhos))

