from DataParser.DataParser import *
from InitializePopulation.RandomInitializePopulation import *
from Fitness.FSMHitRatioFitness import *
from Crossover.RandomCrossover import *
from Mutation.RandomTransitionMutation import *
from Genotype.Genotype import *
from GeneticAlgorithm.GeneticAlgorithm import *
import os

# loop through a directory and output FSM for each learning data set
def testAll(directory):
    with open('output.txt','w') as f:
        for filename in os.listdir(directory):
            print "Parsing:\t", filename
            dp = DataParser(os.path.join(directory, filename))
            dp.setAlphabetSize()


            ip = RandomInitializePopulation(dp,3,2,10);
            fitness = FSMHitRatioFitness(dp)
            c = RandomCrossover()
            m = RandomTransitionMutation(dp)
            ga = GeneticAlgorithm(ip,fitness,c,m)


            (fsm,generation) = ga.start(10000,.8,100000)
            f.write(filename+'\n')
            f.write('Generation:\t'+str(generation)+'\n'+str(fsm)+'\n')
            print "Finished parsing:\t", filename


# main method
if __name__ == '__main__':

    testAll('Data/RandomData/')
