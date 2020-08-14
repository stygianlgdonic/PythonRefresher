# Declare a variable and initialize it
my_var = 120
print(my_var)

# # re-declaring the variable works
my_var = "this is reassigned"
print(my_var)

# # ERROR: variables of different types cannot be combined
# print("Hello " + 123)
print("Hello " + "123")

# Global vs. local variables in functions
def someFunction():
    # global f
    f = "fucntion variable"
    print(f)


someFunction()
print(f)  # for this to work declare f variable as global in someFunction()

del f
print(f)
