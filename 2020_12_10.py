from collections import defaultdict

def get_adapters(path):
    with open(path) as f:
        adapters = [int(x) for x in f.read().strip().split('\n')]
    final_adapter = max(adapters) + 3
    adapters.append(final_adapter)
    return adapters

def find_distribution(adapters):
    distribution = defaultdict(int)
    sorted_adapters = sorted(adapters)
    actual_joltage = 0
    for adapter in sorted_adapters:
        diff = adapter - actual_joltage
        distribution[diff] += 1
        actual_joltage = adapter
    return distribution

def is_a_solution(sol, original_chain):
    return sol[-1] == original_chain[-1]

def find_candidates(sol, original_chain, i):
    n = len(original_chain)
    last_adapter = sol[-1]
    ret = []
    for i in range(i+1, n):
        x = original_chain[i]
        if x - last_adapter < 4:
            ret.append(i)
        else:
            break
    return ret

def backtrack(sol, original_chain, i):
    if is_a_solution(sol, original_chain):
        return 1
    else:
        indices = find_candidates(sol, original_chain, i)
        ret = 0
        for j in indices:
            candidate = original_chain[j]
            ret += backtrack(sol + [candidate], original_chain, j)
        return ret

def get_disconnected_groups(chain):
    n = len(chain)
    zip3 = zip(range(1,n), chain, chain[1:])
    l = 0
    groups = []
    for r, x0, x1  in zip3:
        if x1 - x0 == 3:
            groups.append(chain[l:r])
            l = r
    groups.append(chain[l:])
    return groups

def count_arrangements(chain):
    x0 = chain[0]
    return backtrack([x0], chain, 0)

if __name__ == "__main__":
    path = "2020_12_10.input"
    adapters = get_adapters(path)
    distribution = find_distribution(adapters)
    keys = distribution.keys()
    if all([x < 4 for x in keys]):
        onejoltdiffs = distribution[1]
        threejoltdiffs = distribution[3]
        prod = onejoltdiffs * threejoltdiffs
        print("The number of 3 jolt diffs. multiplied by the number of 1 jolt diffs. is {}".format(prod))
    else:
        print("Cannot connect all adapters to make a chain")
        print(distribution)

    chain = [0] + sorted(adapters)
    groups = get_disconnected_groups(chain)

    total_arrangements = 1
    for g in groups:
        total_arrangements *= count_arrangements(g)
    print("The total number of chains that connect the source with my laptop are {}".format(total_arrangements))
