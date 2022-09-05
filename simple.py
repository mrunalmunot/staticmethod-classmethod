import os
import sys

#Add Circle class implementation below
class Circle:
    no_of_circles = 0
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        a = 3.14*self.radius*self.radius
        Circle.no_of_circles+=1
        return round(a,2)
    
'''Check the Tail section for input/output'''

if __name__ == "__main__":
    with open(os.environ['OUTPUT_PATH'], 'w') as fout:
        res_lst = list()
        lst = list(map(lambda x: float(x.strip()), input().split(',')))
        for radius in lst:
            res_lst.append(Circle(radius).area())
        fout.write("{}\n{}".format(str(res_lst), str(Circle.no_of_circles)))
