import matplotlib.pyplot as plt
        
def get_index(parts):

    if parts[1] == '1':
        if parts[0]== '1' or parts[0]=='2' or parts[0]=='3':
            return 0
        elif parts[0]== '4' or parts[0]=='5' or parts[0]=='6':
            return 1
        elif parts[0] == '7' or parts[0]=='8' or parts[0]=='9':
            return 2
    else:
        if parts[0]== '1' or parts[0]=='2' or parts[0]=='3':
            return 3
        elif parts[0]== '4' or parts[0]=='5' or parts[0]=='6':
            return 4
        elif parts[0] == '7' or parts[0]=='8' or parts[0]=='9':
            return 5

count = [0,0,0,0,0,0]
parts = []
file=open("marketingdata.txt","r")
for line in file:
     if 'NA' not in line :
        parts.append(line.strip().split())

for i in range(0,len(parts)):
    index = get_index(parts[i])
    count[index] = count[index] + 1    

print('\n')
print('Lower Income Male:\t',count[0])
print( 'Middle Income Male:\t',count[1])
print( 'Upper Income Male:\t',count[2])
print( 'Lower Income Female:\t',count[3])
print( 'Middle Income Female:\t',count[4])
print( 'Upper Income Female:\t',count[5])

names = ['Lower Income Male','Middle Income Male','Upper Income Male',
         'Lower Income Female','Middle Income Female','Upper Income Female']


fig = plt.figure()

fig.set_figheight(20)
fig.set_figwidth(20)

plt.subplot(2, 2, 1)
plt.bar(names, count, align='center', alpha=0.5)
plt.xticks(names, rotation=90)
plt.ylabel('Income')

plt.subplot(2, 2, 2)
plt.pie(count, labels=names, autopct='%1.1f%%',startangle=90)
plt.axis('equal')

plt.show()