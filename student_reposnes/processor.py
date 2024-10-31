import os

def readAndWrite(readPath:str,writePath:str)->None:
    fileLen =0
    read=open(readPath,'r')
    num =0
    startReading =False
    write = open(writePath + "studentResponse" +str(num + fileLen) +".py",'w')
    for line in read:
        if("\"def" in line):
            startReading=True
            write.write(line[1:])
        elif(startReading and not "\"" in line):
            write.write(line)
        elif(startReading and "\"" in line):
            write.write(line[:-2])
            num+=1
            write = open(writePath + "studentResponse" +str(num + fileLen) +".py",'w')
            startReading=False
    read.close()
    write.close()


def main()->None:
    readAndWrite("student_reposnes\\results.txt","student_reposnes\\studentResponeses\\")

if __name__=='__main__':
    main()