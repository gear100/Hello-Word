import sys

sys.path.append('D:\\01-AREK-2015\\git-project\\Hello-Word')
from src import filecheck

import struct


# def


def splitLineMscexplDisprep(line,leng=88):
    
    li = struct.unpack("9s13s13s13s13s13s13s", line[:leng])
    li = [ s.strip() for s in li]
    return li




# inputs
file_1 = "840901G.out"
file = "840901.out"

# check if file exist
filecheck.fileexist(file)

'''
muster
     679 -3.56396E+00 -5.19064E+00 -1.44532E+02  3.64840E-03  4.82102E-03 -2.11914E-03
___9_____------13-----_____13______----13-------

'''

inp = open(file, "r")

with open(file,'rb') as f:
    while True:
        line=f.readline()
        if not line: break

        if "Grid_Id :" in line:
            print line
            id = line.split("Grid_Id :")[-1].strip()[:8]
        if len(line) >=88:
            #print len(line), line

            print splitLineMscexplDisprep(line,leng=87)

print "Grid_Id :\n---->  ", id
