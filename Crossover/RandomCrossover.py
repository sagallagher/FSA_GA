from Genotype.Genotype import *
from Genotype.Chromosome import *
from random import randint

class RandomCrossover():

    def __init__(self): pass

    # get the two most fit chromosomes
    def getMostFit(self, genotype):
        most_fit = Chromosome([],[])
        most_fit2 = Chromosome([],[])
        
        # find the first most fit
        for chromosome in genotype.chromosomes:
            if chromosome.fitness > most_fit.fitness: most_fit = chromosome

        # find the second most fit
        for chromosome in genotype.chromosomes:
            if (chromosome.fitness > most_fit2.fitness
                and chromosome.fsm != most_fit.fsm): most_fit2 = chromosome
                
        # reutrn the two most fit chromosomes
        return most_fit, most_fit2

    # get the two least fit chromosomes
    def getLeastFit(self, genotype):
        least_fit = Chromosome([],[])
        least_fit.fitness = 1.1
        least_fit2 = Chromosome([],[])
        least_fit2.fitness = 1.1

        for chromosome in genotype.chromosomes:
            if chromosome.fitness < least_fit.fitness: least_fit = chromosome

        for chromosome in genotype.chromosomes:
            if (chromosome.fitness <= least_fit2.fitness
                and not chromosome == least_fit): least_fit2 = chromosome

        return least_fit, least_fit2

    # get the result of the cross over of the most fit parents
    def getOffspring(self, genotype):
        # get the two most fit chromosomes
        (parent1, parent2) = self.getMostFit(genotype)

        # create empty chromosomes to fill with child data
        child1 = Chromosome([],[])
        child2 = Chromosome([],[])

        # get a random pivot
        random_pivot = randint(0,len(parent1.fsm))

        # one point crossover on rows
        child1.fsm = parent1.fsm[:random_pivot:] + parent2.fsm[random_pivot:]
        child2.fsm = parent2.fsm[:random_pivot] + parent1.fsm[random_pivot:]

        #
        # crossover the rows associated final states
        #
        
        # crossover the first half of the final states
        for row in xrange(random_pivot):
            if row in parent1.final_states:
                child1.final_states.append(row)
            if row in parent2.final_states:
                child2.final_states.append(row)
                
        # crossover the second half of the final states
        for row in range(random_pivot,len(parent2.fsm)):
            if row in parent1.final_states:
                child2.final_states.append(row)
            if row in parent2.final_states:
                child1.final_states.append(row)


    # replace the least fit chromosomes with the offspring of the most fit
    def selectSurvivors(self, child1, child2, genotype):
        
        # get 2 chromosomes with least fitness
        (least_fit1, least_fit2) = self.getLeastFit(genotype)
        
        # remove the least fit chromosomes
        genotype.chromosomes.remove(least_fit1)
        genotype.chromosomes.remove(least_fit2)

        # replace them with the child chromosomes
        genotype.pushChromosome(child1)
        genotype.pushChromosome(child2)

    def start(self,genotype):
        self.getOffspring(genotype)
