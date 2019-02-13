def rental_car_cost(days):
  cost = 40 * days
  if days >= 7:
   	cost -= 40
  elif days >=3:
    cost -= 20
  return cost

rental_car_cost(4)