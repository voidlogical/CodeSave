import time


# def rec_mc(coin_value_list, change, known_result):
#     min_coins = change
#     if change in coin_value_list:
#         known_result[change] = 1
#         return 1
#     elif known_result[change] > 0:
#         return known_result[change]
#
#     else:
#         for i in [c for c in coin_value_list if c <= change]:
#             num_coins = 1 + rec_mc(coin_value_list, change - i, known_result)
#             if num_coins < min_coins:
#                 min_coins = num_coins
#                 known_result[change] = min_coins
#         return min_coins


def dp_make_change(coin_value_list, change, min_coins):
    for cents in range(1, change + 1):
        coin_count = cents
        for j in [c for c in coin_value_list if c <= cents]:
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
        min_coins[cents] = coin_count
    return min_coins[change]


print(dp_make_change([1, 5, 10, 21, 25], 63, [0]*64))


# a = time.time()
# print(a)
# print(rec_mc([1, 5, 10, 25], 63, [0]*64))
# b = time.time()
# print(b)
# print(b - a)
# 1588316042.452156
# 6
# 1588316079.5932806
# 37.14112448692322