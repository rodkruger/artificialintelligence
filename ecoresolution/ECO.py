from enum import Enum


# Defines the states a block can be during the execution
class State(Enum):
    SEEK_SATISFACTION = 1
    SATISFIED = 2
    SEEK_ESCAPE = 3
    ESCAPE = 4
    ATTACK = 5


# Defines a objective that can be reached during the execution
class Tower:
    id = None
    blocks = None

    def __init__(self, id, blocks=None):
        self.id = id
        self.blocks = blocks

        for block, i in zip(blocks, range(len(blocks))):
            block.actual = i


# Defines a block that could be moved during the execution
class Block:
    id = None

    restriction = None
    agression = None
    state = None

    actual = None
    objective = None

    def __init__(self, id, objective):
        self.id = id
        self.objective = objective

    pass


def eco_resolution(blocks, objectives):
    # Para cada bloco, faça:
    # Se satisfeito, nada
    # Se não satisfeito, tentar satisfazer
    # Se há impedimento na satisfação, agredir
    # Se agredido, buscar lugar para fundir diferente do objetivo do agressor
    # Se há impedimento na fuga, agredir
    pass


# Faça imprimir no console antes de tudo !

b1 = Block("A", (3, "T3"))
b2 = Block("B", (1, "T3"))
b3 = Block("C", (2, "T3"))

blocks = [b1, b2, b3]

t1 = Tower("T1")
t2 = Tower("T2", blocks)
t3 = Tower("T3")
