from art import logo


#initiliaze global variable
CONT = True


#addition
def add(n1, n2):
  return n1 + n2

#subtraction
def subtract(n1, n2):
  return n1 - n2

#multiplication
def multiply(n1, n2):
  return n1 * n2

#division
def divide(n1, n2):
  return n1 / n2


#global variable located here because python does not support hoisting
#dictionary with relevant key/value pairs
OPERATIONS = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}


def calculator():
    '''This is the main and only function in this program.'''
    global CONT
    print(logo)
    #first query
    one = float(input('What\'s the first number?\n ~ '))
    for symbol in OPERATIONS:
        print(symbol)

    #separate first query from loop. if user wishes to continue queries with result this allows said functionality
    while CONT:
        choice = input('Pick an operation.\n ~ ')
        two = float(input('What\'s the second number?\n ~ '))
        get_symbol = OPERATIONS[choice]
        result = get_symbol(one, two)
        
        print(f'{one} {choice} {two} = {result}')

        #if user wishes to continue with current value follow this logic
        if input(f'Type "yes" to continue calculating with {result} or type "no" to start a new calculation.\n') == 'yes':
            one = result
        else:
            #start a new loop or catch KeyboardInterrupt on exit
            CONT = False
            try:
                calculator()
            except KeyboardInterrupt:
                print('\nSee you later.')


#initialize calculator functionality
try:
    calculator()

except KeyboardInterrupt:
    print('\nSee you later.')