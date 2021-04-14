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

    def __init__(self, id, blocks):
        self.id = id
        self.blocks = blocks

        for block, i in zip(blocks, range(len(blocks))):
            block.tower = self

    def add_block(self, current_block):
        self.blocks.append(current_block)

    def remove_block(self):
        self.blocks.pop()


# Defines a block that could be moved during the execution
class Block:

    def __init__(self, id, objective):
        self.id = id
        self.objective = objective
        self.restriction = []
        self.tower = None
        self.bottom = None
        self.top = None
        self.states = [State.SEEK_SATISFACTION]
        self.agression = False
        self.restrictions = []

    def add_state(self, state):
        self.states.append(state)

    def add_restriction(self, block_id):
        self.restrictions.append(block_id)

    def clear_restrictions(self):
        self.restrictions = []


def is_satisfied(current_block):
    return current_block.states[-1] == State.SATISFIED


def do_agression(current_block, towers):
    top = current_block.top
    top.agression = current_block
    top.add_state(State.SEEK_ESCAPE)
    top.add_restriction(current_block.objective)

    return do_satisfy(top, towers)


def try_satisfy(current_block, towers):
    # Para cada torre, verificar se é possível satisfazer o objetivo
    for tower in towers:

        if len(tower.blocks) == 0:

            # Objetivo encontrado ! Movimentar !
            if current_block.objective == tower.id:
                if current_block.bottom:
                    current_block.bottom.top = None

                current_block.bottom = None
                current_block.top = None
                current_block.tower.remove_block()
                tower.add_block(current_block)
                current_block.tower = tower
                current_block.add_state(State.SATISFIED)
                return True
        else:
            # Obter o bloco atualmente posicionado no topo da torre
            l_block = tower.blocks[-1]

            # Ignorar a rodada que testa o próprio bloco !
            if l_block.id != current_block.id:

                # Objetivo encontrado ! Movimentar !
                if current_block.objective == l_block.id:
                    if current_block.bottom:
                        current_block.bottom.top = current_block

                    current_block.bottom = l_block
                    l_block.top = current_block
                    current_block.tower.remove_block()
                    tower.add_block(current_block)
                    current_block.tower = tower
                    current_block.add_state(State.SATISFIED)
                    return True

    # Não foi possível satisfazer !
    return False


def make_movement(current_block, towers):
    # Para cada torre, movimentar o bloco sobre uma posição que não haja restrições
    for tower in towers:

        if len(tower.blocks) == 0:

            # Não há restrições ! Movimentar !
            if tower.id not in current_block.restrictions:
                if current_block.bottom:
                    current_block.bottom.top = None

                current_block.bottom = None
                current_block.top = None
                current_block.tower.remove_block()
                tower.add_block(current_block)
                current_block.tower = tower

                return True
        else:
            # Obter o bloco atualmente posicionado no topo da torre
            l_block = tower.blocks[-1]

            # Ignorar a rodada que testa o próprio bloco !
            if l_block.id != current_block.id:

                #  Não há restrições ! Movimentar !
                if l_block.id not in current_block.restrictions:
                    current_block.tower = tower

                    if current_block.bottom:
                        current_block.bottom.top = current_block

                    current_block.bottom = l_block
                    l_block.top = current_block
                    current_block.tower.remove_block()
                    tower.add_block(current_block)
                    current_block.tower = tower

                    return True


def do_satisfy(current_block, towers):
    # Verifica se o caminho está livre para movimentação
    if not current_block.top:

        satisfied = try_satisfy(current_block, towers)

        if not satisfied:
            make_movement(current_block, towers)

    else:
        # Não é possível satisfazer. Há impedimentos. Agredir !!
        return do_agression(current_block, towers)


def eco_resolution(blocks, towers):
    finalizado = False

    while not finalizado:

        index = 0  # Ponteiro do bloco atualmente sendo processado

        # Para cada bloco, faça
        while index < len(blocks):

            block = blocks[index]

            # Se satisfeito, nada
            if is_satisfied(block):
                continue

            # Se não satisfeito, tentar satisfazer
            do_satisfy(block, towers)

            print_towers(towers)

            index += 1


def print_towers(towers):
    for tower in towers:

        print(f"Torre {tower.id}: ", end='')

        for block in tower.blocks:
            print(f"{block.id} {block.restrictions} - {block.states} # ", end='')

        print("")


# Faça imprimir no console antes de tudo !

a = Block("A", "C")
b = Block("B", "T3")
c = Block("C", "B")

a.bottom = None; a.top = b
b.bottom = a; b.top = c
c.bottom = b; c.top = None

t1 = Tower("T1", [])
t2 = Tower("T2", [a, b, c])
t3 = Tower("T3", [])

towers = [t1, t2, t3]

eco_resolution([a, b, c], towers)
