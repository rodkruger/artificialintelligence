
import random
from multiespecialista.especialista.AbstractEspecialista import AbstractEspecialista

# estacaoImpressao3D 'é-um' AbstractEspecialista
class estacaoImpressao3D(AbstractEspecialista):

    @property
    def eh_ativado(self):
        return True if 'processoImpressao3D' in self.QuadroNegro.estadoCompartilhado['problemas'] else False

    @property
    def expertise(self):
        type = self.QuadroNegro.pegaTarefa('processoImpressao3D')
        if type == 'dna':
            return '''O---o   O---o   O---o
O---o   O---o   O---o
 O-o     O-o     O-o
  O       O       O
 o-O     o-O     o-O
o---O   o---O   o---O'''
        elif type == 'quebracabeca':
            return '''_____________________
|      (_     (_     |
|       _)     _)    |
|  _  _(  _  _(     _|
||_|_| |_| |_| |_| |_|
|      (_     (_     |
|       _)     _)    |
|______(______(______|'''
        elif type == 'lajota':
            return '''+---+---+---+---+---+
| o | o   o | o   o |
----+---+---+---+---+
| o   o | o   o | o |
----+---+---+---+---+
| o | o   o | o   o |
+---+---+---+---+---+'''
        #return ['raiz', p ,'=', (p[0] ** (1.0 / p[1]))]

    @property
    def progresso(self):
        return random.randint(12, 120)

    def contribui(self):
        self.QuadroNegro.adicionaContribuicao([[self.__class__.__name__, self.expertise]])
        self.QuadroNegro.atualizaProgresso(self.progresso)
