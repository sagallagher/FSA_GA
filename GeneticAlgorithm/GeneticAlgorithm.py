
# take in genetic operators and call their start() methods


from Genotype.Genotype import *

class GeneticAlgorithm():
    # take objects to initialize the population, calculate the fitnes, 
    # and perform the crossover and mutation operations
    def __init__(self, initialize_population, fitness, crossover, mutation):
        self.initialize_population = initialize_population
        self.fitness = fitness
        self.crossover = crossover
        self.mutation = mutation

    # run the genetic algorithm
    def start(self, introduce_diversity_at, threshold, give_up_at):

        # used to track the generation we are on
        generation = 1
        
        # used to track the last time we introduced diversity
        restart_count = 1
        
        # initialize the genotype
        self.initialize_population.start(geno)
        
        # set fitness of initial population
        self.fitness.start(geno)
        
        # initialize count to the number of solutions initially being checked
        count = len(geno.chromosomes)

        # used store most fit
        most_fit = Chromosome([],[])
        most_fit.fitness = 0

        # loop until end condition is met
        while(True):
     
            # store the most fit of all generations to return if give up is hit
            if geno.getMostFit().fitness > most_fit:
                most_fit = geno.getMostFit()

            if generation >= give_up_at: break
            # if we exceed N generations, introduce random chromosomes to the genotype
            if generation > introduce_diversity_at*restart_count:
                self.initialize_population.introduceDiversity(geno)
                restart_count += 1
                
            # display the generation count every 1000 generations
            if generation%1000 == 0: print "generation:\t", generation
            
            # calculate the fitness of the population
            self.fitness.start(geno)
            
            # if we have met our threshold, stop looping
            if geno.getMaxFitness() >= threshold:
                if geno.getMostFit().fitness > most_fit:
                    most_fit = geno.getMostFit()
                break
            
            # mutate the genotype
            self.mutation.start(geno)

            # crossover and select survivors in the genotype
            self.crossover.start(geno)
            
            # increment our generation count
            generation+=1
            
            # track how many solutions we have checked
            count+=len(geno.chromosomes)



        # if we give, return a negative solution count
        if generation >= give_up_at: count = -count
            
        # return the most fit chromosome and the solutions checked in finding it
        return most_fit, count
