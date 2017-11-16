
class FSMHitRatioFitness():

    def __init__(self, dp):
        self.learning_data = dp.learning_data
        self.alphabet_size = dp.alphabet_size


    def evalFSM(self, chromosome):

        fsm = chromosome.fsm
        correct = 0
        empty_wrong = False

        # loop through each learning example
        for key in self.learning_data:
            # break the string into a char array
            example = key.split(' ')

            row = 0

            # if we dont get the empty string correct, give chromosome
            # a fitness of zero to breed it out quickly
            if example[0] == '':
                if(0 in chromosome.final_states
                    and int(self.learning_data[key]) == 0):
                        return 0
                else: correct+=1

            else:
                # go through the FSM
                for element in example: row = fsm[row][int(element)]

                # if you end on a final state and you should have, you got one correct
                if (row in chromosome.final_states
                    and int(self.learning_data[key]) == 1): correct+=1

                # if you did not end a final state, and you should not have, you got one correct
                elif(row not in chromosome.final_states
                    and int(self.learning_data[key]) == 0): correct+=1

        # the fitness is percentage of examples the FSM got correct
        return float(correct)/len(self.learning_data)

    def setFitness(self, genotype):
        for chromosome in genotype.chromosomes:
            chromosome.fitness = self.evalFSM(chromosome)


    def start(self, genotype):
        self.setFitness(genotype)
