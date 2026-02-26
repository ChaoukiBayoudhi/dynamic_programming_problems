import random as rd
class HouseRobber:
    #constructor
    def __init__(self,nums:list[int]=[])->None:
        #private attributes
        self._nums=nums
        self._n=len(nums)

    #getters properties
    @property
    def nums(self)->list[int]:
        return self._nums

    @property
    def n(self)->int:
        return self._n

    #setters properties
    @nums.setter
    def nums(self,nums:list[int])->None:
        self._nums=nums

    @n.setter
    def n(self,n:int)->None:
        self._n=n

    #generate nums randomly
    def generate_house_profit(self,n:int)->None:
        for _ in range(n+1):
            self.nums.append(rd.randint(1,400))
        self.n=n
    def generate_house_profit_v2(self,n:int)->None:
        self.nums=[rd.randint(1,400) for _ in range(n+1)]
        self.n=n

    def solve(self)->int:
      
        dp=[0]*(self.n+1)
        dp[0]=0
        dp[1]=self.nums[0]
        for i in range(2,self.n+1):
            dp[i]=max(dp[i-1],dp[i-2]+self.nums[i-1])
        return dp[self.n]

    #solution with houses to rob as solution of the problem
    #solution in the form [0,1,0,1,...,0]
    def solve_v2(self)->list[int]:
        # handle small cases explicitly
        if self.n == 0:
            return []
        if self.n == 1:
            return [1]

        # same dp as in solve(), but we will reconstruct the chosen houses
        dp=[0]*(self.n+1)
        dp[0]=0
        dp[1]=self.nums[0]
        for i in range(2,self.n+1):
            dp[i]=max(dp[i-1],dp[i-2]+self.nums[i-1])

        # reconstruct the chosen houses: 1 = rob, 0 = skip
        result=[0]*self.n
        i=self.n
        while i>0:
            if dp[i]==dp[i-1]:
                result[i-1]=0
                i-=1
            else:
                result[i-1]=1
                i-=2
        return result


    def print_solution(self)->None:
        print(f"The maximum profit is {self.solve()}")


#create an instance
hr=HouseRobber()
n:int=int(input("Enter the number of houses: "))
hr.generate_house_profit_v2(n)
print(f"The profits of the houses to rob are {hr._nums}")
hr.print_solution()

#another example
nums=[2,7,9,3,1]
hr=HouseRobber(nums)
hr.solve()
hr.print_solution()

    