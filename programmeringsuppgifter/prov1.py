import random

#1
class Turtle:
  def __init__(self, ålder, vikt):
    self.ålder = ålder
    self.vikt = vikt

turtles = [Turtle(random.randint(0,90), random.randint(0,90)) for _ in range(0,10)]

ålder = [turtles[i].ålder for i in range(len(turtles))]
vikt = [turtles[i].vikt for i in range(len(turtles))]


#2
f = open("numbers.txt", "r")


nums = f.readline().split(",")

produkt = 1
for i in range(len(nums)):
  produkt *= int(nums[i])


#3
f = open("ägg.txt", "r")
list = []
lines = f.readlines()
for i in range(1,10):
  list.append(lines[i][2:5])

max = 0
min = 0
for i in range(0,len(list)):
  nums = float(list[i])
  list.sort()
  max = list[len(list)-1]
  min = list[0]


#5
def permutation(set):
  length = len(set)

  def faktul(n):
    if n == 1:
      return 1
    
    return n * faktul(n-1)

  print(faktul(length))


#permutation("rekursiv")
#Ordet rekrusiv kan ordnas om 20160 gånger unikt. Ordet innehåller 2 r, därför är resultatet ovan 40320/2

lista = []
original = "rekursiv"

def permutations(word, used_pos):
  if len(word) == len(original):
    if word not in lista:
      lista.append(word)
    return

  for i in range(0,len(original)):
    if i not in used_pos:
      used_pos.append(i)
      permutations(word+original[i],used_pos)
      used_pos.remove(i)

permutations("",[])
print(lista)
print(len(lista))