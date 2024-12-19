from itertools import product



def maximize_expression(K, M, lists):
    max_value = 0
    # Iterate over all combinations of elements from each list
    for combination in product(*lists):
        # Compute the sum of squares of the chosen elements
        sum_of_squares = sum(x**2 for x in combination)
        # Take modulo M
        max_value = max(max_value, sum_of_squares % M)
    return max_value



if __name__ == "__main__":
    K, M = map(int, input().rstrip().split())

    lists = [list(map(int, input().rstrip().split()[1:])) for _ in range(K)]

    result = maximize_expression(K, M, lists)
    print(result)
