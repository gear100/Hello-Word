import sys
import os
#
# A. Gernat 
# read file and check if exist
#
#
def fileexist(file_path):
        """
        funktion to check if file exist
        A. Gernat 03.02.2016
        """

        path =  os.path.dirname(os.path.abspath(sys.argv[0])) + "\\"

        sys.stdout.write("working dictionary :"  + path)

        if os.path.isfile(file_path):
                        sys.stdout.write("\nfile exist: \n file-ok-->   " + file_path + "\n")
        else:
                sys.stderr.write("\n[ERO] file NOT found: \n file-ero->   " + file_path + "\n")
                #sys.exit(0)



if __name__ == '__main__':
    file_0 = "..\\src_nas_res\\x_1590638.out"
    fileexist(file_0)
    file_1 = "..\\src_nas_res\\1590638.out"
    fileexist(file_1)

    print "Arek file : " , file
