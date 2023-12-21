# Question 1
die_a = [1, 2, 3, 4, 5, 6]
die_b = [1, 2, 3, 4, 5, 6]

total_combinations = len(die_a) * len(die_b)
print("Total no. of combinations: ", total_combinations)

# Question 2
distribution_matrix = [[0] * 6 for _ in range(6)]

for i in range(6):
    for j in range(6):
        distribution_matrix[i][j] = die_a[i] + die_b[j]

print("Distribution Matrix:")
for i in range(6):
    for j in range(6):
        print(distribution_matrix[i][j], end=" ")
    print()


# Question 3
sum_counts = [0] * (12+1)
for i in range(1, 7):
    for j in range(1, 7):
        sum_counts[i + j] += 1
# sum_counts = [0, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]

probabilities = []

print("\nProbability of Sums:")
for sum_val, count in enumerate(sum_counts):
    probability = count / total_combinations
    probabilities.append(probability)
    print(f"P(Sum = {sum_val}): {probability:.4f}")


