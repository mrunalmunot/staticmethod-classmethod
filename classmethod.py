import os
import sys

#Add Circle class implementation here
class Circle:
    count_of_circle=0
    def __init__(self, r):
        self.r = r
        Circle.count_of_circle+=1
    
    @classmethod
    def getCircleCount(cls):
        return cls.count_of_circle
    
    def area(self):
        return round(3.14*self.r*self.r, 2)
    
'''Check the Tail section for input/output'''

if __name__ == "__main__":
    with open(os.environ['OUTPUT_PATH'], 'w') as fout:
        res_lst = list()
        circcount = list()
        lst = list(map(lambda x: float(x.strip()), input().split(',')))
        for radi in lst:
            c=Circle(radi)
            res_lst.append(str(c.getCircleCount())+" : "+str(c.area()))
        fout.write("{}\n{}".format(str(res_lst), str(Circle.getCircleCount())))
