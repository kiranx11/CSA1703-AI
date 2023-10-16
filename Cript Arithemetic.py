from itertools import permutations

def solve_cryptarithmetic(puzzle):
    letters = set("".join(puzzle)) 
    if len(letters) > 10:
        return None  

    for perm in permutations(range(10), len(letters)):
        digit_mapping = dict(zip(letters, perm))
        
        if all(digit_mapping[word[0]] != 0 for word in puzzle) and \
           sum(int("".join(str(digit_mapping[char]) for char in word)) for word in puzzle[:-1]) == int("".join(str(digit_mapping[char]) for char in puzzle[-1])):
            return digit_mapping

    return None
if _name_ == "_main_":
    puzzle = ["BASE", "BALL", "MONEY"]
    solution = solve_cryptarithmetic(puzzle)
    if solution:
        print("Solution found:")
        for word in puzzle:
            print(f"{word} = {''.join([str(solution[char]) for char in word])}")
    else:
        print("No solution found.")
