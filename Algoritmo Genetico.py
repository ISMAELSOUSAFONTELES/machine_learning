from random import randint, choice

class Algoritimo_genetico:
    def __init__(self,num_ind, num_gen, chance_m):
        self.num_ind = num_ind
        self.num_gen = num_gen
        self.chance_m = chance_m
        self.melhor_ind = None
        self.atributo = [5,10,15,20,25]

    def gerar_ind(self):
        individuo = []
        for i in range(len(self.atributo)):
            individuo.append = randint(1,self.atributo[i])
        return individuo
    
    def gerar_pop(self):
        populacao = []
        for i in range(self.num_ind):
            populacao.append(self.gerar_ind())
        return populacao
    def fitness(self, individuo):
        soma = 0
        for i in range(len(self.atributo)):
            soma += individuo[i]
        return soma
    def selecao(self, populacao):
        selecaoH = [choice(populacao), choice(populacao)]
        selecaoM = [choice(populacao), choice(populacao)]

        pai = []
        if self.fitness(selecaoH[0]) > self.fitness(selecaoH[1]):
            pai = selecaoH[0]
        else:
            pai = selecaoH[1]
        
        mae = []
        if self.fitness(selecaoM[0]) > self.fitness(selecaoM[1]):
            mae = selecaoM[0]
        else:
            mae = selecaoM[1]

        return pai, mae



        
ag = Algoritimo_genetico(10, 10, 10)
