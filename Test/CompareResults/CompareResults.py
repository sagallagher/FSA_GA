
import os
import matplotlib.pyplot as plt
import numpy as np

# return the list of solution counts at the bottom of the output files
def getSolutionCountList(filename):

    # store the previous line
    last_line = ''

    # loop until last line of file
    with open(filename,'r') as f:
        for line in f: last_line = line

    # parse that last line (which is the list) into a list
    return [int(x) for x in last_line.replace('[','').replace(']','').replace(' ','').split(',')]


import math


def plotOutputs(directory):

    # used to store the best average
    best = -1

    # store the path to the best output file
    result = ''

    # dimension for the canvas
    dim = int(math.ceil((math.sqrt(len(os.listdir(directory))))))
    print 'dim',dim
    # canvas for all the plots
    f, canvas = plt.subplots(dim, dim)

    i = -1
    j = 0

    # search through each file looking for
    for outfile in os.listdir(directory):
        solution_list = getSolutionCountList(directory+'/'+outfile)

        # track next location of subplot
        if i < dim-1:
            i+=1
        else:
            i = 0
            j+=1

        # add subplot to canvas
        canvas[i,j].bar(np.arange(len(solution_list)),solution_list)
        canvas[i,j].set_title(outfile)

    # clear ticks in each sub plot
    for i in range(0,dim):
        for j in range(0,dim):
            canvas[i,j].set_yticklabels([])
            canvas[i,j].set_xticklabels([])

    # display the plot

    plt.show()

# given a list of output files, return the one that contains the best average
def bestAverage(directory):

    # used to store the best average
    best = -1

    # store the path to the best output file
    result = ''

    # search through each file looking for
    for outfile in os.listdir(directory):
        solution_list = getSolutionCountList(directory+'/'+outfile)

        average = sum(solution_list)/float((len(solution_list)))

        if average < best or best == -1:
            best = average
            result = str(outfile)


    return result

print bestAverage('/home/me/scripts/python/AutoAutomata/FSA_GA/Data/output')
plotOutputs('/home/me/scripts/python/AutoAutomata/FSA_GA/Data/output')
