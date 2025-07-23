import json
from datetime import datetime
from models.modelo import Modelo

class Relatorio:
    def __init__(self, id, data, id_cliente, id_servico, descricao):
        self.__id = id
        self.__data = data
        self.__id_cliente = id_cliente
        self.__id_servico = id_servico
        self.__descricao = descricao



    def set_id(self, id):
        if id == "":
            raise ValueError("ID não pode estar vazio")
        self.__id = id

    def set_data(self, data):
        if not isinstance(data, datetime):
            raise ValueError("Data deve ser do tipo datetime")
        self.__data = data

    def set_id_cliente(self, id_cliente):
        if id_cliente == "":
            raise ValueError("ID do Cliente não pode estar vazio")
        self.__id_cliente = id_cliente

    def set_id_servico(self, id_servico):
        if id_servico == "":
            raise ValueError("ID do Serviço não pode estar vazio")
        self.__id_servico = id_servico

    def set_descricao(self, descricao):
        if descricao == "":
            raise ValueError("Descrição não pode estar vazia")
        self.__descricao = descricao


def get_id(self): 
    return self.__id

    def get_data(self): 
        return self.__data

    def get_id_cliente(self): 
        return self.__id_cliente

    def get_id_servico(self): 
        return self.__id_servico

    def get_descricao(self): 
        return self.__descricao

    
    def __str__(self):
        return f"ID: {self.__id}, Data: {self.__data.strftime('%d/%m/%Y')}, Cliente: {self.__id_cliente}, Serviço: {self.__id_servico}, Detalhe: {self.__descricao}"

    
    def to_json(self):
        return {
            "id": self.__id,
            "data": self.__data.strftime(%Y-%m-%d %H:%M"),
            "id_cliente": self.__id_cliente,
            "id_servico": self.__id_servico,
            "descricao": self.__descricao
        }

class Relatorios(Modelo):

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("relatorios.json", mode="r") as arquivo:
                dados = json.load(arquivo)
                for dic in dados:
                    data = datetime.strptime(dic["data"], "%d/%m/%Y %H:%M")
                    obj = Relatorio(dic["id"], data, dic["id_cliente"], dic["id_servico"], dic["descricao"])
                    cls.objetos.append(obj)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    @classmethod
    def salvar(cls):
        with open("relatorios.json", mode="w") as arquivo:
            json.dump([r.to_json() for r in cls.objetos], arquivo, indent=4)
            