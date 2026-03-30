#supplies = ['a', 'b', 'c', 'd']
#for i in range(len(supplies)):
 #   print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

my_pets = ['zophie', 'pooka']
print('enter a pet name: ')
name = input()
if name not in my_pets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet')
