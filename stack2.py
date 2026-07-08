stack = []
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)

# Python evaluates expressions from left to right.
#  When you separate expressions with commas like this, 
# Python executes them in order and bundles the results together 
# into a structure called a Tuple (which uses parentheses ()).

store = stack.pop(), stack.pop(), stack.pop() 
print(store)
stack.append(70)
stack.append(80)
print(stack)