while True:                                     #Asking user for all the values inside the while loop
    dollars=input('\nHow many US Dollars do you want to exchange?\n')
    currency=input('\nEnter the name of the currency you are converting dollars to:\n')
    rate=input('\nWhat is the exchange rate?\n')

    if rate.isdigit() and dollars.isdigit():    #checking that both value for dollars andrate are numeric value
        break
    else:                                       #if any of the value is string then asking user to re-enter all values
        print('Invalid input, Please enter a integer number:')
        continue

result= float(dollars) * float(rate)    #calculating result by converting all values to float
float(result)
print('\nConverted value is',result)    #printing result
