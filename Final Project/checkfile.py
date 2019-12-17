# Author: ---

# check out data files

# enter the filename, usually .txt or .csv file

# The program will count the number of lines in the file, 
#   and print the first 5 lines in the file.

linecount = 0

filename = input('Enter file name: ', encoding='utf8')
file = open(filename)
for line in file:
    linecount +=1
    if linecount <= 5:
        print (line)

print ('The file has ', linecount, ' lines.')

# end