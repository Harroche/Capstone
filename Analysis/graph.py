import pandas
import matplotlib.pyplot as plt
import os

class csvReader:
    def __init__(self,filepath:str):
        self.db=pandas.read_csv(filepath)
        self.col = ["key","valid_answer","cyclomatic","time_complexity","time"]
        self.name = filepath[filepath.rfind('/')+1:]
    
    def timeComplexityTotals(self):
        xAxis = ["N","NLogN","N^2"]
        yAxis = []
        for y in xAxis:
            yAxis.append(len(self.db[self.db[self.col[3]] == y]))
        plt.bar(xAxis,yAxis)

        plt.xlabel("X - Time Complexity")

        plt.ylabel("Y - Cumulative amount")

        plt.title(f"{self.name}\nCumulative distribution over Time complexity")

        plt.show()
    
    def timings(self):
        xAxis = [(0.0,10.0),(10.0, 100.0),(100.0,1000.0),(1000.0,10000.0),(10000.0,100000.0)]
        xDisplay = ["0.0 - 10.0","10.0 - 100.0","100.0 - 1000.0","1000.0 - 10000.0","10000.0 - 100000.0"]
        yAxis = []
        for lo, hi in xAxis:
            yAxis.append(len(self.db[(self.db[self.col[4]]> lo) & (self.db[self.col[4]]<hi)]))
        plt.figure(figsize=(10,5))

        plt.bar(xDisplay,yAxis)

        plt.xlabel("X - Time in ms")

        plt.ylabel("Y - Cumulative amount")

        plt.title(f"{self.name}\nCumulative amount time taken to complete dataset")

        plt.show()

    def timeToCyc(self):
        xAxis = ["N","NLogN","N^2"]
        barColor = ["green","orange","red"]
        yAxis = []
        for item in xAxis:
            yAxis.append(mean(self.db[self.db[self.col[3]] == item][self.col[2]]))
        
        plt.bar(xAxis,yAxis,color=barColor)
        plt.xlabel("X - Time Complexity")

        plt.ylabel("Y - Cyclomatic complexity")

        plt.title(f"{self.name}\nMean of the Cyclomatic complexity\n based on Time complexity")

        plt.show()
    
    def correctAnswersPie(self):
        labels = ["No Answer", "N","NLogN","N^2"]
        total = self.db[self.col[3]].isnull().sum()
        percent = [total]
        for i in range(1,4):
            amount = len(self.db[self.db[self.col[3]]== labels[i]])
            percent.append(amount)
        plt.pie(percent,labels=labels,autopct='%1.1f%%',startangle=140)

        plt.title(f"{self.name}\nDistribution of dataset")

        plt.show()
        
    def showAllGraphs(self):
        self.timeComplexityTotals()
        self.correctAnswersPie()
        self.timings()
        self.timeToCyc()

        
            
def mean(db:pandas.DataFrame)->float:
    return db.sum()/len(db)



def main()->None:
    obj = csvReader("Analysis/result.csv")
    obj.showAllGraphs()
    obj=csvReader("Analysis/twoSumStarter3_5.csv")
    obj.showAllGraphs()
    obj = csvReader("Analysis/twoSumStarter4o.csv")
    obj.showAllGraphs()
    # files=os.listdir("Analysis")
    # for file in files:
    #     if ".csv" in file:
    #         reader=csvReader(f"Analysis\\{file}")
    #         reader.showAllGraphs(file)

if __name__=='__main__':
    main()