#Handling exception errprs: Try-except
print('Handling exception errors: Try-except')
new_list = [2,4,6, 'California']
for element in new_list:
    try:
        print(element/2)
    except:
        print('The element is not a number!')

#While-break
print('\nWhile-break 1 :')
n = 4
while n > 0:
    print(n)
    n = n-1
print('Message')

print('\nWhile-break 2:')
n = 4
while n > 0:
    print(n)
    n = n-1
    if n == 2:
        break
print('Loop ended')