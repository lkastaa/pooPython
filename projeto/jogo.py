import random

class Personagem:
  def __init__(self, nome, vida, nivel):
    self.__nome = nome
    self.__vida = vida
    self.__nivel = nivel

  def get_nome(self):
    return self.__nome

  def get_vida(self):
    return self.__vida

  def get_nivel(self):
    return self.__nivel
  
  def exibir_detalhes(self):
    return f"\nNome: {self.get_nome()} \nVida: {self.get_vida()} \nNivel: {self.get_nivel()}"
  
  def receber_ataque(self, dano):
    self.__vida -= dano
    if self.__vida < 0:
      self.__vida = 0

  def atacar(self, alvo):
    dano = random.randint(0, self.get_nivel()) * 2
    alvo.receber_ataque(dano)
    print(f"{self.get_nome()} deu {dano} de dano!")
  
class Heroi(Personagem):
  def __init__(self, nome, vida, nivel, habilidade):
    super().__init__(nome, vida, nivel)
    self.__habilidade = habilidade

  def get_habilidade(self):
    return self.__habilidade
  
  def exibir_detalhes(self):
    return f"{super().exibir_detalhes()} \nHailidade: {self.get_habilidade()}"
  
  def especial(self, alvo):
    dano = self.get_nivel() * 5
    alvo.receber_ataque(dano)
    print(f"{self.get_nome()} deu {dano} de dano com seu especial com {self.get_habilidade()}!")
    
class Inimigo(Personagem):
  def __init__(self, nome, vida, nivel, tipo):
    super().__init__(nome, vida, nivel)
    self.__tipo = tipo

  def get_tipo(self):
    return self.__tipo 
  
  def exibir_detalhes(self):
    return f"{super().exibir_detalhes()} \nTipo: {self.get_tipo()}"

class Jogo:
  def __init__(self) -> None:
    self.heroi = Heroi(nome="Eduarrrdoo", vida=100, nivel=49, habilidade="Xaveco")
    self.inimigo = Inimigo(nome="Laura", vida=100, nivel=7, tipo="ignorante")

  def iniciar_batalha(self):
    print("Iniciando Batalha")

    while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
      print("\nDetalhes dos Personagens")
      print(self.heroi.exibir_detalhes())
      print(self.inimigo.exibir_detalhes())

      input("Pressione Enter para atacar...")

      escolha = input("1 - Ataque normal \n2 - Ataque especial: ")
      if (escolha == "1"):
        self.heroi.atacar(self.inimigo)
      elif (escolha == "2"):
        self.heroi.especial(self.inimigo)
      else:
        print("escolha invalida")

      if self.inimigo.get_vida() > 0:
        self.inimigo.atacar(self.heroi)
    
    if self.heroi.get_vida() > 0:
      print("Win!")
    else:
      print("Voce perdeu!")


jogo = Jogo()
jogo.iniciar_batalha()