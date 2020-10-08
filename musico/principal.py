import random
import abc
 
class Instrumento:
  def _init_(self, afinar, tocar):
    self.afinar = afinar
    self.tocar = tocar
 
class Guitarra(Instrumento):
  def afinar(abc):
    print("Afinando guitarrra")
  def tocar(abc):
    print("Tocando guitarra")
 
class Bajo(Instrumento):
  def afinar(abc):
    print("Afinando bajo")
  def tocar(abc):
    print("Tocando bajo")
 
class Violin(Instrumento):
  def afinar(abc):
    print("Afinando violin")
  def tocar(abc):
    print("Tocando violin")
 
class Principal:
  j = Instrumento
  i = random.randint(1,5)
  if i <2:
    j = Guitarra
  elif i < 4:
    j = Bajo
  else:
    j = Violin
  j.afinar(abc)
  j.tocar(abc)