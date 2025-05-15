from rich import print
# i am going to write a fibonacci series upto "range"
""" 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 """

upto = int(input("Fibonacci series upto: "))
initial_series = [0,1]

for _ in initial_series:
    sumation = initial_series[-1] + initial_series[-2]
    if sumation <= upto:
        initial_series.append(sumation)
    else:
        break

print(", ".join(map(str, initial_series)) + ".")