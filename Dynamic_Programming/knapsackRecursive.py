def knapsack(weights, values, capacity, n):
    if n == 0 or capacity == 0:
        return 0

    if weights[n - 1] > capacity:
        return knapsack(weights, values, capacity, n - 1)

    include = values[n - 1] + knapsack(
        weights, values,
        capacity - weights[n - 1],
        n - 1
    )

    exclude = knapsack(weights, values, capacity, n - 1)

    return max(include, exclude)


weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

print(knapsack(weights, values, capacity, len(weights)))