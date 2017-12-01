
from lib.GeneticAlgorithm.Genotype.Chromosome import *
from lib.Utility.MinimizeFSA import *

c = Chromosome([[0, 1],[0, 1],[2,3],[2,3],[4,0]],[2])
m = MinimizeFSA(c)

m.minimize()
