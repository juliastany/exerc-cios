class Cliente:
  def __init__(self,nome,idade,sexo,email,telefone,endereco):
    self.nome = nome.title()
    self.idade = idade
    self.sexo = sexo.title()
    self.email= email.title()
    self.telefone = telefone.title()
    self.endereco = endereco.title()

  def __str__(self):
      return f'seu nome:{self.nome} sua idade: {self.idade}  eu sexo: {self.sexo} seu email: {self.email} seu telefone: {self.telefone}'


cad1 = Cliente('Julia', 17, 'fem','juliastanichesck@gnail.com','41999473104', 'rua 112')
print (cad1)