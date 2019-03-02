import random
class Strategy:

    def __init__(self, select = 'best2bin', ppoints = None, cost = None):
        strategy = {
            'rand1bin': self.rand1bin,
            'best1bin': self.best1bin,
            'best2bin': self.best2bin,
            'rand2bin': self.rand2bin,
            # 'randbest1bin': self.randbest1bin,
            # 'rand1exp' : self.rand1exp,
            # 'best1exp' : self.best1exp,
            # 'best2exp' : self.best2exp,
            # 'rand2exp' : self.rand2exp,
            # 'randbest1exp' : self.randbest2exp
        }

        self.strategy = strategy[select]
        self.points = ppoints
        self.indexbest = cost.index(min(cost))

    def rand1bin(self,x, y, x1, CR,F):
        [a,b,c,d,e] = ['a','b','c','d','e']
        R = random.random() * x.dim
        for iy in range(x.dim):
            ri = random.random()

            if ri < CR or iy == R:
                
                y.coords[iy] = x1[c].coords[iy] + F * (x1[a].coords[iy] - x1[b].coords[iy])

    def best1bin(self,x, y, x1, CR,F, ppoints = None):
        [a,b,c,d,e] = ['a','b','c','d','e']
        R = random.random() * x.dim
        for iy in range(x.dim):
            ri = random.random()

            if ri < CR or iy == R:
                
                y.coords[iy] = self.points[self.indexbest].coords[iy] + F * (x1[a].coords[iy] - x1[b].coords[iy])
    
    def best2bin(self,x, y, x1 , CR,F, ppoints = None):
        [a,b,c,d,e] = ['a','b','c','d','e']
        R = random.random() * x.dim
        for iy in range(x.dim):
            ri = random.random()

            if ri < CR or iy == R:
                
                y.coords[iy] = self.points[self.indexbest].coords[iy] + F * (x1[a].coords[iy] + x1[b].coords[iy] - x1[c].coords[iy] - x1[d].coords[iy])
    
    def rand2bin(self,x, y, x1 , CR,F):
        [a,b,c,d,e] = ['a','b','c','d','e']
        R = random.random() * x.dim
        for iy in range(x.dim):
            ri = random.random()

            if ri < CR or iy == R:
                
                y.coords[iy] = x1[e].coords[iy] + F * (x[a].coords[iy] + x1[b].coords[iy] - x1[c].coords[iy] -  x1[d].coords[iy]  )
    
    # def randbest1bin(self,x, y, x1 , CR,F):
    #     [a,b,c,d,e] = ['a','b','c','d','e']
    #     R = random.random() * x.dim
    #     for iy in range(x.dim):
    #         ri = random.random()

    #         if ri < CR or iy == R:
                
    #             y.coords[iy] = y.coords[iy] + F * (x[a].coords[iy] + x1[b].coords[iy] - x1[c].coords[iy] -  x1[d].coords[iy]  )
    
    # def rand1exp(self,x, y, x1 , CR,F):
    #     [a,b,c,d,e] = ['a','b','c','d','e']
    #     R = random.random() * x.dim
    #     for iy in range(x.dim):
    #         ri = random.random()

    #         if ri < CR or iy == R:
                
    #             y.coords[iy] = x1[e].coords[iy] + F * (x[a].coords[iy] + x1[b].coords[iy] - x1[c].coords[iy] -  x1[d].coords[iy]  )
    