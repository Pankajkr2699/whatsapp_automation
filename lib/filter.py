class Data():
    def number(self):
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

        return number 
    
    def message(self):
        print('Press Enter for a seperate message and :e for exit')
        message = []
        i = "1"
        while i=="1":
            text = input('')
            if text!=":e":
                message.append(text)
            else: 
                break 
        
        return message 
    
    

