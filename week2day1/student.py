class Student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def getHighest(self):
        return max(self.marks)
    def getLowest(self):
        return min(self.marks)
    def getAvg(self):
        return sum(self.marks)/len(self.marks)
    def addMarks(self,sub,marks):
        self.marks[sub-1]=self.marks[sub-1]+marks
stu1=Student("john",[80,90,100,75])

print(stu1.getAvg())
print(stu1.getHighest())
print(stu1.getLowest())
print(stu1.addMarks(1,10))
print(stu1.marks)