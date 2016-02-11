
import numpy

def closest_wharehouse(self, orders, wharehouses):
	
	closest_orders = {}
	# Finds the closest orders for wach wharehouse
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

	return closest_orders, exc_min

		