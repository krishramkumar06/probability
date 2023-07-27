def all_permutations(nums):
    if len(nums) == 0:
        return [[]]  # Base case: If the list is empty, return a list containing an empty list (representing an empty permutation)
    else:
        last_elt = nums[-1]  # Get the last element from the list
        prev_permutations = all_permutations(nums[:-1])  # Recursively find permutations of n - 1 elements (excluding the last element)
        curr_perms = []  # List to store final permutations

        for perm in prev_permutations:
            for i in range(len(perm) + 1):  # Iterate over all possible positions to insert the last element
                new_perm = perm[:i] + [last_elt] + perm[i:]  # Create a new permutation with the last element inserted at position i
                curr_perms.append(new_perm)  # Add the new permutation to the list of current permutations

        return curr_perms  # Return the list of all permutations

yusuf = [1, 2, 3]
print(all_permutations(yusuf))  # Call the function with the input list [1, 2, 3] and print the result
