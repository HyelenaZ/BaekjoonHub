##### 240115 : CALCULATE mean & median
number_lst = [int(input()) for _ in range(5)]
number_lst.sort()

def calculate_stats(numbers):
    mean = sum(numbers)/len(numbers)
    median = sorted(numbers)[len(numbers)//2]
    return mean, median

mean, median = calculate_stats(number_lst)
print(int(mean))
print(median)