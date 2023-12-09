def get_permutations(sequence):
    out = []
    # This is the trivial case
    if len(sequence) == 1:
        return sequence
    else:
        for i, let in enumerate(sequence):
            # Let out be the previous index value,
            # and then the next index value
            for perm in get_permutations(sequence[:i] + sequence[i + 1:]):
                # Let out be the letter and the return value of permutation
                out += [let + perm]
    return out


if __name__ == '__main__':
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))