import json
from models.modelo import Modelo

class Servico:
    def __init__(self, id, descricao, valor, duracao):
        self.__id = id
        self.__descricao = descricao
        self.__valor = valor
        self.__duracao = duracao
        
    def set_id(self, id):
        if (id == ""):
            raise ValueError("ID não pode estar vazio")
        self.__id = id

    def set_descricao(self, descricao):
        if descricao == "":
            raise ValueError("Descrição não pode estar vazia")
        self.__descricao = descricao

    def set_valor(self, valor):
        if valor < 0:
            raise ValueError("Valor deve ser positivo")
        self.__valor = valor

    def set_duracao(self, duracao):
        if duracao <= 0:
            raise ValueError("Duração inválida")
        self.__duracao = duracao

    def get_id(self): 
        return self.__id

    def get_descricao(self): 
        return self.__descricao

    def get_valor(self): 
        return self.__valor

    def get_duracao(self): 
        return self.__duracao

     def __str__(self):
        return f"ID: {self.__id}, {self.__descricao} - R$ {self.__valor:.2f}, {self.__duracao} minutos"

    def to_json(self):
        return {
            "id": self.__id,
            "descricao": self.__descricao,
            "valor": self.__valor,
            "duracao": self.__duracao
        }

class Servicos(Modelo):

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("servicos.json", mode="r") as arquivo:
                dados = json.load(arquivo)
                for dic in dados:
                    obj = Servico(dic["id"], dic["descricao"], dic["valor"], dic["duracao"])
                    cls.objetos.append(obj)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    @classmethod
    def salvar(cls):
        with open("servicos.json", mode="w") as arquivo:
            json.dump([s.to_json() for s in cls.objetos], arquivo, indent=4)