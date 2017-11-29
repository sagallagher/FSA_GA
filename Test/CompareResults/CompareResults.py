
# run the script with a directoy of outputs as a parameter
# script will display graphs of the number of solutions checked for each example
# in each file
# additionaly, misc stats are displayed

import os, os.path
import matplotlib.pyplot as plt
import numpy as np
import math
import sys

# return the list of solution counts at the bottom of the output files
def getSolutionCountList(filename):

    # store the previous line
    last_line = ''

    # loop until last line of file
    with open(filename,'r') as f:
        for line in f: last_line = line

    # parse that last line (which is the list) into a list
    return [int(x) for x in last_line.replace('[','').replace(']','').replace(' ','').split(',')]

# plot the outputs of each output file in a given directory
def plotOutputs(directory, clear_ticks = False):
    # dimension for the canvas
    dim = int(math.ceil((math.sqrt(len(os.listdir(directory))))))

    # canvas for all the plots
    f, canvas = plt.subplots(dim, dim)

    i = -1
    j = 0

    # search through each file looking for
    for outfile in os.listdir(directory):
        solution_list = getSolutionCountList(directory+'/'+outfile)

        # track next location of subplot
        if i < dim-1: i+=1
        else:
            i = 0
            j+=1

        # add subplot to canvas
        canvas[i,j].scatter(np.arange(len(solution_list)),solution_list)
        canvas[i,j].set_title(outfile)

    if clear_ticks:
        # clear ticks in each sub plot
        for i in range(0,dim):
            for j in range(0,dim):
                canvas[i,j].set_yticklabels([])
                canvas[i,j].set_xticklabels([])

    # display the plot
    plt.tight_layout()
    plt.show()

# given a list of output files, return the one that contains the best average
def bestAverage(directory):

    # used to store the best average
    best = -1

    # store the path to the best output file
    result = ''

    # search through each file looking for
    for outfile in os.listdir(directory):
        solution_list = getSolutionCountList(os.path.join(directory,outfile))

        average = np.mean(solution_list)
        print solution_list, average
        if (average < best or best == -1) and average >= 0:
            best = average
            result = str(outfile)+'\t'+str(average)


    return result

def giveUpCount(solution_list):
    return len([i for i in solution_list if i < 0])


def getStats(file_path):
    solution_list = getSolutionCountList(file_path)

    return np.mean(solution_list),np.median(solution_list),giveUpCount(solution_list)

def displayStats(directory):


    for outfile in os.listdir(directory):
        (mean, median, give_up) = getStats(os.path.join(directory,outfile))
        print '--',outfile,'--'
        print 'MEAN:%20s'% mean
        print "MEDIAN:%20s" % median
        print "GIVE UP:%20s" % give_up
    print "\nBEST AVG:%20s" % bestAverage(directory)

# plot the average solutions checked in each file
def plotAverages(directory):
    pass


displayStats(sys.argv[1])
plotOutputs(sys.argv[1])
