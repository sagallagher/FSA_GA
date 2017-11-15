from random import randint

class Chromosome():

    def __init__(self, fsm, final_states):
        self.fsm = fsm
        self.final_states = final_states
        self.fitness = 0

    def __str__(self):
        final_states =' '
        for state in self.final_states: final_states += (' ' + str(state))
        result = 'Fitness:\t' + str(self.fitness) + '\n' + 'Final States:\t' + final_states + '\n'
        for row in self.fsm:
            for element in row:
                result += ('%12s' % str(element))
            result += '\n'

        return result
