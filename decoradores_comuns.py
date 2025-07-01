class MinhaClasse:
  valor = 10 #Atributo de classe

  def __init__(self, nome) -> None:
    self.nome = nome #Atributo de classe

  #Requer uma instancia
  def metodo_instancia(self):
    return f"{self.nome}"
  
  def metodo_classe(cls):
    return f"{cls.valor}"
  
  @staticmethod
  def metodo_estatico():
    return "Estatico"
  
class Carro:
  def __init__(self, marca, modelo, ano):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano

    @classmethod
    def criar_carro(cls, config):
      marca, modelo, ano = config.split(",")
      return cls(marca, modelo, int(ano))
    
config1 = "Toyota, Corolla, 2025"
carro = Carro.criar_carro(config1)
print(f"Marca: {carro.marca}")
    
    