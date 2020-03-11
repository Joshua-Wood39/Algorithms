#!/usr/bin/python

import argparse


def find_max_profit(prices):
    i = 0
    j = 1
    profit = 0
    temp = 0
    while i < len(prices) - 1:
        while j <= len(prices) - 1:
            print(f'i: {prices[i]}, j: {prices[j]}')
            if temp == 0:
                profit = 0 - prices[i] + prices[j]
            temp = 0 - prices[i] + prices[j]
            if temp > profit:
                profit = temp
                print(profit)

            j += 1

        i += 1
        j = i + 1

        print(f'profit: {profit}')
    return profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
