from random import randint
list_length = int(input("enter massiv length:"))
my_list = [randint(0, 20) for _ in range(list_length)]
print(my_list)
min = int(input("enter minimal:"))
max = int(input("enter maximal: "))
index_list = []
for i in range(list_length):
    if min <= my_list[i] <= max:
        index_list.append(i)
if index_list:
    print(f"elements in range from {min} to {max} have indexes:", "\n", index_list)
else:
    print("are not required elements")
