# Luigi's Monkey Wrench

This is a small library (50 LOC exactly, as of Feb 12) that intends to make writing [Luigi]() workflows that use a lot of shell commands
(which is common e.g. in bioinformatics) a tad easier by allowing to define workflow tasks with a simple shell command pattern, and 
dependencies by using a simple single-assignment patter for specifying how tasks inputs depend on each other's outputs, like so:

````python
import luigi
from luigis_monkey_wrench import *

# Yes, we write the workflow definition inside a normal luigi task ...
class MyWorkFlow(WorkflowTask):

    # ... and do this by setting up the dependency graph and (letting the workflow
    # task depend on it, by) returning the last task in the dependecy graph in the
	# workflow task's requires() function:
    def requires(self):

        # Create tasks by initializing ShellTasks, and giving
        # the shell tasks to execute to the cmd parameter.
        # File names are given in a this special form (including <>):
        #   <i:INPUT_NAME>
        #   <o:OUTPUT_NAME:OUTPUT_FILENAME>
        # Output file names can also include the filename of an input:
        #   <o:some_output:<i:some_input>.some_extension>
        hejer = shell('echo hej > <o:hejfile:hej.txt>')
        fooer = shell('cat <i:hejfile> | sed "s/hej/foo/g" > <o:foofile:<i:hejfile>.foo>')

        # Define the workflow "dependency graph" by telling how outputs
        # from tasks are re-used in inputs of other tasks
        fooer.inports['hejfile'] = hejer.outport('hejfile')

        # Return the last task in the workflow
        return fooer


# We finally make this file into an executable python file, and let luigi take of the running
# which will, among many other cool things, mean that we get a nice command line interface
# generated for us:
if __name__ == '__main__':
    luigi.run()
````
Now run this (as usual with luigi tasks) like this:
````bash
python workflow_example.py --local-scheduler MyWorkFlow
````

## Quick start

Install the dependencies, luigi (and optionally tornado):
````bash
pip install luigi
pip install tornado
````

Clone this git repo to somewhere:
````bash
mkdir testlmw
cd testlmw
git clone https://github.com/samuell/luigis_monkey_wrench.git .
````

Run the example script (or one that you have already)
````bash
python workflow_example.py --local-scheduler MyWorkFlow
````

## Current Status: Experimental

***Use on your own risk only!***
