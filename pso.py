from random import uniform
import numpy as np
from icecream import ic


class Particula:
    def __init__(self, pos, vel, per, c1, c2 ) -> None:
        self.melhor_pos = np.array([0,0,0])
        self.melhor_per = 0
        self.pos = np.array(pos)
        self.vel = np.array(vel)
        self.per = per
        self.c1 = float(c1)
        self.c2 = float(c2)

    def prox_velocidade(self, melhor_pos_g):
        
        c1 = self.c1
        c2 = self.c2
        inercia = self.vel
        c_comp = c1*(self.melhor_pos - self.pos)
        s_comp = c2*(melhor_pos_g - self.pos)
        prox_vel = inercia + c_comp + s_comp
        prox_vel[1] = round(prox_vel[1])
        prox_vel[2] = round(prox_vel[2])
        prox_vel[0] = round(prox_vel[0])
        return prox_vel


class PSO:
    def __init__(self, tam_enxame, num_interacao) -> None:
        
        self.tam_enxame = tam_enxame
        self.num_interacao = int(num_interacao)
        self.melhor_pos_geral = np.array([0,0,0])
        self.melhor_per_geral = 0
    
    def gerar_pos_zero(self):
        zero = np.array([12,12,12])

        return zero

    def gerar_pos_rand(self):
        a = round(uniform(0,25))
        b = round(uniform(0,25))
        c = round(uniform(0,25))

        pos = np.array([a, b, c])
        return pos

    def performace(self, pos):
        return sum(list(pos))/75

    def gerar_part(self):
        zero = self.gerar_pos_zero()
        pos = self.gerar_pos_rand()
        vel = pos - zero
        c1 = uniform(0,2)
        c2 = uniform(0,2)
        per = self.performace(pos)
        p = Particula(pos, vel,per,c1, c2)
        p.melhor_pos = pos
        p.melhor_per = per
        return p
    
    
    
    def gerar_enxame(self):
        enxame = []
        for _ in range(self.tam_enxame):
            p = self.gerar_part()
            if self.performace(p.pos) > p.melhor_per:
                p.melhor_per = self.performace(p.pos)
                p.melhor_pos = np.array(list(p.pos))
            if p.per > self.melhor_per_geral:
                self.melhor_pos_geral = np.array(list(p.melhor_pos))
                self.melhor_per_geral = p.per
            enxame.append(p)
        return enxame
    
    def andar(self, particula):
        p = particula
        pos = p.pos
        prox_vel = p.prox_velocidade(self.melhor_pos_geral)
        nova_pos = pos + prox_vel
        return nova_pos
    
    def executar(self):
        enxame = self.gerar_enxame()
        
        for i in range(self.tam_enxame):
            p = enxame[i]
            if p.per > p.melhor_per:
                p.melhor_per = p.per
                p.melhor_pos = np.array(list(p.pos))
            if p.per > self.melhor_per_geral:
                self.melhor_pos_geral = np.array(list(p.melhor_pos))
                self.melhor_per_geral = p.per
            enxame[i] = p
            print(str(enxame[i].pos) + " " + "vel:" + str(enxame[i].vel))
        print("\n\n")
        
        for _ in range(self.num_interacao):
            for i in range(self.tam_enxame):
                p = enxame[i]
                p0 = p.pos
                p.pos = self.andar(p)
                p.vel = p.pos - p0
                if p.per > p.melhor_per:
                    p.melhor_per = p.per
                    p.melhor_pos = np.array(list(p.pos))
                if p.melhor_per > self.melhor_per_geral:
                    self.melhor_pos_geral = p.melhor_pos
                    self.melhor_per_geral = p.melhor_per
                
                enxame[i] = p
                print(str(enxame[i].pos) + " " + "vel:" + str(enxame[i].vel))
            print("\n\n")
        print(self.melhor_per_geral)      

        
        
if __name__ == '__main__':

    pso = PSO(10,10)
    pso.executar()



