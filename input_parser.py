from warehouse import WareHouse, Customer_order 

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
list_of_order = list()


def parse_input(fileName):
	file_object = open(fileName, "rb")
	simulation_param  = file_object.readline()
	
	#parses the simulation parameters
	parse_param(simulation_param.split())

	#parsing total product and weight of products
	product = file_object.readline()
	global total_product_type, weight_of_product
	total_product_type = int(product) 
	all_products = file_object.readline()
	parse_product(all_products.split())
	#print(weight_of_product,"after parsing products_weight")
	
	#parsing warehouses and availability
	global total_warehouse, list_of_warehouses
	no_warehouse = file_object.readline()
	total_warehouse = int(no_warehouse)
	parse_warehouse(file_object)
	#print(list_of_warehouses[0].id ,": Yes : ")

	#parsing customer orders
	global total_customers, list_of_order
	no_customers = file_object.readline()
	total_customers = int(no_customers)
	parse_customer_order(file_object)
	#print("customers",list_of_order[0])

	file_object.close()

'''
This function sets the simulation parameters
'''
def parse_param(simulation_params):
	global number_of_row, number_of_row, number_of_drones, max_sim_time, max_drone_load
	number_of_row = int(simulation_params[0])
	number_of_col = int(simulation_params[1])
	number_of_drones = int(simulation_params[2])
	max_sim_time = int(simulation_params[3])
	max_drone_load = int(simulation_params[4])

'''
This function parses the products weights
'''
def parse_product(all_products):
	global weight_of_product, total_product_type
	
	for i in range(0, total_product_type):
		weight_of_product.append(int(all_products[i]))

'''
This function parses the warehouses and creates the warehouse
'''
def parse_warehouse(file_object):
	global total_warehouse, list_of_warehouses
	for i in range(0, total_warehouse):
		position = (file_object.readline()).split()
		x_pos = int(position[0])
		y_pos = int(position[1])
		pos = (x_pos, y_pos)
		wareHouse_object = WareHouse(i, pos)
		item_in_warehouse = file_object.readline()
		wareHouse_object.set_list_of_product(item_in_warehouse.split())
		list_of_warehouses.append(wareHouse_object)


'''
This function parses the customer orders
'''
def parse_customer_order(file_object):
	global total_customers, list_of_order
	for i in range(0, total_customers):
		position = (file_object.readline()).split()
		x_pos = int(position[0])
		y_pos = int(position[1])
		total_product = file_object.readline()
		total_product = int(total_product)
		pos = (x_pos,y_pos)
		customer_object = Customer_order(i,total_product,pos)
		item_ordered = file_object.readline()
		customer_object.set_list_of_order_product(item_ordered.split())
		list_of_order.append(customer_object)