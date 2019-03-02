import random
class Strategy:

    def __init__(self, select = 'best1bin', ppoints = None):
        strategy = {
            'rand1bin': self.rand1bin,
            'best1bin': self.best1bin,
            # 'best2bin': self.best2bin,
            # 'rand2bin': self.rand2bin,
            # 'randbest1bin': self.randbest1bin,
            # 'rand1exp' : self.rand1exp,
            # 'best1exp' : self.best1exp,
            # 'best2exp' : self.best2exp,
            # 'rand2exp' : self.rand2exp,
            # 'randbest1exp' : self.randbest2exp
        }

        self.strategy = strategy[select]
        self.best = max(ppoints)

    def rand1bin(self,x, y, a, b, c, CR,F):
        R = random.random() * x.dim
        for iy in range(x.dim):
            ri = random.random()

            if ri < CR or iy == R:
                
                y.coords[iy] = a.coords[iy] + F * (b.coords[iy] - c.coords[iy])

    def best1bin(self,x, y, a, b, c, CR,F, ppoints = None):
        R = random.random() * x.dim
        for iy in range(x.dim):
            ri = random.random()

            if ri < CR or iy == R:
                
                y.coords[iy] = self.best + F * (b.coords[iy] - c.coords[iy])

