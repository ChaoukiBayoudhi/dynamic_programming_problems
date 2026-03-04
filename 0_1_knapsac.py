import random as rd
class KnapsacPb:
    def __init__(self,weights:list[int],profits:list[int],capacity:int):
        self.n=len(weights)
        self.weights=weights
        self.profits=profits
        self.capacity=capacity
    def generate_pb_inputs(self):
        self.n=rd.randint(1,100)
        self.capacity=rd.randint(1,1000)
        for i  in range(self.n):
            self.weights.append(rd.randint(1,100))
            self.profits.append(rd.randint(1,100))

    def generate_pb_inputs_v2(self):
        self.n=rd.randint(1,100)
        self.capacity=rd.randint(1,1000)
        
        self.weights=[rd.randint(1,100) for _ in range(self.n)]
        self.profits=[rd.randint(1,100) for _ in range(self.n)]
    #fill the matrix (n+1)x(capacity+1)
    #n+1 rows and capacity+1 columns
    def fill_dp_matrix(self)->list[list[int]]:
        #fill the matrix with zeros
        
        dp=[[0]*(self.capacity+1) for _ in range(self.n+1) ]
        #...

    