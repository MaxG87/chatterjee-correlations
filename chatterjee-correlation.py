import math
import random as rnd


def chatterjee(X: list[float], Y: list[float]) -> float:
    as_tuples = list(zip(X, Y, strict=True))
    as_tuples.sort(key=lambda x: x[0])
    y_ranks = get_ranks(Y)

    intermediate = 0
    for (_, y_cur), (_, y_succ) in zip(as_tuples[:-1], as_tuples[1:], strict=True):
        rank_cur = y_ranks[y_cur]
        rank_succ = y_ranks[y_succ]
        intermediate += abs(rank_succ - rank_cur)

    corr_coeff = 1 - 3 * intermediate / (len(X) ** 2 - 1)
    return corr_coeff


def get_ranks(items: list[float]) -> dict[float, int]:
    sorted_items = sorted(items)
    ranks = {item: n for n, item in enumerate(sorted_items)}
    return ranks


if __name__ == "__main__":
    N = 1000
    X = [rnd.random() for i in range(1000)]
    for func in [
        math.sin,
        math.cos,
        math.tan,
        math.asin,
        math.acos,
        math.atan,
        round,
        lambda x: x**2,
        lambda x: 1 / x,
        lambda x: rnd.random(),
    ]:
        Y = [func(x) for x in X]
        print(func.__name__, chatterjee(X, Y))
