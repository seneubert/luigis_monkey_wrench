import luigi
from luigis_monkey_wrench import *

# Yes, we write the workflow definition inside a normal luigi task ...
class MyWorkFlow(WorkflowTask):
    def requires(self):
        # make several generator tasks
        pssim = []
        for i in range(0,5) :
            pssim.append(shell('root -l -b -q ps.C\\(\\"<o:testps{0}:testps{0}.root>\\",12345{0}\\)'.format(i) ))
        
        hadder = shell('hadd <o:ntupl:ntuple.root> testps?.root')
        # Define the workflow "dependency graph" by telling how outputs
        # from tasks are re-used in inputs of other tasks
        for i in range(0,5) :
            hadder.inports['testps{0}'.format(i)] = pssim[i].outport('testps{0}'.format(i))

        plotter=shell('root -l -b -q plot.C\\(\\"<i:ntupl>\\",\\"<o:plotfile:plots.root>\\" \\)'.format(i) )
        plotter.inports["ntupl"]=hadder.outport("ntupl")
        
        # Return the last task in the workflow
        return plotter

# We finally make this file into an executable python file, and let luigi take of the running
# which will, among many other cool things, mean that we get a nice command line interface
# generated for us:
if __name__ == '__main__':
    luigi.run()
