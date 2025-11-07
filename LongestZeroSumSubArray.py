def longest_subarray(arr):
    """
    Finds the length and elements of the longest subarray with a sum of zero.

    Args:
        arr (list of int): The input array of integers.

    Returns:
        tuple: A tuple containing:
            - max_length (int): The length of the longest subarray with sum zero.
            - longest_subarray (list of int): The longest subarray with sum zero.
    """
    max_length = 0
    sum_map = {}
    current_sum = 0
    start_index = -1  # To track the start index of the longest subarray

    for i in range(len(arr)):
        current_sum += arr[i]

        if current_sum == 0:
            max_length = i + 1
            start_index = 0  # Update start index to 0

        if current_sum in sum_map:
            if max_length < i - sum_map[current_sum]:
                max_length = i - sum_map[current_sum]
                start_index = sum_map[current_sum] + 1  # Update start index
        else:
            sum_map[current_sum] = i

    longest_subarray = arr[start_index:start_index + max_length] if max_length > 0 else []
    return max_length, longest_subarray

def main():
    print("Hello, World!")  # Added Hello World functionality
    my_array = [1,-5,5, 2, 3, 4, 5, 2, -2, 3, -3, 4, -4]  # Declare an array
    print(my_array)  # Print the array
    
    print("Longest subarray length:", longest_subarray(my_array))  # Print longest subarray length
    

if __name__ == "__main__":
    main()
