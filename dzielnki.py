tab=[]
def factors(x):
    for i in range(1, x + 1):
        if x % i == 0:
            tab.append(i)
            print(i)


# take input from the user
num = int(input("Enter a number: "))
print(num )
print("The factors of",num,"are:")
print('vertical list')
factors(num)
print('horizontal list')
print(tab)