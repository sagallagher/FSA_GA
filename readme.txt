----------------------------------------------------------------
Introduction
----------------------------------------------------------------

A supervised genetic algorithm approach for the automatic generation of finite state automata.

----------------------------------------------------------------
Configutation
----------------------------------------------------------------
#
# EXAMPLE CONFIGURATION FILE
#

################################################################################
# USER SETTINGS
################################################################################
# generate random files
RANDOM_GEN = True

# file to output results in for a single test
OUTPUT_FILE = output.txt

# which test to run
# 1 => Single Directory Test
# 2 => Generate Random Tests | RANDOM_GEN must be true for this to work
TEST_OPTION = 2

################################################################################
# LEARNING DATA GENERATOR SETTINGS
################################################################################
# prefix to place on numbered outputted files
DIRECTORY = data/RandomData/Dataset1/
# number of learning data sets to generate
FILES_TO_GENERATE = 2


# number of examples to include in each file
EXAMPLES_PER_FILE = 10
# the size of the alphabet to use
ALPHABET_SIZE = 5
# minimum length of each example word
MINIMUM_LENGTH = 0
# maximum length of each example word
MAXIMUM_LENGTH = 25

################################################################################
# MULTI_TESTER SETTINGS
################################################################################

OUTPUT_DIRECTORY = /data/Outputs/RandomOutput
# the size to begin testing
MIN_ALPHABET_SIZE = 2
# the size to end testing
MAX_ALPHABET_SIZE = 4
# the minimum examples to start with in each file
MIN_EXAMPLES_PER_FILE = 1
# the max examples to start with in each file
MAX_EXAMPLES_PER_FILE = 10


FILE_PREFIX = 0

################################################################################
# GENETIC ALGORITHM SETTINGS
################################################################################
# add another random individual to the population at this generation
DIVERSITY_AT = 1000
# stop pursing current learning data set when there is a chromosome of this fitness
THRESHOLD = 1
# generation to stop pursuing the current learning data set
GIVE_UP = 10000
# the number of randomly generated FSMs to include in the initial population
POPULATION_SIZE = 10
# the minimum number of states for each FSM
MIN_STATES = 2
# the maximum number of states for each FSM
MAX_STATES = 10

