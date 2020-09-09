def rental_car_cost(d: int) -> int:
    """Gives out the total amount for different count days of rent car."""
    cost = d * 40
    if d >= 7:
        cost -= 50
    elif d >= 3:
        cost -= 20
    return cost


print(rental_car_cost(1))
print(rental_car_cost(4))
print(rental_car_cost(7))
print(rental_car_cost(8))
