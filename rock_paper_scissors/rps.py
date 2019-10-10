#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    core = ["rock", "paper", "scissors"]
    results = []

    def looper(cycles, temp_result=[]):

        if cycles < 1:
            print(f"temp: {temp_result}")
            return results.append(temp_result)
        else:
            for v in core:
                print(f"v: {v}")
                looper(cycles - 1, temp_result + [v])

    looper(n)
    return results


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
