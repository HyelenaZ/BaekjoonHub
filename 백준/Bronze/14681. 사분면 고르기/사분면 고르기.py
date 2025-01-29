try:
    x = int(input())
    y = int(input())
    if not (-1000<=x<=1000 and x!=0) and (-10000<y<=1000 and y!=0):
        raise ValueError

    def quadrant(x, y):
        if x>0:
            return 1 if y>0 else 4
        else:
            return 2 if y>0 else 3

    print(quadrant(x, y))

except ValueError:
    print("Invalid input")