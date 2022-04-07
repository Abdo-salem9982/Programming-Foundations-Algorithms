# use recursion to implement a countdown counter


def countdown(x):
    if x == 0:
        print("Done!")
        return
    else:
        print(x, "...")
        countdown(x-1)


countdown(5)


# Output ====>  
# 5 ...
# 4 ...
# 3 ...
# 2 ...
# 1 ...
# 0 ...
# Done!
# foo
# foo
# foo
# foo
# foo
