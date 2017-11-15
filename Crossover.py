from Chromosome import *
from random import randint

class Crossover():

    def __init__(self, genotype):
        self.genotype = genotype

        self.getOffspring()

    # get the two most fit chromosomes
    def getMostFit(self):
        most_fit = Chromosome([],[])
        most_fit2 = Chromosome([],[])
        for chromosome in self.genotype.chromosomes:
            if chromosome.fitness > most_fit.fitness: most_fit = chromosome

        for chromosome in self.genotype.chromosomes:
            if (chromosome.fitness > most_fit2.fitness
                and chromosome.fsm != most_fit.fsm): most_fit2 = chromosome

        return most_fit, most_fit2

    # get the two least fit chromosomes
    def getLeastFit(self):
        least_fit = Chromosome([],[])
        least_fit.fitness = 1.1
        least_fit2 = Chromosome([],[])
        least_fit2.fitness = 1.1

        for chromosome in self.genotype.chromosomes:
            if chromosome.fitness < least_fit.fitness: least_fit = chromosome

        for chromosome in self.genotype.chromosomes:
            if (chromosome.fitness < least_fit2.fitness
                and chromosome.fsm != least_fit.fsm): least_fit2 = chromosome

        return least_fit, least_fit2

    # get the result of the cross over of the most fit parents
    def getOffspring(self):

        (parent1, parent2) = self.getMostFit()

        child1 = Chromosome([],[])
        child2 = Chromosome([],[])

        # get a random pivot
        random_pivot = randint(0,len(parent1.fsm))


        # one point crossover on rows
        child1.fsm = parent1.fsm[:random_pivot] + parent2.fsm[random_pivot:]
        child2.fsm = parent2.fsm[random_pivot:] + parent2.fsm[:random_pivot]

        random_pivot2 = randint(0, len(parent2.final_states))
        # one point crossover on final states
        child1.final_states = parent1.final_states[:random_pivot2] + parent2.final_states[random_pivot2:]
        child2.final_states = parent2.final_states[random_pivot2:] + parent2.final_states[:random_pivot2]

        self.selectSurvivors(child1, child2)

    # replace the least fit chromosomes with the offspring of the most fit
    def selectSurvivors(self, child1, child2):

        (least_fit1, least_fit2) = self.getLeastFit()
        
        self.genotype.chromosomes.remove(least_fit1)

        self.genotype.chromosomes.remove(least_fit2)

        self.genotype.pushChromosome(child1)
        self.genotype.pushChromosome(child2)
