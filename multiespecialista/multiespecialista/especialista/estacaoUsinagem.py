
import random
from multiespecialista.especialista.AbstractEspecialista import AbstractEspecialista

# estacaoUsinagem 'é-um' AbstractEspecialista
class estacaoUsinagem(AbstractEspecialista):

    @property
    def eh_ativado(self):
        if 'processoUsinagem' in self.QuadroNegro.estadoCompartilhado['problemas']:
            return True
        else:
            return False

    @property
    def expertise(self):
        sides, operation = self.QuadroNegro.pegaTarefa('processoUsinagem')
        string = (sides[0] * 'u' * 2 + '\n') * sides[1]
        #print(string)
        for i in range(operation):
            position = random.randint(0,int(sides[0]*sides[1]/2))
            new_character = ' '
            if string[position-1]=='\n':
                position = position -2            
            if position == 0:
                string = new_character + string[position+1:]
            elif position == sides[0]*sides[1]-1:
                string = string[:position] + new_character
            else:
                string = string[:position] + new_character + string[position+1:]
        return string

    @property
    def progresso(self):
        return random.randint(10, 30)

    def contribui(self):
        self.QuadroNegro.adicionaContribuicao([[self.__class__.__name__, self.expertise]])
        self.QuadroNegro.atualizaProgresso(self.progresso)

