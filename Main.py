from DataParser.DataParser import *
from InitializePopulation.RandomInitializePopulation import *
from Fitness.FSMHitRatioFitness import *
from Crossover.RandomCrossover import *
from Mutation.RandomTransitionMutation import *
from Genotype.Genotype import *
from GeneticAlgorithm.GeneticAlgorithm import *
import os

# loop through a directory and output FSM for each learning data set
def testAll(directory, introduce_diversity_at, threshold, give_up):
    with open('output.txt','w') as f:
        for filename in os.listdir(directory):
            print "Parsing:\t", filename
            dp = DataParser(os.path.join(directory, filename))
            dp.setAlphabetSize()


            ip = RandomInitializePopulation(dp,20,2,10);
            fitness = FSMHitRatioFitness(dp)
            c = RandomCrossover()
            m = RandomTransitionMutation(dp)
            ga = GeneticAlgorithm(ip,fitness,c,m)


            (fsm,generation) = ga.start(introduce_diversity_at,threshold,give_up)
            f.write(filename+'\n')
            f.write('Generation:\t'+str(generation)+'\n'+str(fsm)+'\n')
            print "Finished parsing:\t", filename

def testOne(filename):
    with open('output.txt', 'w') as f:
        print "Parsing:\t", filename
        dp = DataParser(filename)
        dp.setAlphabetSize()

        ip = RandomInitializePopulation(dp,20,2,20);
        fitness = FSMHitRatioFitness(dp)
        c = RandomCrossover()
        m = RandomTransitionMutation(dp)
        ga = GeneticAlgorithm(ip,fitness,c,m)


        (fsm,generation) = ga.start(1000,.8,20000)
        f.write(filename+'\n')
        f.write('Generation:\t'+str(generation)+'\n'+str(fsm)+'\n')
        print "Finished parsing:\t", filename


# main method
if __name__ == '__main__':
    # loop through all learning data sets in a directory
    testAll('Data/RandomData/',1000, .9, 10000)
    #testOne("Data/test_data.txt")
