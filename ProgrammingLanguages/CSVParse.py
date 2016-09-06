import csv

from Restaurant import Restaurant
from Item import Item

def csvParser(filename):

	restaurantDict = {}

	with open(filename) as csvfile:
		csvreader = csv.reader(csvfile)

		for row in csvreader:
			restaurantId = int(row[0])
			price = float(row[1])
			label = [x.strip() for x in row[2:]]

			try:
				restaurant = restaurantDict[restaurantId]
			except:
				restaurant = Restaurant(restaurantId, [])
				restaurantDict[restaurantId] = restaurant

			item = Item(label, price)
			restaurant.menu.append(item)

	return restaurantDict
