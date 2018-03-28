allItemsEntered = False
items = []

while not allItemsEntered:
	
	item = input("Insert price of item numer {}, or a 0 if you are finished: ".format(len(items) + 1))

	if item.isdigit(): 
		item = float(item)
	else:
		print("You've entered an invalid price! Try again")
		continue

	if item == 0:
		allItemsEntered = True
	elif item < 0:
		print("You've entered an invalid price! Try again")
		continue
	else:
		items.append(item)

print('Number of items: {}'.format(len(items)))
for n,i in enumerate(items):
	print('Price of item {}: ${}'.format(n, items[n]))

total = 0
for i in items:
	total += i

if total > 100:
	total *= .9

print('Total price for 3 items is ${}'.format(total))

while True:
	pass

