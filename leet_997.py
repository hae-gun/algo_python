class Vertex:
    def __init__(self, label):
        self.label = label

    def show(self):
        return self.label


class Graph:
    def __init__(self):
        self.in_degree = list()
        self.out_degree = list()

    def get_in_degree(self):
        return self.in_degree

    def get_out_degree(self):
        return self.out_degree

var1 = Vertex(10)
print(var1.show())

# class Solution:
#    def findJudge(self, n: int, trust: List[List[int]]) -> int:
