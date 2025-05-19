from rich import print

upto: int = int(input("Fibonacci series upto: "))
initial_series: list[int] = [0, 1]

each_number: int
for each_number in initial_series:
    sumation = initial_series[-1] + initial_series[-2]
    if sumation <= upto:
        initial_series.append(sumation)
    else:
        break

print(", ".join(map(str, initial_series)) + ".")
