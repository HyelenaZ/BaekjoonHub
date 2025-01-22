def bc_year(y):
    try:
        assert 1000<= y <= 3000, "불기연도 유효범위가 아님"
        return y - 543
    except (AssertionError, ValueError) as e:
        return str(e)

y = int(input())
print(bc_year(y))