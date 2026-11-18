# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first):
    #   Save each number's index and check whether its complement was seen earlier.
    seen = {}
    for j, number in enumerate(nums):
        needed = target - number
        if needed in seen:
            return [seen[needed], j]
        seen[number] = j


def max_profit(prices):
    # Outline:
    #   Track the lowest price so far and the best profit from selling each day.
    if len(prices) < 2:
        return 0

    lowest_price = prices[0]
    best_profit = 0
    for price in prices[1:]:
        best_profit = max(best_profit, price - lowest_price)
        lowest_price = min(lowest_price, price)
    return best_profit


def max_subarray(nums):
    # Outline:
    #   Extend the current contiguous sum or start a new one at each number.
    current_sum = best_sum = nums[0]
    for number in nums[1:]:
        current_sum = max(number, current_sum + number)
        best_sum = max(best_sum, current_sum)
    return best_sum


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   Keep opening brackets in a stack and match each closing bracket to the latest
    #   opening bracket.
    matching_open = {")": "(", "]": "[", "}": "{"}
    stack = []
    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in matching_open:
            if not stack or stack.pop() != matching_open[char]:
                return False
    return not stack


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass


if __name__ == "__main__":
    main()
