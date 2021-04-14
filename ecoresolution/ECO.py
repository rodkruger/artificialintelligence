"""
ECO.py:
    ECO-resolution algorithm explained, using moving blocks example
"""

__author__ = "Rodrigo Krüger / Vitor Shimada"
__copyright__ = "Copyright 2021, PPGIA"
__credits__ = ["Rodrigo Krüger, Vitor Shimada"]
__version__ = "1.0.0"
__maintainer__ = "Rodrigo Krüger/Vitor Shimada - PPGIA"
__email__ = "rodrigo.kruger.eng@gmail.com"

from enum import Enum


# Defines the states a block can be during the execution
class State(Enum):
    SEEK_SATISFACTION = 1
    SATISFIED = 2
    SEEK_ESCAPE = 3
    ESCAPE = 4
    ATTACK = 5


# Defines objectives that can be reached during the execution. In this example,
# we are modelling Towers as the objective for each block, but it could be adapted to
# any situation
class Tower:

    def __init__(self, id, blocks):
        self.id = id            # Objective Identifier
        self.blocks = blocks    # Blocks presents in each tower

        for block, i in zip(blocks, range(len(blocks))):
            block.tower = self

    def add_block(self, current_block):
        self.blocks.append(current_block)

    def remove_block(self):
        self.blocks.pop()


# Defines a block that could be moved during the execution. We can understad that each block
# actually is an intelligent agent looking for objectives
class Block:

    def __init__(self, id, objective):
        self.id = id                                # Block Identifier
        self.objective = objective                  # Target objective
        self.tower = None                           # Actual tower
        self.bottom = None                          # Block immediately below
        self.top = None                             # Block immediatley above
        self.states = [State.SEEK_SATISFACTION]     # States that each block will pass through the execution
        self.agression = None                       # Which block triggerred an agression
        self.restrictions = []                      # Restrictions that needed to be ensured during the execution

    def add_state(self, state):

        last_state = self.states[-1]
        if last_state != state:
            self.states.append(state)

    def add_restriction(self, block_id):
        self.restrictions.append(block_id)

    def clear_restrictions(self):
        self.restrictions = []
        self.agression = None


def is_satisfied(current_block):
    """
    Checks if a Block is satisfied or not. As a block will handle multiple states during the execution, the latest state
    will be the one which is on top of the list
    :param current_block:
        The block to have the state checked
    :return:
        True - if the latest state is State.SATISFIED
        False - if any
    """
    return current_block.states[-1] == State.SATISFIED


def put_on_empty_tower(current_block, tower):
    """
    Put the block on top of an empty tower

    :param current_block:
        The block to be placed
    :param tower:
        New tower
    :return:
    """

    # If the current block does not have any block below him, we don't need to adjust the pointers
    if current_block.bottom:
        current_block.bottom.top = None

    # Adjust the pointers of the block, that will remain with any block below and above it
    current_block.bottom = None
    current_block.top = None

    # Remove the block from the current tower, and adjust for the new tower
    current_block.tower.remove_block()
    tower.add_block(current_block)
    current_block.tower = tower


def put_on_top_of_block(current_block, new_block, tower):
    """
    Put the block on top of a new block

    :param current_block:
        The block to be placed on top
    :param new_block:
        The block to receive a new block
    :param tower:
        New tower
    :return:
    """

    # If the current block does not have any block below him, we don't need to adjust the pointers
    if current_block.bottom:
        current_block.bottom.top = current_block

    # Adjust the pointers of the block, that will point for the block it will be placed
    current_block.bottom = new_block
    new_block.top = current_block

    # Remove the block from the current tower, and adjust for the new tower
    current_block.tower.remove_block()
    tower.add_block(current_block)
    current_block.tower = tower


def do_agression(current_block, towers):
    """
    During the ECO-resolution algorithm, a block will be assaulted if there is a block for its movements. Then, a
    message for the block that is blocking the movement is sent, and a new try to satisfy this block is raised

    :param current_block:
        The block that has a block for the movement
    :param towers:
        The towers (or objectives) we have mapped in the problem
    :return:
        True - if the agression were solved
        False - if it is impossible to solve the agression
    """
    top = current_block.top
    top.agression = current_block
    top.add_restriction(current_block.objective)

    if try_satisfy(top, towers):
        top.clear_restrictions()
        return True
    else:
        return False


def do_satisfy(current_block, towers):
    """
    During the ECO-resolution algorithm, we satisfy a block movement by placing the block on top of the objective, or,
    if we move the block for another place that can release more blocks to be moved

    :param current_block:
        The block to be satisfied
    :param towers:
        The towers (or objectives) we have mapped in the problem
    :return:
    """

    # For each tower, try to place the block on top of the objective or in a new place to release more blocks
    for tower in towers:

        # In case we find an empty tower, we can test if it is the objective for the block. If so, we just make
        # the movement !
        if len(tower.blocks) == 0:

            # Objective found ! Do the movement and satisfy the block !
            if current_block.objective == tower.id:

                # Put on empty tower !
                put_on_empty_tower(current_block, tower)

                # Satisfy the block
                if current_block.agression:
                    current_block.add_state(State.ESCAPE)

                current_block.add_state(State.SATISFIED)

                return True
        else:
            # In case we have the block to be placed above a block, we need to test if it is the objective

            # Read the block immediately on top of the current tower
            l_block = tower.blocks[-1]

            # Just ignore if we are testing the current block
            if l_block.id != current_block.id:

                # Verify if we found the objective. If so, move it and satisfy !
                if current_block.objective == l_block.id:

                    # Put on top of a new block
                    put_on_top_of_block(current_block, l_block, tower)

                    # Satisfy the block
                    if current_block.agression:
                        current_block.add_state(State.ESCAPE)

                    current_block.add_state(State.SATISFIED)

                    return True

    # Impossible to satisfy ! Make a mandatory movement (make_movement) !
    return False


def make_movement(current_block, towers):
    """
    During ECO-resolution algorithm, if we can't satisfy an objective even not having any blockings, we need to
    make a mandatory movement, in order to release more blocks to be moved

    :param current_block:
        The block to be satisfied
    :param towers:
        The towers (or objectives) we have mapped in the problem
    :return:
    """

    # For each tower, try to place the block on top of the objective or in a new place to release more blocks
    for tower in towers:

        if len(tower.blocks) == 0:

            # If there is no restrictions, move it !
            if tower.id not in current_block.restrictions:

                # Put on empty tower ! No satisfaction !
                put_on_empty_tower(current_block, tower)

                # Change the state to ESCAPE
                if current_block.agression:
                    current_block.add_state(State.ESCAPE)

                return True
        else:
            # In case we have the block to be placed above a block, we need to test if it is the objective

            # Read the block immediately on top of the current tower
            l_block = tower.blocks[-1]

            # Just ignore if we are testing the current block
            if l_block.id != current_block.id:

                # If there is no restrictions, move it !
                if l_block.id not in current_block.restrictions:
                    current_block.tower = tower

                    # Put on top of a new block ! No satisfaction !
                    put_on_top_of_block(current_block, l_block, tower)

                    # Change the state to ESCAPE
                    if current_block.agression:
                        current_block.add_state(State.ESCAPE)

                    return True

    # Fatal Error ! God Help me !
    return False


def try_satisfy(current_block, towers):
    """
    Try to satisfy the objectives of the blocks. If there is blocks, assault them !
    :param current_block:
        The block to be satisfied
    :param towers:
        The towers (or objectives) we have mapped in the problem
    :return:
    """

    if not current_block.agression:
        current_block.add_state(State.SEEK_SATISFACTION)
    else:
        current_block.add_state(State.SEEK_ESCAPE)

    # Check if there is blockings in the way. If there is, assault the block that is blocking the movement !
    if not current_block.top:

        # If we can't satisfy the objective, we will do a mandatory movement, in order to release new places
        if not do_satisfy(current_block, towers):
            return make_movement(current_block, towers)

    else:
        # There is blocks. Assault the block immediatelly above !
        return do_agression(current_block, towers)


def eco_resolution(blocks, towers):
    """
    ECO-resolution algorithm. Main point
    :param blocks:
        The blocks we have mapped in the problem
    :param towers:
        The towers (or objectives) we have mapped in the problem
    :return:
    """
    num_satisfied = len(blocks)

    # While we do not satisfy all the blocks, repeat the satisfaction for all of them in a circular way
    while num_satisfied > 0:

        # For each block in the problem, try to satisfy !
        for block in blocks:

            # Print the towers and blocks
            print_towers(towers)

            # If it is already satisfied, continue and get the next block !
            if is_satisfied(block):
                num_satisfied -= 1
            else:
                # If it is not satisfied, try to satisfy and assaulted them if necessary
                try_satisfy(block, towers)


def print_towers(towers):

    print("\n---------------------------------------------------------------------------------------")

    for tower in towers:

        print(f"\n{tower.id}: ", end='')

        for block in tower.blocks:
            print(f"{block.id} - Restri.: {block.restrictions}", end='')
            print(' - Estados [', end="")

            for state in block.states:
                if state == State.SEEK_SATISFACTION:
                    print("'BS'", end="")
                elif state == State.SATISFIED:
                    print("'S'", end="")
                elif state == State.SEEK_ESCAPE:
                    print("'BF'", end="")
                elif state == State.ESCAPE:
                    print("'F'", end="")
                elif state == State.ATTACK:
                    print("'A'", end="")

                print(",", end="")

            print("] ### ", end='')

    print("\n")

#######################################################################################################################
# MAIN PROGRAM
#######################################################################################################################

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