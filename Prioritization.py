

def prioritization(list_of_soldiers):
    n=len(list_of_soldiers)
    for i in range(n):
        for j in range(0, n - i - 1):
            Comparison_1=list_of_soldiers[j]
            Comparison_2=list_of_soldiers[j+1]
            if Comparison_1['distance_in_kilometers']+(Comparison_1['Family complexity']*30)<Comparison_2['distance_in_kilometers']+(Comparison_2['Family complexity']*30):
                list_of_soldiers[j],list_of_soldiers[j+1]=list_of_soldiers[j+1],list_of_soldiers[j]
    return list_of_soldiers


