import pandas as pd

states = ['California', 'Texas', 'Florida', 'Newyork']
population = [39613493, 29730311, 21944577, 19299981]

print('Example 1 :')
dict_states = {'States': states, 'Population': population}
df_states = pd.DataFrame.from_dict(dict_states)
print(df_states)
#df_states.to_csv('states.csv', index=False)

print('\nExample 2 :')
print(states[-1])

print("\nExample 3 :")
for state in states:
    print(state)

print("\nExample 4 :")
for state in states:
    if state == "Florida":
        print(state)

#print("\nExample 4 :")
#with open('test.txt', 'w') as file:
#    file.write("Data succesfully scrapped!")

