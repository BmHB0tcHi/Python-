# GLOBAL VARS
history = [' ']
Capital_Letter_Symbol = '~'
max_buffer_lenght = 4
i = 0
prev_index = 0
#--------------------------

# Reads 4 Characters and Implements CLL
def ReadChars(max_buffer_lenght, Capital_Letter_Symbol):
    Chars = ''
    while len(Chars) < max_buffer_lenght:
        character = f.read(1)

        # Capital Letter Logic (CLL)
        if (character.isupper()):
            if((max_buffer_lenght - len(Chars)) >= 2):
                Chars = Chars + Capital_Letter_Symbol + character.lower()
            else:
                Chars = Chars + Capital_Letter_Symbol
        else:
            Chars = Chars + character
    return Chars


# adding 4 characters to our history
# aswell as incrementing i
def add_to_history(i, buffer):
    if i == 0:
        history[i] = buffer
        i+=1
        #print (history)
        return i
    elif i < 0:
        print ("Index Error!")

    elif i > 0:
        history.append(buffer)
        i+=1
        #print (history)
        return i

def print_manual():
    print (f'''
        Commands :
        --> "Read" : reads the next 4 characters from the file
        --> "Prev" : prints previously read characters
        --> "exit": exit the program\n
        --> "help": print manual
        --> 'list': print out the history list
        ''')

print_manual()


# Reacting to User input and acting accordingly
with open('readme.txt', 'r') as f:
    while True:

        userinput = input("Input:  ")
        if userinput.lower() == 'help':
            print_manual()

        if userinput.lower() == 'list':
            print (history)
        # rd = read
        # reads 4 characters
        if userinput.lower() == 'read':
            prev_index = i - 1
            buffer = ReadChars(max_buffer_lenght,Capital_Letter_Symbol)
            print (f"--- Read: {buffer}")
            i = add_to_history(i, buffer)

        #prv = Previously read Characters
        if userinput.lower() == 'prev':
            if prev_index < 0:
                print('Nothing aviablable')
                continue
            else:
                prev = history[prev_index]
                print (f"Prev = {prev}")
                #print (f"   {history}")
                prev_index-=1
                continue
        elif userinput.lower() == 'exit':
            print(f"List:\n  {history} ")
            print ("Program Exiting...")
            break


