w1=[1,-1,1,-1]
w2=[1,1,-1,-1]
a1=input("Enter Data 1 = ")
a2=input("Enter Data 2 = ")
d1=[]
d2=[]
for i in a1:
	d1.append(int(i))
for i in a2:
	d2.append(int(i))
sumw1 = []
sumw2 = []
for j in range(len(d1)):
	temp=[]
	for i in range(len(w1)):
		temp.append(w1[i]*d1[j])
	sumw1.append(temp)
for j in range(len(d2)):
	temp=[]
	for i in range(len(w2)):
		temp.append(w2[i]*d2[j])
	sumw2.append(temp)
fin = []
for i in range(len(sumw1)):
	temp=[]
	for j in range(len(w1)):
		temp.append(sumw1[i][j]+sumw2[i][j])
	fin.append(temp)

print("D1.W1 + D2.W2 = ")
print(fin)
te=0
temp2=[]
for j in range(len(fin)):
	te=0
	for i in range(len(w1)):
		te+=fin[j][i]*w1[i]
	temp2.append(te//len(w1))
te1=0
temp3=[]
for j in range(len(fin)):
	te1=0
	for i in range(len(w1)):
		te1+=fin[j][i]*w2[i]
	temp3.append(te1//len(w2))
b=int(input("Enter Which data you want to retrive - 1 or 2 ?"))

if b==1:
	print(temp2)
elif b==2:
	print(temp3)
else:
	print("Enter Valid Data")




