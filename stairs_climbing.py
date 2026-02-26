class  StairProblem:
    #constructor
    def __init__(self,n:int=0):
        self.n=n

    def __str__(self) -> str:
        return f'the number of stairs is {n}'

    def nb_ways(self)->int:
        l=[0]*(self.n+1)
        l[0]=1
        l[1]=1
        for i in range(2, self.n+1):
            l[i]=l[i-1]+l[i-2]
        return l[self.n]


#Create an instance
n:int=int(input('Enter the number of stairs : '))
st_pb=StairProblem(n)
print(st_pb)
print(f'number of possible ways is {st_pb.nb_ways():}')
