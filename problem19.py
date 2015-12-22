from inputs.input19 import input
import re
import copy
string = input()
array = string.splitlines()
biology = "CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl"
molecules = []
value = 0
replacements = []

class Molecule:
    def __init__(self,name):
        self.possibilities = []
        self.name = name

#Setup
for lines in array:
    matchUp = re.match("(.+) => (.+)",lines)
    if matchUp:
        molecule = matchUp.group(1)
        possibility = matchUp.group(2)
        #Check if we already have the molecule
        found = False
        for m in molecules:
            if m.name == molecule:
                m.possibilities.append(possibility)
                found = True
        if not found:
            m = Molecule(molecule)
            m.possibilities.append(possibility)
            molecules.append(m)

# Work out the biology!
def oldBiology(index,string):
    current = biology[index]
    #Check if next is lowercase
    if len(biology) > index + 1:
        if ord(biology[index + 1]) >= 97:
            current += biology[index + 1]
            index += 1
    #Check if in molecules
    for m in molecules:
        if m.name == current:
            found = True
            for p in m.possibilities:
                updatedString = string + p
                #Check if last
                if len(biology) == index + 1:
                    replacements.append(updatedString)
                else:
                    Biology(index + 1,updatedString)
    found = False
    if not found:
        string += current
        #Check if last
        if len(biology) == index + 1:
            replacements.append(string)
        else:
            Biology(index + 1,string)

def Biology(index,done,string):
    current = biology[index]
    #Check if next is lowercase
    if len(biology) > index + 1:
        if ord(biology[index + 1]) >= 97:
            current += biology[index + 1]
            index += 1
    print "Current", current
    if done:
        #Check if last
        string += current
        if len(biology) == index + 1:
            replacements.append(string)
        else:
            Biology(index + 1,done,string)
    else:
        #Check if in molecules
        found = False
        for m in molecules:
            if m.name == current:
                found = True
                for p in m.possibilities:
                    updatedString = string + p
                    #Check if last
                    if len(biology) == index + 1:
                        replacements.append(updatedString)
                    else:
                        Biology(index + 1,True,updatedString)
                #Check if last
                if len(biology) != index + 1:
                    string += current
                    Biology(index + 1,False,string)
        if not found:
            string += current
            #Check if last
            if len(biology) != index + 1:
                Biology(index + 1,done,string)

Biology(0,False,"")
replaceSet = set(replacements)

print "answer" , len(replaceSet)
