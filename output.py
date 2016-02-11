
class Event():

	def __init__(self, id, command):
		self.drone_id = id
		#command must be a string
		self.command = command


class Load_event(Event):
	
	def __init__(self, id, warehouse_id,product_id, total_product):
		self.drone_id = id
		self.command = "L"
		self.warehouse_id = warehouse_id
		self.product_id = product_id
		self.total_product = total_product
		#super(Load_event, self.id, self.command)

	def __str__(self):
		line = str(self.drone_id)
		line += " " + self.command
		line += " " + str(self.warehouse_id)
		line += " " + str(self.product_id)
		line += " " + str(self.total_product)
		return line

class Deliver_event(Event):
	def __init__(self, id, customer_id, product_id,total_product):
		self.drone_id = id
		self.command = "D"
		self.customer_id = customer_id
		self.product_id = product_id
		self.total_product = total_product
		#super(Deliver_event, self.id, self.command)

	def __str__(self):
		line = str(self.drone_id)
		line += " " + self.command
		line += " " + str(self.customer_id)
		line += " " + str(self.product_id)
		line += " " + str(self.total_product)
		return line		

class Wait_event(Event):

	def __init__(self, drone_id, turn):
		self.drone_id = drone_id
		self.command = "W"
		self.turn = turn
		#super(Wait_event, self.id, self.command)

	def __str__(self):
		line = str(self.drone_id)
		line += " " + self.command
		line += " " + str(turn)
		return line

class OutputFormat():

	def __init__(self):
		self.total_command = 0
		self.list_of_events = list()

	

	def append_event(self, event_object):
		self.list_of_events.append(event_object)
		self.total_command += 0

	def write_event_to_file(output_file):
		file_object = open(output_file, "wb")
		first_line = str(self.total_command)
		file_object.write(first_line)
		for i in range(0,self.total_command):
			event = self.list_of_events[i]
			file_object.write(event)
			
		file_object.close()