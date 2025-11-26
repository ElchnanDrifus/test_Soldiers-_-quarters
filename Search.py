def Search(List_after_insertion):
    print('Enter personal number')
    personal_number=int(input())
    for i in List_after_insertion:
        if i['personal_number']==personal_number:
            placement_status =i['placement_status']
            if placement_status==True:
                return 'Already assigned for residence'
            else:
                return 'On the waiting list'
    return 'The number is not in the system'


