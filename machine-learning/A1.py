import pandas as pd 
import numpy as np 


pk = pd.read_csv('pokemons.csv')

# Problem 1

n = len(pk)
pk.loc[(pk['Name'] == "Farfetch'd"), 'Legendary'] = True

# Problem 2
print('For Problem 2: \n')
def maxhp():
    sorting_Descending = pk.sort_values(by='HP', ascending = False)
    print('The Name of the strongest Pokemon is : ' +str(sorting_Descending.iloc[0,1]))

maxhp()

# Problem 3
print('For Problem 3: \n')
pk['Total Attack'] = pk['Attack'] + pk['Sp. Atk']
print(pk.head())




#Problem 4
print('For Problem 4: \n')
smart_pokemons = pk.groupby('Type 1').filter(lambda pk : pk['Sp. Def'].mean() > 80.)
print(smart_pokemons.head())

#Problem 5 
smart_pokemons.to_csv('smart_pokemons.csv', index =  True, header = True)