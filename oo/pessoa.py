class Pessoa:
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa() #objeto
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar()) #forma mais usual