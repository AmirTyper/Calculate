def calculate():
    operation = input('''
Script By @Mr_Amir_Typer
========================
----Wich one?----
[]+
[]-
[]*
[]/
[]** (Tavan) (Power)
----Choose---- = ''')
    nb1 = float(input('---Number One = '))
    
    nb2 = float(input('--Number Two = '))

    if operation == '+' :
        print('')
        print('')

        print(

            '''Answer :''',nb1+nb2)
        print('''



''')

    elif operation == '-' :
        print('')
        print('')

        print(

            '''Answer :''',nb1-nb2)
        print('''



''')

    elif operation == '*' :
        print('')
        print('')

        print(

            '''Answer :''',nb1*nb2)
        
        print('''



''')

    elif operation == '/' :
        print('')
        print('')

        print(

            '''Answer :''',nb1/nb2)
        print('''



''')
    elif operation == '**' :
        print('')
        print('')

        print(

            '''Answer :''',nb1**nb2)
        print('''



''')
    
    else:
        print('')
        print('')

        print('Wrong Choose!')
        print('''



''')

    again()

def again():
    clc_again = input('''
=======================
[*]Again?

[*]Y or N

[*]Choose = ''')
    if clc_again == 'Y':
        calculate()

    elif clc_again == 'N':
        print('''

========================
[Bye Friend! <3 | Script By @Mr_Amir_Typer]
========================

''')

    else:
        again()
        
calculate()








    

    
