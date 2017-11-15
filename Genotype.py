class Genotype():
    def __init__(self):
        self.chromosomes = []

    def __str__(self):
        result = ''
        for chromosome in self.chromosomes: result += ('-'*50+'\n' + str(chromosome))
        return result

    def pushChromosome(self, chromosome):
        self.chromosomes.append(chromosome)

    def getMaxFitness(self):
        max_fitness = 0
        for chromosome in self.chromosomes:
            if chromosome.fitness > max_fitness: max_fitness = chromosome.fitness

        return max_fitness
