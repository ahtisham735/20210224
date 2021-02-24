from collections import defaultdict
import sys
mylist=[]
try:
	with open("input.txt") as data:
		cases=int(data.readline())
		for _ in range(cases):
			N=int(data.readline())
			mydict = defaultdict(set)
			for _ in range (N):
				line=data.readline()
				words=line.split()
				key=words.pop(0)
				name=''
				for n in words:			
					name=f'{name} {n}'
			
				mydict[key].add(name)
			mylist.append(mydict)
			
	with open('output.txt','a') as output:
		case=1
		for mydict in mylist:
			sortedkeys=sorted(mydict)
			output.write(f'case:{case}\n')
			case=case+1
			for key in sortedkeys:
				output.write(f'{key}:{len(mydict[key])}\n')
except FileNotFoundError:
	print("No Such file Exist in the specified directory")
except Exception as e:
	print(e.__class__)

	
	
		
