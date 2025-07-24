import json
from models.modelo import Modelo

class Cliente:
    def __init__(self, id, nome, email, telefone, senha):
        self.__id = id
        self.__email = email
       self.__senha = senha
        self.__nome = nome
        self.__fone = fone
 

    def set_id(self, id):
        if (id == ""):
            raise ValueError("ID não pode estar vazio")
        self.__id = id

    def set_nome(self, nome):
        if nome == "":
            raise ValueError("Nome não pode estar vazio")
        self.__nome = nome

    def set_email(self, email):
        if (email == ""):
            raise ValueError("Email não pode estar vazio")
        self.__email = email

    def set_senha(self, senha):
        if (senha == ""):
            raise ValueError("Senha não pode estar vazia")
        self.__senha = senha

    def set_fone(self, fone):
        if fone == "":
            raise ValueError("Telefone não pode estar vazio")
        self.__fone = fone

    def get_id(self):
         return self.__id

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email
    
    def get_senha(self):
        return self.__senha

    def get_fone(self):
        return self.__fone


    
    def __str__(self):
        return f"ID: {self.__id}, Nome: {self.__id}, Email: {self.__email}, Telefone: {self.__fone}"

        def to_json(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "email": self.__email,
            "senha": self.__senha,
            "fone": self.__fone
        }

class Clientes(Modelo):
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try: 
            with open("clientes.json", mode="r") as arquivo:
                dados = json.load(arquivo)
                for dic in daddos:
                    obj = Cliente(dic["id"]
                                  dic["email"]
                                  dic["senha"]
                                  dic["nome"]
                                  dic["fone"])
                    cls.objetos.append(obj)
        except (FileNotFoundError , json.JSONDecodeError):
            pass
        
    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump([c.to_json() for c in cls.objetos], arquivo, indent=4)