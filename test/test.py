'''
countrycode = input('Enter Country Code : +')
countrycode = countrycode.strip()
print('Please Enter 10 digit number Only')
tempNumber = input('Numbers  {Comma seperated} : ').split(',') 
number = []

# Formating Number 
for i in tempNumber: 
    x = i.strip()
    x = countrycode+x 
    # checking right number Formate 
    if len(x)==12:
        number.append(int(x))
    else: 
        print(f'{x} wrong Number')
    
    

'''


