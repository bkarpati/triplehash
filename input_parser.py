

#product type start with 
#
#parameters of the simulation
number_of_row = 0
number_of_col = 0
number_of_drones = 0
max_sim_time = 0
max_drone_load = 0

#weights of the product available for order
total_product_type = 0
weight_of_product = list()

#warehouses and availability of individual product type
total_warehouse = 0
list_of_warehouses = list() #is a list of WareHouses


#Customer orders:
total_customers = 0

def parse_input(fileName):
	file_object = open(fileName, "rb")
	simulation_param  = file_object.readline()
	
	parse_param(simulation_param.split())
	
	file_object.close()
	
def parse_param(simulation_params):
	global number_of_row, number_of_row, number_of_drones, max_sim_time, max_drone_load
	number_of_row = int(simulation_params[0])
	number_of_col = int(simulation_params[1])
	number_of_drones = int(simulation_params[2])
	max_sim_time = int(simulation_params[3])
	max_drone_load = int(simulation_params[4])


class WareHouse():

	def __init__(self):
		self.id = None
		self.x_pos = None
		self.y_pos = None
		self.item_available = None
		self.list_of_product = list()


class Customer_order():

	def __init__(self):
		self.customer_id = None
		self.total_ordered_product = None
		self.list_of_orders = list()
