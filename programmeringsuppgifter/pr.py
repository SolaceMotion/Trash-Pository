


def onetotwenty(n):
  if n > 20:
    return
  print(n)
  return onetotwenty(n+1)


def sixtytoforty(n):
  if n < 40:
    return
  
  print(n)
  return sixtytoforty(n-1)

def sum(n):
  if n == 1:
    return 1
  return n + sum(n-1)


def fakultet(n):
  if n == 1:
    return 1

  return n * fakultet(n-1)

def fibonacci(n):
  lista = []
  if n <= 1:
    return n
  return fibonacci(n-1) + fibonacci(n-2)


def inspectmatrix():
  file = open("matrix.txt", "r")

  matris = []
  lines = file.readlines() #Returnera alla rader i en lista
  print(lines)
  for y in range(len(lines)):
    row = lines[y].split()
    matris.append([]) #Lägg in listor för alla rader
    for x in range(len(row)):
      matris[y].append(int(row[x])) #Lägg in värden i listor

  positioner = []
  #Leta reda på talet 5 och spara dessosition
  for y in range(len(matris)):
    for x in range(len(matris[y])):
      if matris[y][x] == 5:
        positioner.append((y+1,x+1))

  print(positioner)


def pokemon():
  file = open("pokemon.csv")
  lines = file.readlines()
  lista = []
  categories = lines[0].strip().split(",")

  for i in range(len(lines)):
    row = lines[i].strip().split(",") #Har inte än tagit bort första raden
    lista.append({}) #Lägg in objekt för varje rad
    
    for j in range(len(row)):
      lista[i][categories[j]] = row[j] if not row[j].isnumeric() else int(row[j]) 

  #har inte sorterat ännu
  
pokemon()

