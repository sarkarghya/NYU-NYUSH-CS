def purchase_combination_helper(Y_cost, cur_credit, min_spend, prefix, i, j, results, X):
    # boundary case for i
    if i == len(Y_cost):
        # We are done.
        # prefix should contain a combination choice. Now check if the prefix is eligible
        if len(prefix) == len(Y_cost) and cur_credit >= 0 and cur_credit <= X-min_spend:
            results.append(prefix)
        return

    # boundary case for j
    if j == len(Y_cost[i]):
        if len(prefix) == i:
            # This means that some item was picked
            purchase_combination_helper(Y_cost, cur_credit, min_spend, prefix, i + 1, 0, results, X)
        return

    # we are considering type i, brand j
    if Y_cost[i][j] <= cur_credit:
        # pick this item, and move to the next type (i+1, j=0)
        # print(i,j, Y_cost[i][j])
        purchase_combination_helper(Y_cost, cur_credit - Y_cost[i][j], min_spend, prefix + (j,), i + 1, 0, results, X)
    # skip item as an alternative path
    purchase_combination_helper(Y_cost, cur_credit, min_spend, prefix, i, j + 1, results, X)


def purchase_combination(Y_cost, X, Z):
    results = []
    purchase_combination_helper(Y_cost, X, Z, (), 0, 0, results, X)
    return results


def main():
    Y_cost = [[1,5], [2,4,3,6]]
    X = 12
    Z = 9
    print(purchase_combination(Y_cost, X, Z)) # Expect: results = [(1,1), (1,3)]


if __name__ == "__main__":
    main()