from math import sqrt
import random

#create a 2D-list
def create_generation(gene_size, nr_of_genes, generation_size):
  gen = []
  for i in range(generation_size):
      temp2 = []
      for j in range(gene_size):
        temp2.append(random.randint(0,nr_of_genes-1))
      gen.append(temp2)
    
  return gen


#given a generation, take the DNA and calculate a position from the below conditions
def get_mouse_position(lista):
  arr = []
  for i in range(0,len(lista)):
    pos = [0,0]
    for j in range(0,len(lista[i])):

      if lista[i][j] == 0:
        pass

      if lista[i][j] == 1:
        pos[0]+=1
      if lista[i][j] == 2:
        pos[1]+=1
      if lista[i][j] == 3:
        pos[0]-=1
      if lista[i][j] == 4:
        pos[1]-=1
        
    arr.append(tuple(pos))  
    
  return arr

test = [[3,0,1,0,0,3,1,2],
        [0,0,1,1,1,1,4,4],
        [0,4,1,4,2,3,0,4],
        [3,1,1,3,3,2,4,4]]


def fitness(mouse_positions, goal):
  arr = []
  for i in range(0,len(mouse_positions)):
    for j in range(0, len(mouse_positions[i])):
      #y                                                #x
      hypotenuse = pow((goal[1] - mouse_positions[i][1]), 2) + pow((goal[0] - mouse_positions[i][0]), 2)
      distance = hypotenuse**0.5
    arr.append(distance)
  return arr


def crossover(generation):
  newgen = []
  for i in range(0, int(len(generation)/2)):
    splicing_point = random.randint(0,len(generation))

    parent1 = generation[i*2]
    parent2 = generation[i*2+1]

    p1gene_start = parent1[:splicing_point]
    p1gene_end = parent1[splicing_point:]

    p2gene_start = parent2[:splicing_point]
    p2gene_end = parent2[splicing_point:]

    child1 = p1gene_start + p2gene_end
    child2 = p2gene_start + p1gene_end

    newgen.append(child1)
    newgen.append(child2)

crossover(test)


def mutate(lista,rate,nr_of_genes):
  mutated = lista
  for i in range(len(lista)):
    for j in range(len(lista[i])):
      if random.randint(0,rate) == 0:
        mutated[i][j] = random.randint(0, nr_of_genes)
  return mutated

generation = create_generation(8,5,4)

#Välj ut de möss som har presterat bäst
def selection(möss, goal):
  genes = []

  for i in range(0,len(möss)):
    sp0 = möss[random.randint(0,len(möss) -1)]
    sp1 = möss[random.randint(0,len(möss) -1)]
    mouse = get_mouse_position([sp0,sp1])

    fitness_möss = fitness(mouse, goal)

    if fitness_möss[0] < fitness_möss[1]:
      genes.append(sp0)
    else:
      genes.append(sp1)

  return genes

