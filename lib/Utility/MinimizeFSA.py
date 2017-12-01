import collections

class MinimizeFSA():

    # constructor
    def __init__(self,chromosome):
        self.chromosome = chromosome

    def getNonFinalStates(self):

        # get total number of states
        num_states = len(self.chromosome.fsm)

        # generate array of all states
        states = [i for i in xrange(num_states)]

        # remove final states
        for state in states:
            if state in self.chromosome.final_states: states.remove(state)

    def getEq(self):
        eqs = {}
        checked = []
        # find equivelent classes
        for i,row in enumerate(self.chromosome.fsm):
            eq = [i]
            for j,other_row in enumerate(self.chromosome.fsm):

                if i != j and row == other_row:
                    eq.append(j)

            # make sure theres no duplicates
            if sorted(eq) not in checked:
                eqs[str(sorted(eq))]=row
            checked.append(eq)

        return collections.OrderedDict(sorted(eqs.items()))

    def getNewFSM(self,eqs):

        # split keys of eq classes into 2d array
        keys = []
        for key in eqs: keys.append(eval(key))

        # hold out new FSM
        new_fsm = []

        # go through each transition in og fsm
        for row in self.chromosome.fsm:
            new_row = []
            for transition in row:
                # find the index of that row in the new fsm
                for i,key in enumerate(keys):
                    # create a new row based on these indices
                    if transition in key: new_row.append(i)
            if new_row not in new_fsm: new_fsm.append(new_row)

        # return the newly generated FSM
        return new_fsm

    def getFinalStates(self,new_fsm,eqs):
        # split keys of eq classes into 2d array
        keys = []
        for key in eqs: keys.append(eval(key))

        new_final_states = []

        # look for each final states new index
        for final_state in self.chromosome.final_states:
            for i,key in enumerate(keys):
                if final_state in key: new_final_states.append(i)

        # return the newly found final states
        return new_final_states

    def minimize(self):

        # get array of non final states
        non_final_states = self.getNonFinalStates()

        # store the final states
        final_states = self.chromosome.final_states

        # set of non final and final states
        p = [[non_final_states],[final_states]]

        # get the equivelent states in the fsm
        eqs = self.getEq()

        # need to make lookup table mapping old row to new row
        new_fsm = self.getNewFSM(eqs)

        # set the final states of the new fsm
        self.getFinalStates(new_fsm,eqs)

        # return a chromosome with the minimized fsm and associated final states
        return Chromosome(new_fsm,final_states)
