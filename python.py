print(len('GITHUB tutorial'))


def access_to_club(age):
    if age > 17:
        return ('enter') 
    elif age == 0:
        return ('access')
    else: 
       return('no access') 


user_input = input('hey user enter any age for access grant\n')
user_input_number = int(user_input)

age = access_to_club(user_input_number)
print(age)