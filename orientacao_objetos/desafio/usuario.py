class Usuario:
    def __init__(self, matricula, nome, tipo, email):
        self.matricula = matricula
        self.nome = nome
        self.tipo = tipo #Leitor ouu Redator
        self.email = email
        
    def __str__(self):
        return "%s - %s" % (self.matricula, self.nome)   
        # return f"{self.matricula} - {self.nome}"
        # return "{self.matricula} - {self.nome}".format()
