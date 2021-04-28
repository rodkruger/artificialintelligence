
import random
from multiespecialista.especialista.AbstractEspecialista import AbstractEspecialista

# estacaoMontagem 'é-um' AbstractEspecialista
class estacaoMontagem(AbstractEspecialista):

    @property
    def eh_ativado(self):
        if 'processoMontagem' in self.QuadroNegro.estadoCompartilhado['problemas']:
            return True
        else:
            return False

    @property
    def expertise(self):
        return self.QuadroNegro.pegaTarefa('processoMontagem')

    @property
    def progresso(self):
        return random.randint(10, 30)

    def contribui(self):
        self.QuadroNegro.adicionaContribuicao([[self.__class__.__name__, self.expertise]])
        self.QuadroNegro.atualizaProgresso(self.progresso)