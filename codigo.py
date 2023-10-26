class Client():
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        self._age = age

class Login(Client):
    

    def __init__(self, name, age, email, cpf):
        super().__init__(name, age)
        self._email = email
        self._cpf = cpf
        
    
    def __str__(self):
      return f'Nome: {self.name}, idade: {self.age}, email: {self.email}, CPF: {self.cpf}'

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email):
        self._email = email

    @property
    def cpf(self):
        return self._cpf
