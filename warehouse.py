

class WareHouse():

	def __init__(self, id, pos):
		self.id = id
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.item_available = None
		self.list_of_product = list()

	def set_list_of_product(self,list_of_product):
		total_product = len(list_of_product)
		for i in range(0, total_product):
			product_value = int(list_of_product[i])
			self.list_of_product.append(product_value)

class Customer_order():

	def __init__(self,id,total_ordered_product,pos):
		self.customer_id = id
		self.total_ordered_product = total_ordered_product
		self.list_of_orders = list()
		self.x_pos = pos[0]
		self.y_pos = pos[1]

	def set_list_of_order_product(self, list_of_orders):
		total_product = len(list_of_orders)
		for i in range(0, total_product):
			product_value = int(list_of_orders[i])
			self.list_of_orders.append(product_value)
		
class Order():

	def __init__(self):
		self.id = None
