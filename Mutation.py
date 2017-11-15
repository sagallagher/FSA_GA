from random import randint
class Mutation():

    def __init__(self, dp):

        self.alphabet_size = dp.alphabet_size


    def mutateGenotype(self, genotype):

        for chromosome in genotype.chromosomes:
            if len(chromosome.fsm) == 0: break
            number_of_states = len(chromosome.fsm)

            # choose a random row
            random_row = randint(0,number_of_states-1)

            # choose a random column
            random_col = randint(0, self.alphabet_size-1)

            # choose a random number to replace a random element with
            random_transition = randint(0,number_of_states-1)

            # write the random number to the random position
            chromosome.fsm[random_row][random_col] = random_transition

    def start(self, genotype):
        self.mutateGenotype(genotype)
