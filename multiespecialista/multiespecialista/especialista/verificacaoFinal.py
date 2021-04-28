
import random
from multiespecialista.especialista.AbstractEspecialista import AbstractEspecialista

### verificacaoFinal 'é-um' AbstractEspecialista
class verificacaoFinal(AbstractEspecialista):

    @property
    def eh_ativado(self):
        if 'verificacaoProduto' in self.QuadroNegro.estadoCompartilhado['problemas']:
            return True
        else:
            return False

    @property
    def expertise(self):
        return str(self.QuadroNegro.pegaTarefa('verificacaoProduto')) + ' pontos'

    @property
    def progresso(self):
        return random.randint(10, 30)

    def contribui(self):
        self.QuadroNegro.adicionaContribuicao([[self.__class__.__name__, self.expertise]])
        self.QuadroNegro.atualizaProgresso(self.progresso)