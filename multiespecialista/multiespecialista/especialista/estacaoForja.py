
import random
from multiespecialista.especialista.AbstractEspecialista import AbstractEspecialista

# estacaoForja 'é-um' AbstractEspecialista
class estacaoForja(AbstractEspecialista):

    # Testa se a especialidade do 'estacaoForja' está presente na lista de problemas a serem resolvidos
    @property
    def eh_ativado(self):
        if 'processoForja' in self.QuadroNegro.estadoCompartilhado['problemas']:
            return True
        else:
            return False

    # implementação da expertise do 'estacaoForja'; como ele realiza sua tarefa
    @property
    def expertise(self):
        polygontype, size = self.QuadroNegro.pegaTarefa('processoForja')
        element = 'f '
        lista = []
        if polygontype == 'triangulo':
            for i in range(1,size+1):
                lista.append(element*i)
            lista = '\n'.join(lista)
        if polygontype == 'quadrado':
            lista = (size * 'f ' + '\n') * size
        return lista
        #return ['processoForja', p , '=', (p[0]+p[1])]

    # Quanto a realização da tarefa so estacaoForja contribui com o avanço geral da solução do problema.
    @property
    def progresso(self):
        return random.randint(1, 5)

    # Atualiza o quadro-negro com a contribuição do 'estacaoForja'
    def contribui(self):
        self.QuadroNegro.adicionaContribuicao([[self.__class__.__name__, self.expertise]])
        self.QuadroNegro.atualizaProgresso(self.progresso)
