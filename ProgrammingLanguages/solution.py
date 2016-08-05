import csv
import sys
import itertools

class Restaurant:

	restaurantId = 0
	menu = []	#list of Item objects

	def __init__(self, restaurantId, menu):
		self.restaurantId = restaurantId
		self.menu = menu


class Item:
	label = []
	price = 0.0

	def __init__(self, label, price):
		self.label = label
		self.price = price



def main():

	myMenu = [x.strip() for x in sys.argv[2:]]
	restaurantDict = csvParser(sys.argv[1])
	suitableRestaurants = findSuitableRestaurants(restaurantDict, myMenu)

	if len(suitableRestaurants) == 0:
		print "Nil"
		exit(0)

	bestRestaurant, minPrice = findPerfectRestaurant(suitableRestaurants, myMenu)
	print bestRestaurant, minPrice


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



def printRestaurantMap(restaurantDict):
	for restaurant in restaurantDict:
		print restaurantDict[restaurant].restaurantId

		for item in restaurantDict[restaurant].menu:
			print item.price
			print item.label


def findSuitableRestaurants(restaurantDict, myMenu):

	suitableRestaurants = []

	for restaurant in restaurantDict:

		menuFlag = [0 for item in myMenu]
		
		currentRestaurant = restaurantDict[restaurant]
		menu = currentRestaurant.menu


		for menuItem in menu:
			common = set(menuItem.label).intersection(set(myMenu))

			for commonItem in common:
				menuFlag[myMenu.index(commonItem)] = 1

		if all([flag == 1 for flag in menuFlag]):
			suitableRestaurants.append(currentRestaurant)

	return suitableRestaurants


def findPerfectRestaurant(suitableRestaurants, myMenu):

	restPriceCombo = []

	for restaurant in suitableRestaurants:
		allMenuItems = []
		priceOfMenuItems = []

		for menuItem in restaurant.menu:
			allMenuItems.append(menuItem.label)
			priceOfMenuItems.append(menuItem.price)

		max_price = sys.maxsize

		for length in range(0, len(allMenuItems) + 1):
			for subset in itertools.combinations(allMenuItems, length):
				mergedItems = []
				price = 0

				for item in subset:
					price = price + priceOfMenuItems[allMenuItems.index(item)]
					mergedItems = mergedItems + item

					if len(set(mergedItems).intersection(set(myMenu))) == len(myMenu) and price < max_price:
						max_price = price

		restPriceCombo.append((restaurant.restaurantId, max_price))


	minPrice = restPriceCombo[0][1]
	bestRestaurant = restPriceCombo[0][0]

	for combo in restPriceCombo:
		if combo[1] < minPrice:
			minPrice = combo[1]
			bestRestaurant = combo[0]

	return (bestRestaurant, minPrice)


if __name__ == "__main__":
	main()