'''
If you want to use this program, edit the constants

Makes a template file for the black binder programs

Licensed under my GitHub account license; find it at lakewood999.github.io

Note: This is version two.  There is a config file, which should be placed in this folder.  The file will be created in the folder before this folder.
'''

########################
# Assign Constants     #
########################
NAME = "su steven"
NAME_UPPER = "Steven Su"

#######################
# Asks for variables  #
#######################
numberPage = input("Page 1: ")
numberPageTwo = input("Page 2: ")
numberProblem = input("Question #: ")
docstring = input("Docstring information: ")

#####################
# Changes variables #
#####################
if len(numberPage) < 3:
    numberPage = (3 - len(numberPage)) * "0" + numberPage
if len(numberPageTwo) < 3:
    numberPageTwo = (3 - len(numberPageTwo)) * "0" + numberPageTwo
if len(numberProblem) < 3:
    numberProblem = (3 - len(numberProblem)) * "0" + numberProblem

if numberPage == numberPageTwo:
    number = numberPage
else:
    number = numberPage + " - " + numberPageTwo

#################################
# Read config file for comments #
#################################
configFile = open("config.txt", "r")
configDict = {}
for x in range(4):
    line = configFile.readline()
    parts = line.split(": ")
    var = parts[0]
    info = parts[1].replace("\n", "")
    configDict[var] = info
configFile.close()

#################
# Make file     #
#################
file = open("../" + numberPage + " " + numberProblem + " " + NAME + " " + "ggggggg.py", "w")
file.write('"""\n')
file.write("Page " + number + "\n")
file.write("Exercise " + numberProblem + "\n\n")
file.write("Program by: " + NAME_UPPER + "\n\n")
file.write(docstring + "\n")
file.write('"""\n')

if configDict["import"] == "yes":
    file.write("""
###################
# Import modules  #
###################

""")
if configDict["initialize"] == "yes":
    file.write("""
#########################
# Initialize Variables  #
#########################

""")
if configDict["main"] == "yes":
    file.write("""
###################
# Main Program    #
###################

""")
if configDict["summary"] == "yes":
    file.write("""
###################
# Print summary   #
###################

""")

file.close()
print("\nFile successfully created\n\n")
input("Press any key to continue...")



