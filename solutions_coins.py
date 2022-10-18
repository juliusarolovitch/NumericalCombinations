import math
import random
import time
from matplotlib import pyplot

# Julius Arolovitch, October 17th 2022, For Use Under License

# Function takes two inputs, the dollar value and an array of bills
def Calculate_Solutions(n, c):
    maximum_values = []
    solutions = {}
    solutions_found = 0
    x = []
    y = []
    for i in c:
        maximum_values.append(math.floor(n/i))
    end_time = time.time() + 5
    time_now = time.time()
    combinations_tried = 0
    while time.time() < end_time:
        try_values = []
        pending_sum = 0
        for j in range(0, len(c)):
            try_values.append(random.randint(0, maximum_values[j]))
        for k in range(0, len(c)):
            pending_sum += try_values[k] * c[k]
        if pending_sum == n:
            if try_values not in solutions.values():
                solutions[str(solutions_found)] = try_values
                solutions_found += 1
                y.append(solutions_found)
                x.append(time.time())
        combinations_tried +=1
        print(f"{combinations_tried} {try_values} {solutions_found}.")
        
    print(solutions)
    print(f"The total solutions found is {solutions_found}.")
    pyplot.xlim(time_now, time.time())
    pyplot.ylim(0, solutions_found + 10)
    pyplot.grid()
    pyplot.plot(x, y, marker="o", markersize=2, markeredgecolor="red")
    pyplot.title("Distinct Solutions Found Over Time")
    pyplot.xlabel("Time (s)")
    pyplot.ylabel("Solutions found")
    pyplot.rcParams["figure.figsize"] = [7.00, 3.50]
    pyplot.rcParams["figure.autolayout"] = True
    pyplot.show()
    
coins = [1, 2, 3, 4]
Calculate_Solutions(20, coins)




