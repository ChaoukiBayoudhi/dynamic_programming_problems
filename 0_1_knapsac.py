import random as rd


class KnapsacPb:
    def __init__(
        self, weights: list[int] = [], profits: list[int] = [], capacity: int = 0
    ):
        self.n = len(weights)
        self.weights = weights
        self.profits = profits
        self.capacity = capacity
        self.solution = [0] * self.n

    def generate_pb_inputs(self):
        self.n = rd.randint(1, 100)
        self.solution = [0] * self.n
        self.capacity = rd.randint(1, 1000)
        self.weights = []
        self.profits = list()
        for i in range(self.n):
            self.weights.append(rd.randint(1, 100))
            self.profits.append(rd.randint(1, 100))

    def generate_pb_inputs_v2(self):
        self.n = rd.randint(1, 100)
        self.solution = [0] * self.n
        self.capacity = rd.randint(1, 1000)

        self.weights = [rd.randint(1, 100) for _ in range(self.n)]
        self.profits = [rd.randint(1, 100) for _ in range(self.n)]

    # fill the matrix (n+1)x(capacity+1)
    # n+1 rows and capacity+1 columns
    def fill_dp_matrix(self) -> list[list[int]]:
        # fill the matrix with zeros

        dp = [[0] * (self.capacity + 1) for _ in range(self.n + 1)]
        for i in range(1, self.n + 1):
            for w in range(1, self.capacity + 1):
                """x=0
                if w>=self.weights[i-1]:
                    x=dp[i-1][w-self.weights[i-1]]+self.profits[i-1]
                dp[i][w] = max(
                    dp[i - 1][w],
                    x
                )"""
                # one liner version
                """dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - self.weights[i - 1]] + self.profits[i - 1] if w>=self.weights[i-1] else 0
                )"""
                # using logical operators
                dp[i][w] = max(
                    dp[i - 1][w],
                    w >= self.weights[i - 1]
                    and dp[i - 1][w - self.weights[i - 1]] + self.profits[i - 1]
                    or 0,
                )
        return dp

    def print_dp_matrix(self, matrix: list[list[int]]) -> None:
        for i in range(self.n + 1):
            for j in range(self.capacity + 1):
                print(matrix[i][j], end="\t")
            print()

    def solve(self):
        dp = self.fill_dp_matrix()
        w = self.capacity
        for i in range(self.n, 0, -1):
            if dp[i][w] != dp[i - 1][w]:
                self.solution[i - 1] = 1
                w -= self.weights[i - 1]


# main
kps_pb: KnapsacPb = KnapsacPb([1, 3, 4, 5], [1, 4, 5, 7], 7)
dp: list[list[int]] = kps_pb.fill_dp_matrix()
kps_pb.print_dp_matrix(dp)
kps_pb.solve()
print(f"The solution is {kps_pb.solution}")

# test the random generation
kps_pb = KnapsacPb()
kps_pb.generate_pb_inputs_v2()
# print the generated values
print(
    f"n={kps_pb.n}\ncapacity={kps_pb.capacity}\nweights={kps_pb.weights}\nprofits={kps_pb.profits}"
)
kps_pb.solve()
print(f"The solution is {kps_pb.solution}")

