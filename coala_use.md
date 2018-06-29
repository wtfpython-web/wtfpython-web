#Coala

This is a guide on how to use coala-bears for this project

This project consists of a .coafile which basically has all the guidelines
that needs to be followed when working with coala.It can modified.

In order to specify the files to analyze, you can use the --files argument. 
For all file paths, you can specify (recursive) globs.

`coala --files=src/\*.c --bears=SpaceConsistencyBear --save`

Coala will now ask you for missing values that are needed to perform the analysis.  
Coala will now check the code and, in case there are errors it will be duly pointed out.
You can also run coala in non interactive mode 
`coala  --non-interactive`  

###Auto-applying results
Coala includes a special setting called default_actions that allows you to set the 
action for a bear that shall be automatically applied on run. It has a command line 
alias --apply-patches to make it easier to use.
For eg
`coala -S python.bears=PEP8Bear python.files=\*\*/\*.py --apply-patches --save`
This command would automatically fix all your issues in python files.

###Help
To know more about Coala you could do the following
`coala -h`
To follow the documentation follow the [link](https://docs.coala.io/en/latest/Users/Tutorial.html)