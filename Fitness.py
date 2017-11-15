class Fitness():

    def __init__(self, genotype, learning_data, alphabet_size):
        self.genotype = genotype
        self.learning_data = learning_data
        self.alphabet_size = alphabet_size
        self.setFitness()

    def __str__(self):
        result = ''
        for chromosome in self.chromosomes: result += ('-'*50+'\n' + str(chromosome))
        return result

    def evalFSM(self, chromosome):

        fsm = chromosome.fsm
        correct = 0

        # loop through each learning example
        for key in self.learning_data:

            # break the string into a char array
            example = []
            for character in key:
                example.append(int(character))

            row = 1

            '''
            BUG: fsm[][] sometimes goes out of bounds
            '''
            # go through the FSM

            for element in example:

                try: row = fsm[row-1][element]
                except: print "AHHH",row,element, len(fsm)
            # if you end on a final state and you should have, you got one correct
            if (row in chromosome.final_states
                and int(self.learning_data[key]) == 1): correct+=1

            # if you did not end a final state, and you should not have, you got one correct
            elif(row not in chromosome.final_states
                and int(self.learning_data[key]) == 0): correct+=1

        # the fitness is percentage of examples the FSM got correct
        return float(correct)/len(self.learning_data)

    def setFitness(self):
        for chromosome in self.genotype.chromosomes:
            chromosome.fitness = self.evalFSM(chromosome)
