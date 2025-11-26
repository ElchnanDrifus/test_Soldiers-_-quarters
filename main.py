from data import list_of_soldiers
from Prioritization import prioritization
from Apartment_placement import Apartment_placement
from Search import Search
from Filing_an_appeal import Filing_an_appeal

print(f'list of soldiers {list_of_soldiers}')

Sorted_by_priority=prioritization(list_of_soldiers)
print(f'Sorted by priority {Sorted_by_priority}')

List_after_insertion=Apartment_placement(Sorted_by_priority)
print(f'List after insertion {List_after_insertion}')

Search=Search(List_after_insertion)
print(Search)

if Search=='On the waiting list':
    print('In urgent cases, an appeal can be filed.')
    print('To file an appeal, press one digit.')
    print('If no appeal is needed, click on any other number.')
    appeal=input()
    if appeal=='1':
        Filing_an_appeal=Filing_an_appeal()








