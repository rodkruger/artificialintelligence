
class QuadroNegro(object):

    def __init__(self):
        self.especialistas = []
        self.estadoCompartilhado = {'problemas' : ['processoForja','processoUsinagem','processoImpressao3D','processoMontagem','verificacaoProduto'],
                                    'instancias-de-problemas' : {'processoForja' : [],
                                                                 'processoUsinagem' : [],
                                                                 'processoImpressao3D' : [],
                                                                 'processoMontagem' : [],
                                                                 'verificacaoProduto' : []},
                                    'contribuicoes' : [],
                                    'progresso' : 0}

    def adicionaEspecialista(self, especialista):
        self.especialistas.append(especialista)

    def adicionaContribuicao(self, contribuicao):
        self.estadoCompartilhado['contribuicoes'] += contribuicao

    def atualizaProgresso(self, progresso):
        self.estadoCompartilhado['progresso'] += progresso

    def adicionaTarefa(self, tarefa, paramentros):
        self.estadoCompartilhado['instancias-de-problemas'][tarefa] = paramentros

    def pegaTarefa(self, tarefa):
        return self.estadoCompartilhado['instancias-de-problemas'][tarefa]

    def mostraTarefas(self):
        print('instancias-de-problemas',self.estadoCompartilhado['instancias-de-problemas'])
