# String Similarity Calculation using Edit Distance

def edit_distance(str1, str2):
    n = len(str1)
    m = len(str2)

    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1

            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + cost
            )

    return dp[n][m]


def similarity_percentage(str1, str2):
    distance = edit_distance(str1, str2)
    max_len = max(len(str1), len(str2))

    similarity = 1 - (distance / max_len)
    return similarity * 100


text1 = input("Enter first text: ")
text2 = input("Enter second text: ")

percent = similarity_percentage(text1, text2)

print("\nSimilarity Percentage:", round(percent, 2), "%")
