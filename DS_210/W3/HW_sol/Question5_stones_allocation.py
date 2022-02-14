def throw_stones(N, M):
    """
    N: Number of stones (N>=1)
    M: Number of days (M>=1)
    """
    # TODO:
    results = []
    throw_stone_helper2(M, N, 1, [], results)
    return results


def throw_stone_helper2(days, n, current_day, history, val):
    if current_day > days:
        if n == 0:
            val.append(history)
        return
    if n <= 0:
        return

    if current_day % 2 == 0:
        history_new = history[:]
        history.append(1)
        history_new.append(3)

        throw_stone_helper2(days, n-1, current_day+1,history, val)
        throw_stone_helper2(days, n-3, current_day + 1, history_new, val)
    else:
        history_new1 = history[:]
        history_new2 = history[:]
        history_new1.append(1)
        history_new2.append(2)
        history.append(3)

        throw_stone_helper2(days, n-1, current_day+1, history_new1, val)
        throw_stone_helper2(days, n-2, current_day+1, history_new2, val)
        throw_stone_helper2(days, n-3, current_day+1, history, val)



def main():
    print(throw_stones(N=5,
                       M=3))  # Expect: [(1, 1, 3), (1, 3, 1), (2, 1, 2), (3, 1, 1)] or [[1, 1, 3], [1, 3, 1], [2, 1, 2], [3, 1, 1]]
    print(throw_stones(N=6, M=2))  # Expect: [(3, 3)] or [[3, 3]]


if __name__ == '__main__':
    main()