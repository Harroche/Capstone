from random import randint
from testAnswer import check_calc
from importlib import reload
from complexity import cyclomatic
import providedSolution
import os
import sys
import csv



class HidePrint:
    '''Stops all stdout functionally when called should be used with the `with` operator.'''

    def __enter__(self):
        self.original_stdout = sys.stdout
        sys.stdout = open(os.devnull,'w')
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        sys.stdout.close()
        sys.stdout=self.original_stdout



def test_func()->bool:
    '''Will randomly generate test cases and compare the provided solution with a proven solution'''

    with HidePrint():
        reload(providedSolution)
    n = randint(3, 1e5)
    a = [0] * n
    b = []
    for j in range(n):
        a[j] = randint(1, 1e9)
        l = randint(0, n-2)
        r = randint(l, n-1)
        b.append((l, r))
    sol = check_calc(a, b)
    try:
        student_sol = providedSolution.calc(a, b)
    except NameError:
        print("Fatal Error")
        return False
    if not isinstance(student_sol, list) or len(student_sol) != len(sol):
        return False
    if student_sol != sol:
        return False
    return True

def numerical(str1:str)->int:
    num=0
    for char in str1:
        if('0'<=char and char <='9'):
            num*=10
            num+=int(char)
    return num
    


def goThoughTest(folder:str):
    '''Will retrieve and process each student solution'''
    amountOfFiles= os.listdir(folder)
    amountOfFiles = sorted(amountOfFiles,key=(lambda str1: numerical(str1)))
    data = []
    i =0
    for path in amountOfFiles:
        write(folder+"\\"+path)
        id = numerical(path)
        valid=test_func()
        with open('Analysis\\providedSolution.py','r') as file:
            code = file.read()
            cyc = cyclomatic(code)
        data.append({"type":"AI","number":id,"valid_answer":valid,"cyclomatic":cyc,"code":code})
    csvWrite(data)

        

def write(path:str):
    read = open(path,'r')
    write = open('Analysis\\providedSolution.py','w')
    for line in read:
        write.write(line)
    read.close()
    write.close()

def csvWrite(data:list[dict]):
    header = ["type","number","valid_answer","cyclomatic","code"]
    contains="result.csv" in os.listdir("Analysis")
    with open("Analysis\\result.csv",'a',newline='') as csvFile:
        writer = csv.DictWriter(csvFile,fieldnames=header)
        if not contains:
            writer.writeheader()
        writer.writerows(data)

            
            

def main()->None:
    folder="LLM\\aiResponeses"
    goThoughTest(folder)

if __name__=='__main__':
    main()