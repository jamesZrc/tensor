
from datetime import date
# 函数
def xirr(cashflows):
    years = [(ta[0] - cashflows[0][0]).days / 365. for ta in cashflows]
    residual = 1.0
    step = 0.05
    guess = 0.05
    epsilon = 0.0001
    limit = 10000
    while abs(residual) > epsilon and limit > 0:
        limit -= 1
        residual = 0.0
        for i, trans in enumerate(cashflows):
            residual += trans[1] / pow(guess, years[i])
        if abs(residual) > epsilon:
            if residual > 0:
                guess += step
            else:
                guess -= step
                step /= 2.0
    return guess - 1


# 测试
data = [(date(2020, 1, 1), -100), (date(2020, 2, 14), -100), (date(2020, 3, 6), -100), (date(2020, 4, 3), -100),
        (date(2020, 5, 10), -100), (date(2020, 6, 23), -100), (date(2020, 7, 2), -100), (date(2020, 8, 25), -100),
        (date(2020, 9, 1), -100), (date(2020, 10, 3), -100), (date(2020, 11, 2), -100), (date(2020, 12, 6), -100),
        (date(2020, 12, 30), 1300)]
print(xirr(data))
