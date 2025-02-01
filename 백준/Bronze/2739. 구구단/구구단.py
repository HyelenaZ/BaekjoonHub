try:
    n = int(input())  
    if not (1<=n<=9):
        raise ValueError
    for i in range(1,10):
        print(f'{n} * {i} = {n*i}') 
        
except ValueError:
    print("Invalid input")