budget = input("Enter the budget:").strip()
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    dishes = {}
    items_ratio = {}
    max_calories = 0
    for key, value in items.items():
        items_ratio[key] = round(value["calories"] / value["cost"], 2)
    sorted_items = sorted(items_ratio.items(), key=lambda x: x[1], reverse=True)
    while budget >= (min(items.values(), key=lambda x: x["cost"])["cost"]):
        for item in sorted_items:
            if budget >= items[item[0]]["cost"]:
                budget -= items[item[0]]["cost"]
                max_calories += items[item[0]]["calories"]
                if item[0] in dishes:
                    dishes[item[0]] += 1
                else:
                    dishes[item[0]] = 1
    return budget, max_calories, dishes


def dynamic_programming(items, budget):
    dp = [0] * (budget + 1)
    choice = [None] * (budget + 1)
    for item, value in items.items():
        cost = value["cost"]
        calories = value["calories"]
        for b in range(budget, cost - 1, -1):
            if dp[b] < dp[b - cost] + calories:
                dp[b] = dp[b - cost] + calories
                choice[b] = item
    b = budget
    dishes = {}

    while b > 0 and choice[b] is not None:
        item = choice[b]
        if item in dishes:
            dishes[item] += 1
        else:
            dishes[item] = 1
        b -= items[item]["cost"]
    

    return b, dp[budget], dishes
  
    
try:
    budget = int(budget)
    b_greedy, max_calories_greedy, dishes_greedy = greedy_algorithm(items, budget)
    b_dynamic, max_calories_dynamic, dishes_dynamic  = dynamic_programming(items, budget)
   
    if dishes_greedy:
        print("\nGreedy Algorithm Result:")
        print(f"Maximum calorie content: {max_calories_greedy}")
        print(f"Selected dishes: {dishes_greedy}")
        print(f"Budget left: {b_greedy}")
    if dishes_dynamic:
        print("\nDynamic Programming Result:")
        print(f"Maximum calorie content: {max_calories_dynamic}")
        print(f"Selected dishes: {dishes_dynamic}")
        print(f"Budget left: {b_dynamic}")
except ValueError:
    print("Please anter a valid budget")