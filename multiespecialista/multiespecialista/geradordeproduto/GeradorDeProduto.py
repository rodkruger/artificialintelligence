
import random

class GeradorDeProduto(object):

    def __init__(self, quadro_negro):
        self.QuadroNegro = quadro_negro

    def processoForja(self):
        polygontype = ['quadrado','triangulo']
        random.shuffle(polygontype)
        size = random.randint(5, 8)
        return polygontype[0], size

    def processoUsinagem(self):
        sides = [random.randint(3, 9),random.randint(3, 9)]
        operations = random.randint(3, 9)
        return sides, operations

    def processoImpressao3D(self):
        impressiontype = ['dna','quebracabeca','lajota']
        random.shuffle(impressiontype)
        return impressiontype[0]


    def processoMontagem(self):
        ordem = ['forja','usinagem','impressao']
        random.shuffle(ordem)
        return ordem

    def verificacaoProduto(self):
        nota = random.randint(30, 100)
        return nota

    def adicionaTarefa(self):
        self.QuadroNegro.adicionaTarefa('processoForja', self.processoForja())
        self.QuadroNegro.adicionaTarefa('processoUsinagem',self.processoUsinagem())
        self.QuadroNegro.adicionaTarefa('processoImpressao3D',self.processoImpressao3D())
        self.QuadroNegro.adicionaTarefa('processoMontagem',self.processoMontagem())
        self.QuadroNegro.adicionaTarefa('verificacaoProduto',self.verificacaoProduto())
