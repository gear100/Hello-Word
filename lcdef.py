import sys
import os



class UlcLcdef2List:
    def __init__(self,file):
        self.file = file
    
                #list.append([(n[i:j]) for i,j in lineformat])
                                
    def ulc(self):
        inp = open(self.file, "r")
        lineformat , grp, sid = [(0,8),(8,16),(16,24),(24,32),(32,40),(40,48),(48,56),(56,64),(64,72),(72,81)] ,"gru" ,"sid"

        line = inp.readline()
        dic_ulc = {}
        while 1:

                        if line.startswith("$LCASE"):
                                n = line.rstrip("\n").ljust(80)# + "\n"                             # add \n on position 81 for each line
                                dic_ulc["LCASE"]=n[8:].split()
                                cou = 1
                                #print line


                                line = inp.readline()

                                while line.startswith(" "):
                                        n = line.rstrip("\n").ljust(80)
                                        dic_ulc[cou]=[n[:8], n[8:]]
                                        
                                        cou +=1
                                        line = inp.readline()
                                      
                        break
        
        inp.close()
            

        return dic_ulc

class ClcLcdef2List():

        ulc={1000:"ulc n/a"}
        csv = ""
        DICcsv = ""


        def __init__(self,file,find=""):
                self.file = file
                self.find = find
                ClcLcdef2List.ulc= UlcLcdef2List(file).ulc() # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
                #list.append([(n[i:j]) for i,j in lineformat])

                if self.find == "" or self.find == "PRINT only" :
                        
                        print " no function find acvivated"
                elif self.find != "" or self.find != "PRINT only":
                        
                        print " function find is acvivated", self.find
                

                if self.csv == 1:
                        out = open(self.DICcsv + "lcdef.csv", "w")
                        print " file created:     ", self.DICcsv , "lcdef.csv"

                elif self.csv == "":
                    
                        print " csv file NOT  created:"

                        
        def clc(self):
            inp = open(self.file, "r")
            lineformat , grp, sid = [(0,8),(8,16),(16,24),(24,32),(32,40),(40,48),(48,56),(56,64),(64,72),(72,81)] ,"gru" ,"sid"
            lineformatCOM , grp, sid = [(8,16),(16,24),(24,32)] ,"gru" ,"sid"
            line = inp.readline()
            dic_ulc = {}
            cou = 500
            while 1:
                        
                        if line.startswith("$LCOMB"):
                                cou += 1 
                                n = line.rstrip("\n").ljust(80)
                                COM = ";".join([(n[i:j]) for i,j in lineformatCOM])
                                clc = "CLC_id;"  + str(cou).ljust(4)  +  ";" + COM + ";"

                                #print cou, line[8:].split()
                                
                                line = inp.readline()
                                while line.startswith(" "):
                                        #print line
                                        n = line.rstrip("\n").rjust(80)
                                        list = [(n[i:j]) for i,j in lineformat]

                                        for x in list:
                                                if "." not in x and x.strip() != "":

                                                        id_ulc = int(x.strip()) - 20000

                                                        ulc = " ".join([a for a in self.ulc[id_ulc]])

                                                        Toprint =  clc +  str(id_ulc).strip().ljust(8)  + ";"  +  ulc.strip().ljust(80)  + ";",     str(x).ljust(8),  ";"

                                                        #print Toprint[0],
                                                        
                                                if "." in x:
                                                        Toprint2 =  "Fac" +  " ; "  +  str(x).ljust(8)  + ";"
                                                        ToprintAll = Toprint[0] +  Toprint2



                                                        if self.find == "" or self.find == "PRINT only":
                                                                print   ToprintAll
                                                                
                                                        else:
                                                                if self.find in ToprintAll:
                                                                        print   ToprintAll
                                                                        if self.csv == 1:
                                                                                self.out.write(ToprintAll)


                                                        
                                                if x.strip() == "":
                                                        #print "?????????????????????????"
                                                        break

                                        line = inp.readline()
                                        if not line:
                                                     break
                
                                        
                        else:
                                line = inp.readline()
                                if not line:
                                                break
        
            inp.close()
            

            return dic_ulc


    
if __name__ == '__main__':

        print  "\n _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/ \n"

        path =  os.path.dirname(os.path.abspath(sys.argv[0])) + "\\"

        #print "work dictionary :" ,path

        file_1 = "LCDDEC14.SDB"
        file_p = path + file_1
        
        if os.path.isfile(file_p):
                        sys.stdout.write("file exist: \n -ok-->   " + file_p + "\n")
        else:
                sys.stderr.write("[ERO] no file find: \n -ero->   " + file_p+ "\n")


        print  "\n _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/ \n"

        ulc_1 = UlcLcdef2List(file_p).ulc()


        print type(ulc_1)

        for inp in ulc_1:
                print inp, ulc_1[inp]


        print  "\n _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/ \n"

        
        clc_1 = ClcLcdef2List(file_p).clc()

        print type(clc_1)
        
        
