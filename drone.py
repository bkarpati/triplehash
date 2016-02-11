
import numpy
import input_parser as ip

def closest_wharehouse(self, orders, wharehouses):
	
	closest_orders = {}
	# Finds the closest orders for wach wharehouse
	orders = 
	for order in orders:
		L = []
		for wharehouse in wharehouses:
			L.append(numpy.linalg.norm(order.coordinate - wharehouse.coordinate))
		id = numpy.argmin(L)
		closest_orders[id].append(order)

	# Finds the order items for each wharehouse 
	for key, val in closest_orders.iteritems:
		items = [0]*wharehouse[key].length()
		for order in val:
			for item in order.item:
				items[item]+=1
		closest_orders[key] = items

	# Returns a dictionary with a tuple list of have and have not
	exc_min = {}
	for key, val in closest_orders.iteritems:
		need = []
		exc = []
		diff = [itW - itO for itW, itO in zip(wharehouse[key], val)]
		for i, num in enumerate(diff):
			if num<1:
				need.append((i, num*-1))# (product no, items required)
			elif num > 0:
				exc.append((i, num))
		exc_min[key] = (need, exc)

	return (closest_orders, exc_min)

def which_whearehouse(self, closest_orders, exec_min):
	# Wherehouse 

def main(self):
	input1 = ip.parse_input("busy_day.in")
	number_of_row = input1[0]
	number_of_col  = input1[1]
	number_of_drones = input1[2]
	max_sim_time = input1[3] 
	max_drone_load = input1[4] 
	total_product_type = input1[5] 
	weight_of_product = input1[6] 
	list_of_warehouses = input1[7] 
	total_customers = input1[8] 
	list_of_order = input1[9]

	tup1 = closest_wharehouse(list_of_order, list_of_warehouses 