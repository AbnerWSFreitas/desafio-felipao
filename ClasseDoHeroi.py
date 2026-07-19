class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        elif self.tipo == "ninja":
            ataque = "shuriken"
        else:
            ataque = "nada"
        print(f"O {self.tipo} atacou usando {ataque}")

heroi1 = Heroi("Gandalf", 100, "mago")
heroi1.atacar()
heroi2 = Heroi("Hagnar", 26, "guerreiro")
heroi2.atacar()
heroi3 = Heroi("Ryu", 25, "monge")
heroi3.atacar()
heroi4 = Heroi("Naruto", 19, "ninja")
heroi4.atacar()
