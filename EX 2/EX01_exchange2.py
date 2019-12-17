# Author:       MyName
# Description:  This program is to calculate the amount of currency that
#               the user can get with the amount of foriegn currency he/she
#               holds and the current exchange rate for that currency.
#               
#               The output is simply the amount he/she can get.

while True:
    print
    dollar_amount = input("How many US Dollars do you want to exchange? - Type the value or 'done' to exit: ")
    if dollar_amount == 'done':
    	print ('\nThanks for using this tool!\n')
    	break

    # checking if the input is numeric. If not it will start the whole loop again
    try:
        float(dollar_amount)
    except:
        print ('\n---wrong input: please enter numbers only---')
        continue

    #  asking for currency name
    currency_name = input('Enter the name of the currency you are converting dollars to: ')

    #  asking for conversion rate
    conversion_rate = input('What is the exchange rate? ')

    # checking if the input is numeric. If not it will start the whole loop again
    try:
        float(conversion_rate)
    except:
        print ('\n---wrong input: please enter numbers only---')
        continue

    #  calculating the conversion
    conversion_value = float(dollar_amount) * float(conversion_rate)

    print ('\n---You can exchange', dollar_amount, ' U.S. dollars for', conversion_value, currency_name)
