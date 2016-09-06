class Restaurant:

	restaurantId = 0
	menu = []	#list of Item objects

	def __init__(self, restaurantId, menu):
		self.restaurantId = restaurantId
		self.menu = menu
