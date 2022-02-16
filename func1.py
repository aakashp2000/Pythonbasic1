#recursive function to calculate the sum of numbers
def addition(num):
    if num:
        return num+addition(num-1)
    else:
        return 0
res=addition(15)
print(res)