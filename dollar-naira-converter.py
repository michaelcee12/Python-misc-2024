# toSeconds = 20*34

# print (F'there are {toSeconds} days now !!!')

# Using functions and parameters in python 


#Simple currency converting program in python

oneNaira = 1629

def dollarToNaira(dollar):
    convert = f"${dollar} is equivalent to NGN{dollar*oneNaira}"
    return convert
 
def validate_and_execute():
    try:
        number = int(element)
        if number > 0:
            calc_value = dollarToNaira(number)
            print(calc_value)
        elif number == 0:
            print ("Enter a number greater than 0")
        else:
            print ('Negative number, try again')
    except:
        print('Your input isn\'t a digit')

userInput = ''
while userInput != 'exit':  
    userInput = input('How many dollars do you want to convert? (Type "exit" to quit)\n')
    if userInput.lower() == 'exit':
        break 
    for element in userInput.split(','):
        validate_and_execute()




