animals=['zebra','tiger','lion','jackal','kangaroo']
print(animals[2])
ages=['25','34','54','12','23']
animals[2]='peacock'
print(animals[2])
for index, a in enumerate(animals):
	print(index,a)
ages[2:5]=[24,32,12] #sets items 2 to 5 with values 24,25,32
for index, a in enumerate(ages):
	print(index,a)
ages[2:5]=[]
for index, a in enumerate(ages):
	print(index,a)