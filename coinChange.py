def coin_change(coins):
    coin_dict = {
        'quarters': 0,
        'dimes': 0,
        'nickles': 0,
        'pennies': 0,
    }

    change = 0

    while coins >= 25:
        change = 25
        coin_dict['quarters'] += 1
        coins -= change
    while coins >= 10:
        change = 10
        coin_dict['dimes'] += 1
        coins -= change
    while coins >= 5:
        change = 5
        coin_dict['nickles'] += 1
        coins -= change
    while coins >= 1:
        change = 1
        coin_dict['pennies'] += 1
        coins -= change

    return coin_dict


print(coin_change(99))