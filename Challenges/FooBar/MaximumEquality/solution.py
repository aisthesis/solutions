def answer(x):
    n_cars = len(x)
    n_rabbits = sum(x)
    if n_rabbits % n_cars == 0:
        return n_cars
    return n_cars - 1
