#Hello, thank you for looking at my project. There are a few things I would like to point out:
#This is the New York Times project and the program needs the txt file to work.
#Specifically under the name bestsellers2

#My partner dropped the course before he could begin to do his share of the work
#Therefore I completed 100% of this project by myself, and I ask you to take this into consideration when grading :)
#Thank You!

###PLEASE PLACE THE GIVEN "BESTSELLERS2.TXT" TEXT FILE INTO THE SAME FOLDER AS THIS PROGRAM###


#Function to find the books between a certain year range

def yearfinder(txt, start, end):
    books = [ ]
    start = int(start)
    end = int(end)
    for i in txt:
        i = i.lstrip().rstrip()
        i = i.split('\t')                                   # splits lines in txt file
        if len(i) > 1:
            x = i[3].split('/')                             # splits the date by „/„ to get the year of book
            x = x[2]
            x = int(x)
            if x in range(start, end+1):                    # checks if year is in given range
                title_ = ''
                t = i[0]
                for letter in t:
                    if letter.isupper():
                        title_ += ' '                       # adding spaces between words
                        title_ += letter
                    else:
                        title_ += letter

                aut = ''
                a = i[1]
                for letter in a:
                    if letter.isupper():
                        aut += ' '                          # adding spaces between words
                        aut += letter
                    else:
                        aut += letter
                books.append(f'    {title_}, by {aut} ({i[3]})')

    if len(books) == 0:                                           # checks if there are any matching books
        print('No books for this year range')
    else:
        print('All Titles between', start, 'and', end, 'are:')
        for book in books:
            print(book)



#Function to find a book with a specific month and year

def monthfinder(txt, y, m):
    books = []
    for i in txt:
        i=i.lstrip().rstrip()
        i=i.split('\t')
        if len(i) > 1:
            x = i[3].split('/')                               # splits date to get month and year
            year = x[2]
            month = x[0]
            year = int(year)
            month = int(month)
        if month == int(m) and year==int(y):                  # checks if year and month are matching
            title_ = ''
            t = i[0]
            for letter in t:
                if letter.isupper():
                    title_ += ' '                            # adding spaces between words
                    title_ += letter
                else:
                    title_ += letter

            aut = ''
            a = i[1]
            for letter in a:
                if letter.isupper():
                    aut += ' '
                    aut += letter
                else:
                    aut += letter
            books.append(f'    {title_}, by {aut} ({i[3]})')

    if len(books) == 0:                                      # checks if there are any matching books
        print('There are No books for month', m, 'of', y)
    else:
        print('All Titles in month', m, 'of', y, ':')
        for book in books:
            print(book)




#Function to search for author no matter the case

def authorsearch(txt, author):
    books = []
    for i in txt:
        i=i.lstrip().rstrip()
        i = i.split('\t')
        if len(i) > 1:
            b = str(i[1])
            if author.lower() in b.lower():                 # checks if author names match in lower case
                title_ = ''
                t = i[0]
                for letter in t:
                    if letter.isupper():
                        title_ += ' '                        # adding space before a capital letter to display properly
                        title_ += letter
                    else:
                        title_ += letter                     # adding the letter in the string

                aut = ''
                a = i[1]
                for letter in a:
                    if letter.isupper():
                        aut += ' '                           # adding spaces between words
                        aut += letter
                    else:
                        aut += letter
                books.append(f'    {title_}, by {aut} ({i[3]})')

    if len(books) == 0:                                          # checks if there are any matching books
        print('No Books for this author')
    else:
        for book in books:
            print(book)



#Function to search by title no matter the case

def titlesearch(txt, title):
    books = []
    for i in txt:
        i = i.lstrip().rstrip()
        i = i.split('\t')
        if len(i) > 1:
            b = str(i[0])
            if title.lower() in b.lower():                  # checks if book titles match in lower case
                title_ = ''
                t = i[0]
                for letter in t:
                    if letter.isupper():
                        title_ += ' '                       # adding space before a capital letter to display properly
                        title_ += letter
                    else:
                        title_ += letter

                aut = ''
                a = i[1]
                for letter in a:
                    if letter.isupper():
                        aut += ' '
                        aut += letter
                    else:
                        aut += letter
                books.append(f'    {title_}, by {aut} ({i[3]})')

    if len(books) == 0:                                          # checks if there are any matching books
        print('No Books for this title')
    else:
        for book in books:
            print(book)




#Menu function, user inputs & calling on the other functions

def menu():
    print('\nWhat would you like to do?')
    print('1: Look up year range.')
    print('2: Look up month and year.')
    print('3: Look up Author.')
    print('4: Look up Name.')
    print('Q: Quit\n')


while True:                                            # loop to ask for correct user input
    menu()                                             # prints the main menu
    option = input('Choose: ')
    if option == '1':                                  # checks if selected option is 1
        while True:
            start = input('Enter starting year: ')
            if start.isnumeric():
                break                                  #exception for when the input is not a number
            else:
                print('Invalid input, please enter a number')
        while True:
            end = input('Enter ending year: ')
            if end.isnumeric():
                break
            else:
                print('Invalid input, please enter a number')

        txt = open('bestsellers2.txt', 'r')            # opens text file
        yearfinder(txt, start, end)                    # calls the year range finder function
        txt.close()
    elif option == '2':                                # checks if selected option is 2
        while True:
            y = input('Enter Desired Year: ')
            if y.isnumeric():
                break
            else:
                print('Invalid input, please enter a number')

        while True:                                             # checks if entered month is valid
            m = input('Entire Desired Month: ')                 # asks user for desired year
            if m.isnumeric():
                if 0 < int(m) < 13:
                    break
                else:
                    print('Month should be between 1 and 12')
            else:
                print('Invalid input, please enter a number')

        txt = open('bestsellers2.txt', 'r')
        monthfinder(txt, y, m)                                            # calls month and year finder function
        txt.close()
    elif option == '3':                                                   # checks if selected option is 3
        author = input('Enter author name (or part of name): ')
        txt = open('bestsellers2.txt', 'r')
        authorsearch(txt, author)                                         # calls search by author function
        txt.close()
    elif option == '4':                                                   # checks if selected option is 4
        title = input('Enter title of book (or part of title): ')
        txt = open('bestsellers2.txt', 'r')
        titlesearch(txt, title)                                           # calls search by title function
        txt.close()
    elif option.lower() == 'q':                                           # checks if option is Q
        print('\nThanks for Using this program!')
        break
    else:
        print('Invalid input. Please enter Valid option.')


#To start the program automatically
menu()