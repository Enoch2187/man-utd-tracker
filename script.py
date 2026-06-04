

my_list = ['sister', 'in', 'arms']
for _ in my_list:
    print(_, end=" ")



a_stuff = 12 % 2 == 0 or 12 % 3 == 0
print(a_stuff)


def show_output():
    top = 7
    count = 0
    total = 0
    for bottom in range(0, top + 1, 2):
        count += 1
        total += top + bottom
    print("count:", count, "total:", total)

show_output()