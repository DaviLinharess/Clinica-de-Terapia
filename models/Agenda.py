import json
from datetime import datetime
from models.modelo import Modelo

class Agenda:
    def __init__(self, id, data, confirmado, id_cliente, id_servico):
        self.__id = id
        self.__data = data
        self.__confirmado = confirmado
        self.__id_cliente = id_cliente
        self.__id_servico = id_servico

    def set_id(self, id):
        if id == "":
            raise ValueError("ID não pode estar vazio")
        self.__id = id

    def set_data(self, data):
        if not isinstance(data, datetime):
            raise ValueError("Data deve ser do tipo datetime")
        self.__data = data

    def set_confirmado(self, confirmado):
        if not isinstance(confirmado, bool):
            raise ValueError("Confirmado deve ser True ou False")
        self.__confirmado = confirmado

    def set_id_cliente(self, id_cliente):
        self.__id_cliente = id_cliente

    def set_id_servico(self, id_servico):
        self.__id_servico = id_servico


    def get_id(self): 
        return self.__id

    def get_data(self): 
        return self.__data

    def get_confirmado(self): 
        return self.__confirmado

    def get_id_cliente(self): 
        return self.__id_cliente

    def get_id_servico(self): 
        return self.__id_servico

    
    def __str__(self):
        status = "Confirmado" if self.__confirmado else "Pendente"
        return f"ID: {self.__id}, Data: {self.__data.strftime('%d/%m/Y %H:%M')}, Cliente: {self.__id_cliente}, Serviço: {self.__id_serviço}, Status: {status}"

    def to_json(self):
        return {
            "id": self.__id,
            "data": self.__data.strftime("%Y-%m-%d %H:%M"),
            "confirmado": self.__confirmado,
            "id_cliente": self.__id_cliente,
            "id_servico": self.__id_servico
        }
    
class Agendas(Modelo):
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("agendas.json", mode="r") as arquivo:
                dados = json.load(arquivo)
                for dic in dados:
                    datetime.strptime(dic["data"], "%d/%m/%Y %H:%M"),
                    obj = Agenda(dic["id"],
                                 datetime.strptime(dic["data"], "%d/%m/%Y %H:%M"), 
                                 dic["confirmado"], 
                                 dic["id_cliente"], 
                                 dic["id_servico"])
                    cls.objetos.append(obj)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    @classmethod
    def salvar(cls):
        with open("agendas.json", mode="w") as arquivo:
            json.dump([a.to_json() for a in cls.objetos], arquivo, indent=4)