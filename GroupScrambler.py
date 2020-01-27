"""
GroupScrambler
"""
from random import shuffle

fileBase = "GroupScrambler"

class Class(object):
    def __init__(self, name, groups):
        self.name = name
        self.nGroups = len(groups)
        self.groups = groups
        nStudents = 0
        for gr in self.groups:
            nStudents += len(gr)
        self.nStudents = nStudents
        
    def __str__(self):
        strn = self.name + "\n"
        strn += "{}\n".format(len(self.groups))
        for gr in self.groups:
            for p in gr:
                strn += p + ", "
            strn += '\n'
        return strn
    
    def makeGroups(self, nGroups):
        # Shuffle each group, then concatenate
        shuffledList = []
        for gr in self.groups:
            shuffle(gr)
            shuffledList += gr
        # make empty groups
        newGroups = []
        for i in range(nGroups):
            newGroups.append([])
        # Make new groups by striding through the shuffled list
        for i in range(len(shuffledList)):
            newGroups[i % nGroups].append(shuffledList[i])
        self.nGroups = nGroups
        self.groups = newGroups
    
def readClasses(fileName):
    fp = open(fileName, 'r')
    nClasses = int(fp.readline())
    classes = []
    for i in range(nClasses):
        name = fp.readline().strip()
        nGroups = int(fp.readline())
        groups = []
        for j in range(nGroups):
            line = fp.readline().strip(' ,\n\t').split(',')
            for (i,p) in enumerate(line):
                line[i] = p.lstrip()
            groups.append(line)
        classes.append(Class(name, groups))
    fp.close()
    return classes

def writeClasses(classes, fileName):
    fp = open(fileName, 'w')
    nClasses = len(classes)
    fp.write("{}\n".format(nClasses))
    for class0 in classes:
        fp.write("{}\n{}\n".format(class0.name, len(class0.groups)))
        for group in class0.groups:
            for student in group:
                fp.write("{}, ".format(student))
            fp.write("\n")
    fp.close()

def writeHTML(class0, fileName, nWeek):
    # This is smallest HTML 5 page with content
    # Oh. I added a CSS style sheet
    htmlHead = \
"""<!doctype html><html lang=en>
<head><meta charset=utf-8><title>A</title><link rel="stylesheet" href="{}.css"></head>
<body>\n""".format(fileBase)
    fp = open(fileName, 'w')
    fp.write(htmlHead)
    fp.write(
"""<h1>{}</h1>
<h2>Week {}</h2>
<h2>{} Groups</h2>
""".format(class0.name, nWeek, len(class0.groups)))
    # Start Table
    htmlTableHead = \
"""<table border="1">
<tr>
    <th>Group #</th>
    <th>Members</th> 
</tr>\n"""
    fp.write(htmlTableHead)
    for (i, group) in enumerate(class0.groups):
        fp.write("<tr><td>Group {}</td>".format(i+1))
        for student in group:
            fp.write("<td>{}</td>".format(student))
        fp.write("</tr>\n")
    fp.write("</table>")
    fp.close()

# EOF
