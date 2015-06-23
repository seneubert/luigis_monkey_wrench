# Luigi's Monkey Wrench -- HEP Edition

This is a small library (50 LOC exactly, as of Feb 12) that allows to easily write [Luigi]() workflows that use a lot of shell commands
(which is common e.g. in HEP or bioinformatics). Examples using ROOT are given. 

Goal for this fork: A full suite of tools to make LHCb analysis workflows.

## Quick start

This demo runs a small phasespace simulation, divided into 5 jobs; It 
h-adds the output into an ntuple and finally produces a plot from the ntuple. 

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
