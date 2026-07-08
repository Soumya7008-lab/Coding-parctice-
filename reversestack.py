def reverse(input_word):
    my_stack = []
    
    # Step 1: Push every letter of the word onto the stack
    for letter in input_word:
        my_stack.append(letter)
    
    reversed_word = ""
    
    # Step 2: Pop letters one by one until the stack is empty
    # len(my_stack) checks how many items are left in the stack
    while len(my_stack) > 0:
        captured_letter = my_stack.pop()
        reversed_word = reversed_word + captured_letter
        
    return reversed_word

# Let's test it!
original = "HELLO"
result = reverse(original)

print("Original Word:", original)
print("Reversed Word:", result)