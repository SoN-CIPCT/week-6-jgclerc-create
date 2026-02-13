web_users = ['Kelsolth', 'GrKitty', 'Quacky', 'TurdTed', 'BullyBill', 'Seamour']
new_users = ['TurdTed', 'BullyBill', 'Mary', 'Lonnie', 'Debby']

for user_name in new_users:
    if user_name in web_users:
        print(user_name.title ( ) + ' This user name is already in use. Please choose a different user name.')
    else:
        print(user_name.title() + ' The user name is available.')

cities = { }
cities['Madrid'] = {'Country': 'Spain', 'Population': 3400000, 'Fact': 'Madrid has the oldest restaurant, Sobrino de Botin, founded in 1725.'}
cities['London'] = {'Country': 'England', 'Population': 8800000, 'Fact': 'Four world heritage sites are located in London.'}
cities['Prague'] = {'Country': 'Czech Republic', 'Population': 1400000, 'Fact': 'It was founded in the 8th century.'}
print(cities)