## Dynamic Programming Problems (2BIS1)

This mini-project contains **simple, well-structured implementations of classic dynamic programming problems** used in the 2BIS1 problem solving course.

The goal is to:

- **Illustrate the DP mindset** (optimal substructure, overlapping subproblems).
- **Contrast recursive thinking with bottom‑up tabulation.**
- Provide **clean, reusable Python examples** you can adapt in assignments and exams.

### Contents

- **`house_robbing.py`**  
  - Implements the classic *House Robber* problem.  
  - Uses a `HouseRobber` class that:
    - Randomly generates profits for a street of houses.
    - Computes the maximum profit without robbing two adjacent houses (bottom‑up DP).
    - Optionally reconstructs which houses to rob as a binary list (1 = rob, 0 = skip).

- **`fibonacci.py`**  
  - Demonstrates different ways to compute Fibonacci numbers (e.g. naive recursion vs DP).
  - Highlights why memoization / tabulation are much more efficient.

- **`stairs_climbing.py`**  
  - Models the classic “climbing stairs” problem (number of ways to reach the top with small steps).
  - Shows how a simple recurrence leads to an efficient DP solution.

> Note: The exact implementations may evolve over time as we refine examples in class.

### How to Run the Examples

All programs are standard Python scripts and require **Python 3.10+** (for type hints like `list[int]`).

From the project root of this repository:

```bash
cd dynamic_programming_problems
```

- **Run the House Robber example:**

```bash
python house_robbing.py
```

You will be prompted to:

- Enter the number of houses.
- The script will then:
  - Randomly generate profits for each house.
  - Print the profits list.
  - Print the maximum profit obtainable without robbing adjacent houses.

Other scripts are run in the same way:

```bash
python fibonacci.py
python stairs_climbing.py
```

### Pedagogical Notes

- **State definition**: Clearly identify what each DP state represents.  
  Example (House Robber):  
  \( dp[i] = \) maximum profit using the first \( i \) houses.

- **Transition**: Write an explicit recurrence before coding.  
  Example:  
  \( dp[i] = \max(dp[i-1],\ dp[i-2] + \text{profit of house } i) \)

- **Base cases**: Always handle small inputs carefully (e.g. 0 or 1 house).

- **Reconstruction**: When possible, show how to **reconstruct a solution**, not only its value  
  (e.g. which houses to rob, which steps to take).

These examples are intentionally **compact and readable** so you can focus on the reasoning process, not on framework or boilerplate code.

### Suggested Exercises

- Modify `house_robbing.py` to:
  - Forbid robbing three houses in a row instead of two.
  - Introduce a limit on the total number of houses you are allowed to rob.
- Extend `stairs_climbing.py` to allow variable step sets (e.g. steps of size 1, 3, or 5).
- Implement a **top‑down (recursive + memoization)** version for each problem and compare performance.

### License

Feel free to use these examples for **learning and teaching purposes**.  
If you reuse them in your own materials, a short attribution is appreciated but not required.

