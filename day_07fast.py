# copy data to test.txt and in.txt
# aliases in terminal: 'aot' for test, 'aos' for puzzle input, 'aoc' to run both

# extremely fast following the solution by https://hyperneutrino.xyz/
# conditions are nested for stepwise explanations, but they can also be one-liners

def refactor(res: int, nums: list, p2: bool) -> bool:
    if len(nums) == 1: return res == nums[0]

    if res % nums[-1] == 0:                             # res is result of something * last number
        if refactor(res // nums[-1], nums[:-1], p2):    # check for something and remaining numbers
            return True

    if res - nums[-1] > 0:                              # res is result of something + last number
        if refactor(res - nums[-1], nums[:-1], p2):     # check for something and remaining numbers
            return True

    if not p2: return False

    if str(res).endswith(str(nums[-1])):            # str(res) = something + str(nums[-1])
        cut = str(res).rindex(str(nums[-1]))        # most right idx where last number starts
        if cut > 0:                                 # at least one digit before last number
            something = int(str(res)[:cut])         # part of res that completes with last number to res
            if refactor(something, nums[:-1], p2):  # check for something and remaining numbers
                return True

    return False


part1 = part2 = 0
data = open(0)
# with open("test.txt", "r") as f: data = f.readlines()
# with open("in.txt", "r") as f: data = f.readlines()

for line in data:
    result, numbers = line.split(":")
    result = int(result)
    numbers = list(map(int, numbers.split()))
    part1 += result * refactor(result, numbers, False)
    part2 += result * refactor(result, numbers, True)

print(part1)  # 4364915411363
print(part2)  # 38322057216320
