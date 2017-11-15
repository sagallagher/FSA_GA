from random import randint
from Chromosome import *
from Genotype import *

class InitializePopulation():

    # constructor
    def __init__(self, data_parser, population_size, min_states, max_states):
        self.alphabet_size = data_parser.alphabet_size
        self.learning_data = data_parser.learning_data

        self.min_states = min_states
        self.max_states = max_states
        self.population_size = population_size

    # string representation of initial population is the genotype
    def __str__(self): return str(self.genotype)

    # return the randomly generated genotype
    def getGenotype(self): return self.genotype

    # generate a random finite state machine
    def generateRandomFSM(self, min_states, max_states):

        '''
        BUG: currently generates NFSA. Might be easier if only generate DFSA
        '''

        number_of_states = randint(min_states, max_states)
        fsm = []
        for number_state in xrange(number_of_states):
            state = []
            for transition in xrange(self.alphabet_size):
                state.append(randint(0,number_of_states-1))

            fsm.append(state)
        return fsm

    # choose random states to be final given a FSM
    def generateRandomFinalStates(self, fsm):
        final_states = []
        number_of_final_states = randint(1,len(fsm))
        for state in xrange(number_of_final_states):
            random_final_state = randint(0,len(fsm)-1)
            if random_final_state not in final_states:
                final_states.append(random_final_state)
        return final_states

    # fill genotype with desired population size
    def fillGenotype(self, genotype):

        for i in xrange(self.population_size):
            fsm = self.generateRandomFSM(self.min_states, self.max_states)
            final_states = self.generateRandomFinalStates(fsm)
            genotype.pushChromosome(Chromosome(fsm, final_states))

    def start(self, genotype):
        self.fillGenotype(genotype)
