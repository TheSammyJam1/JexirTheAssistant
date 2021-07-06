def domylaundry():
    yn = input('Do You Think I am Your Servant?!?!\ny/n\n')
    inq = 'you should type "y" or "n"'
    if yn == 'y':
        inq = 'im not sure what ' + str(input('Why\nI am incapable\n')) + ' means'
    if yn == 'n':
        inq = 'im not sure what ' + str(input('Good.\nThen why did you choose 3\n')) + ' means'
    print(inq)
