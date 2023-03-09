first_element = int(input("enter the first element: "))
difference = int(input("enter difference: "))
list_lenght =int(input("enter list lenght: "))
my_progression = []
my_progression.append(first_element)
for i in range(1, list_lenght):
    my_progression.append(first_element + i*difference)


print(my_progression)