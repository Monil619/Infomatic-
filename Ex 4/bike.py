def print_details(data = []):

    for i in range(0,30):
        avg_list.append(data[i][3])
        avg_list[i]=float(avg_list[i])
        pass24.append(data[i][7])
        pass24[i]=int(pass24[i])
    sum24=sum(pass24)
    average = sum(avg_list)/30
    
    print("\nThe following data is from",data[0][0],"to",data[len(data)-1][0],":")
    print("\nThe average miles:", average)
    print("Total number of pass purchased:", sum24)
    
def Sort(sub_list): 
    sub_list.sort(key = lambda x: x[1]) 
    return sub_list 



#txt file

file=open('citi_bike.txt')

data = []
avg_list=[]
pass24 = []

for line in file:
    parts = line.strip().split()
    data.append(parts)

print_details(data)

sorted = Sort(data)
print('top 5 day with highest no. of trips:')
for i in range(5):
    print (sorted[i][0])
    
# CSV file

file1= open('citi_bike.csv')
data = []
avg_list=[]
pass24 = []

for line in file1:
    parts = line.strip().split(',')
    data.append(parts)

print_details(data)

sorted = Sort(data)
print('top 5 day with highest no. of trips:')
for i in range(5):
    print (sorted[i][0])
    
    
print("\nThis is the end of the files processing")
