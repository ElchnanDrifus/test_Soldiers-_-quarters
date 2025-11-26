def Filing_an_appeal():
    print("Here you can appeal")
    print('Choose the correct option.')
    print("You were kicked out of your house due to the draft and you don't even have a place to sleep, one click.")
    print('If you are sleeping at home but there is distress at home, press two.')
    print('If, from too much travel and buses and trains, you dream at night about buses and trains, press three.')
    print('Another reason click four')
    print('Please click on the desired number.')
    Selection_key=int(input())
    for i in range(1,4):
        if i==Selection_key:
            print('Your request has been received and will be processed as soon as possible.')
    if Selection_key==4:
        print('Please write your request.')
        turn=input()
        print('Your request has been received and will be processed as soon as possible.')

