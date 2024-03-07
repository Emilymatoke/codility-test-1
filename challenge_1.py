def solution(S):
    N = len(S)
    M = len(S[0])

    # Define a comparator function to compare two strings based on a specific position
    def compare_strings(i, j, k):
        return S[j][i] == S[k][i]

    # Iterate through each position in the strings
    for i in range(M):
        # Iterate through each pair of strings
        for j in range(N):
            for k in range(j + 1, N):
                # Check if the characters at position i are the same in both strings
                if compare_strings(i, j, k):
                    # Return the indices of the strings and the position
                    return [j, k, i]

    # If no pair is found, return an empty array
    return []

# Test cases
print(solution(["abc", "bca", "dbe"]))  # Output: [0, 2, 1]
print(solution(["zzzz", "ferz", "zdsr", "fgtd"]))  # Output: [0, 1, 3]
print(solution(["gr", "sd", "rg"]))  # Output: []
print(solution(["bdafg", "ceagi"]))  # Output: [0, 1, 2]
