import os
import sys

#Add circle class implementation here
class Circle:
    n=0
    def __init__(self, r):
        Circle.n+=1
        self.r = r
        
    @staticmethod
    def getPi():
        return 3.14
    
    @classmethod
    def getCircleCount(cls):
        return Circle.n
    
    def area(self):
        return round(Circle.getPi()*self.r*self.r,2)
        
'''Check the Tail section for input/output'''

if __name__ == "__main__":
    with open(os.environ['OUTPUT_PATH'], 'w') as fout:
        res_lst = list()
        circcount = list()
        lst = list(map(lambda x: float(x.strip()), input().split(',')))
        for radi in lst:
            c=Circle(radi)
            res_lst.append(str(c.getCircleCount())+" : "+str(c.area()))
        fout.write("{}".format(str(res_lst)))
