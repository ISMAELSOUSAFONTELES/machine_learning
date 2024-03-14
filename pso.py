from random import randint, choice





class Particula:
    def __init__(self) -> None:
        self.melhor_loc = None
        self.melhor_per = None
        self.loc_atual = None
        self.velocidade = None

    def prox_velocidade(self):
        pass

class PSO:
    def __init__(self, tam_enxame) -> None:
        self.num_interacao = None
        self.tam_enxame = tam_enxame
    
    def gerar_pos_zero(self):
        zero = [12,12,12]

        return 0

    def gerar_pos_rand(self):
        pass

    def gerar_part(self):
        zero = self.gerar_pos_zero()
        

        vel = pos - self.gerar_pos_zero()
        c1 = randint(0,2)
        c1 = randint(0,2)
    
    def gerar_enxame(self):
        enxame = []
        for i in range(self.tam_enxame):
            p = self.gerar_part()


