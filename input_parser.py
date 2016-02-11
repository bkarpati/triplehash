

#product type start with 
#
#parameters of the simulation
number_of_rows = 0
number_of_col = 0
number_of_drones = 0
max_sim_time = 0
max_drone_load = 0

#weights of the product available for order
total_product_type = 0
weight_of_product = list()

#
def parse_input(fileName):
	op = open(fileName, "rb")
	line  = op.readline()

	print(line)
	op.close()
	


