import random

def contagion_simulation(numbers, contagion_factor=0.5):
    # Copy the array to avoid in-place modification
    numbers = numbers[:]
    # Length of the array
    N = len(numbers)

    # First pass: adjusting all single numbers to match their neighbors
    for i in range(N):
        left_neighbor = numbers[i-1] if i-1 >= 0 else None
        right_neighbor = numbers[i+1] if i+1 < N else None

        if numbers[i] != left_neighbor and numbers[i] != right_neighbor:
            if left_neighbor is not None and right_neighbor is not None:
                numbers[i] = left_neighbor if abs(numbers[i] - left_neighbor) < abs(numbers[i] - right_neighbor) else right_neighbor
            elif left_neighbor is not None:
                numbers[i] = left_neighbor
            elif right_neighbor is not None:
                numbers[i] = right_neighbor

    # Second pass: contagion process
    for i in range(N):
        left_neighbor = numbers[i-1] if i-1 >= 0 else None
        right_neighbor = numbers[i+1] if i+1 < N else None

        if left_neighbor == numbers[i] or right_neighbor == numbers[i]:
            # Case of a number in a group
            group_size = 1
            # Count the size of the group to the left
            j = i - 1
            while j >= 0 and numbers[j] == numbers[i]:
                group_size += 1
                j -= 1
            # Count the size of the group to the right
            j = i + 1
            while j < N and numbers[j] == numbers[i]:
                group_size += 1
                j += 1
            # Based on the group size, decide if it spreads to the neighbors
            if random.random() < group_size / N * contagion_factor:
                if left_neighbor is not None and left_neighbor != numbers[i]:
                    numbers[i-1] = numbers[i]
                if right_neighbor is not None and right_neighbor != numbers[i]:
                    numbers[i+1] = numbers[i]

    return numbers



def check_errors(string):
    repeated_words = []
    current_word = ""
    current_count = 0
    word_count = len(string.split())

    if word_count < 500:
        raise SystemExit(f"Error with file - Word count only {word_count} Number of words is below 500. Exiting the script.")

    for word in string.split():
        if word == current_word:
            current_count += 1
        else:
            if current_count > 10:
                repeated_words.append(current_word)
            current_word = word
            current_count = 1

    if current_count > 10:
        repeated_words.append(current_word)

    if repeated_words:
        raise SystemExit(f"Error with file - Repeated words {repeated_words} found more than 10 times. Exiting the script.")




# numbers = [9, 3, 3, 3, 3, 10, 10, 10, 10, 10, 10, 4, 4, 4, 4, 12, 11, 11, 11, 12, 12, 12, 12, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 1, 1, 1, 1, 7, 7, 7, 8, 8, 8, 8, 7, 7, 0, 0, 0, 0, 0, 9, 9, 9, 9, 9, 2, 2, 14, 14, 14, 2, 13, 13]


# numbers = [9, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 8, 8, 8, 8, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 7, 7, 6, 6, 6, 6, 7, 7, 4, 4, 4, 4, 4, 9, 9, 9, 9, 9, 9, 2, 2, 2, 2, 5, 5, 5]


# print (numbers)
# print (contagion_simulation(numbers))



# Check if the file is being run directly
if __name__ == "__main__":
    # This code will only run if the file is executed directly
    contagion_simulation()




# chatgpt request

# The contagion_simulation() function modifies an array of numbers to simulate a contagion process. It first adjusts each number to match its neighboring values. Then, it iterates through the array and checks if a number is part of a group based on its neighbors. If so, it determines the group size by counting the adjacent numbers with the same value. The likelihood of spreading the number to its neighbors depends on the group size and a contagion factor. If the random contagion probability is met, the number spreads to its adjacent neighbors. Finally, the modified array is returned as the result of the simulation. The function allows for an optional contagion factor parameter, which influences the spread of the numbers. It avoids modifying the original array by creating a copy. The simulation operates in two passes, adjusting single numbers first and then applying the contagion process. Overall, the function provides a concise way to simulate the spread of values in an array based on neighbor interactions.



## implementation of the contagion_simulation
# # Attach cluster labels to result_list
# for i, result_dict in enumerate(data_list):
#     # result_dict['cluster_label'] = kmeans.labels_[i]
#     result_dict['cluster_label'] = rearranged_kmeans_labels[i]
# # print(data_list)
