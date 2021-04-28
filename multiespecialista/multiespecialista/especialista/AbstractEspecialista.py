
import abc

# operacões que os todos especialistas devem implementar.
class AbstractEspecialista(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, quadro_negro):
        self.QuadroNegro = quadro_negro

    @property
    def eh_ativado(self):
        raise NotImplementedError('Deve fornecer implementação na subclasse.')

    @property
    def expertise(self):
        raise NotImplementedError('Deve fornecer implementação na subclasse.')

    @property
    def progresso(self):
        raise NotImplementedError('Deve fornecer implementação na subclasse.')

    @abc.abstractmethod
    def contribui(self):
        raise NotImplementedError('Deve fornecer implementação na subclasse.')
