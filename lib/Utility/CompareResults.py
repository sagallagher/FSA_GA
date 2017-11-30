
# run the script with a directoy of outputs as a parameter
# script will display graphs of the number of solutions checked for each example
# in each file
# additionaly, misc stats are displayed

import os, os.path
import matplotlib.pyplot as plt
import numpy as np
import math
import sys
from mpl_toolkits.mplot3d import Axes3D


class CompareResults():
    def __init__(self, directory):
        self.directory = directory
    # return the list of solution counts at the bottom of the output files
    def getSolutionCountList(self,filename):

        # store the previous line
        last_line = ''

        # loop until last line of file
        with open(filename,'r') as f:
            for line in f: last_line = line

        # parse that last line (which is the list) into a list
        return [int(x) for x in last_line.replace('[','').replace(']','').replace(' ','').split(',')]

    # plot the outputs of each output file in a given self.self.directory
    def plotOutputs(self, clear_ticks = False):
        # dimension for the canvas
        dim = int(math.ceil((math.sqrt(len(os.listdir(self.directory))))))

        # canvas for all the plots
        f, canvas = plt.subplots(dim, dim)

        i = -1
        j = 0

        # search through each file looking for
        for outfile in os.listdir(self.directory):
            solution_list = getSolutionCountList(self.directory+'/'+outfile)

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

    def plot3D(self,x,y,z):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.scatter(x, y, z, c='r', marker='o')
        ax.set_zlabel('Solutions Checked')
        ax.set_xlabel('Alphabet Size')
        ax.set_ylabel('Examples per File')


    # two graphs, one with x-axis as alphabet size, one with x-axis as
    def plotAllOneGraph(self,min_alph,max_alph,min_ex,max_ex,files_to_gen):

        solutions = []

        outfiles = []

        # loop through each output file
        for outfile in os.listdir(self.directory):
            # store the file
            outfiles.append(int(outfile))

        # sort the output files in ascending order
        outfiles = sorted(outfiles)

        for ofile in outfiles:
            # get the solutions on last line
            solution_list = self.getSolutionCountList(self.directory+'/'+str(ofile))

            # append the list to all solulution 2d array
            solutions.append(solution_list)

        # canvas for our graphs
        f, can = plt.subplots(2, 1)

        # plot first graph that has alphabet sizes as x axis
        x= []
        for i in range(min_alph,max_alph+1):
            for j in range(min_ex,max_ex+1):
                for b in xrange(files_to_gen):
                    x.append(i)


        can[0].scatter(x,solutions)
        can[0].set_ylabel('Solutions Checked')
        can[0].set_xlabel('Alphabet Size')
        can[0].set_title('Solutions Checked vs. Alphabet Size')

        # plot second graph that has examples per file as x axis
        y = []
        for i in range(min_alph,max_alph+1):
            for j in range(min_ex,max_ex+1):
                for b in xrange(files_to_gen):
                    y.append(j)

        can[1].scatter(x,solutions)

        can[1].set_ylabel('Solutions Checked')
        can[1].set_xlabel('Examples per File')
        can[1].set_title('Solutions Checked vs. Examples per File')

        # display graph
        plt.tight_layout()

        self.plot3D(x,y,solutions)

        plt.show()



    # given a list of output files, return the one that contains the best average
    def bestAverage(self):

        # used to store the best average
        best = -1

        # store the path to the best output file
        result = ''

        # search through each file looking for
        for outfile in os.listdir(self.directory):
            solution_list = self.getSolutionCountList(os.path.join(self.directory,outfile))

            average = np.mean(solution_list)
            print solution_list, average
            if (average < best or best == -1) and average >= 0:
                best = average
                result = str(outfile)+'\t'+str(average)


        return result

    def giveUpCount(self,solution_list):
        return len([i for i in solution_list if i < 0])


    def getStats(self,file_path):
        solution_list = self.getSolutionCountList(file_path)

        return np.mean(solution_list),np.median(solution_list),giveUpCount(solution_list)

    def displayStats(self):


        for outfile in os.listdir(self.directory):
            (mean, median, give_up) = self.getStats(os.path.join(self.directory,outfile))
            print '--',outfile,'--'
            print 'MEAN:%20s'% mean
            print "MEDIAN:%20s" % median
            print "GIVE UP:%20s" % give_up
        print "\nBEST AVG:%20s" % self.bestAverage(self.directory)

    # plot the average solutions checked in each file
    def plotAverages(self):
        pass
