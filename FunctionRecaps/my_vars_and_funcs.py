num_of_people = 100

counter = 1
def doubled(x):
    return x*2

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)