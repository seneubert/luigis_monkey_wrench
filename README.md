# Luigi's Monkey Wrench

This is a small library (50 LOC exactly, as of Feb 12) that intends to make writing [Luigi]() workflows that use a lot of shell commands
(which is common e.g. in HEP or bioinformatics) a tad easier by allowing to define workflow tasks with a simple shell command pattern, and
dependencies by using a simple single-assignment patter for specifying how tasks inputs depend on each other's outputs, like so:

````python
import luigi
from luigis_monkey_wrench import *

class MyWorkFlow(WorkflowTask):
    def requires(self):
		# Create some tasks
        hejer = shell('echo hej > <o:hejfile:hej.txt>')
        fooer = shell('cat <i:hejfile> | sed "s/hej/foo/g" > <o:foofile:<i:hejfile:.txt|.foo>>')

		# Connect them together
        fooer.inports['hejfile'] = hejer.outport('hejfile')

		# Return the last one in the chain
        return fooer

# Make this a runnable script, and leave control to luigi
if __name__ == '__main__':
    luigi.run()
````

Short and neat, ain't it?

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
git clone https://github.com/seneubert/luigis_monkey_wrench.git .
````

Run the example script (or one that you have already)
````bash
python root_example.py --local-scheduler MyWorkFlow
````

## Current Status: Experimental

***Use on your own risk only!***
