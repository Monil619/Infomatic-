n1=0
count=1
n2=0
n3=0

file_control= open('marketingdata.txt')
print("\nThese are the first fifteen lines in the file with no NA in it:\n")
for line1 in file_control:
    if "NA" not in line1:
        n1=n1+1
        if count<= 15:
            count=count+1
            print(line1.strip())
print("\nThe file has", n1 ,"lines with no NA in it\n")


file_control2= open("NYC-CitiBike-2016.csv")
for line2 in file_control2:
    n2=n2+1
    if "9/29/16" in line2:
        n3=n3+1
print("The file has", n2, "lines, of which" ,n3 ,"are from 9/29/16")
if n1> n2:
    print("The first file is larger than second one")
else:
    print("The first file is smaller that second one")
