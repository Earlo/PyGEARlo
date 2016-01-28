from pygame import time
from constants import dtap_keys,dtap_time


class mcontrols():
	def __init__(self,key_map):		
		self.key_map = key_map
		self.k_time = {}
		for k in dtap_keys:
			self.k_time[k] = time.get_ticks()
					
	def add_input(self,key):
		pass
	#	try:
	#		command = self.key_map[key]
	#		self.puppet.commands.add(command)
	#		try: #see if it's a doubletap
	#			ot = self.k_time[command]
	#			nt = time.get_ticks()
	#			if nt-ot < dtap_time:
	#				self.puppet.commands.add("DT_"+command)
	#			self.k_time[command] = nt
	#		except KeyError:
	#			pass
	#	except KeyError:
	#		pass
			
	def rmv_input(self,key):
		pass
	#	try:
	#		command = self.key_map[key]
			#selfpuppet.commands[command] = True
			#self.puppet.commands.remove(command)
			#print "released",command
	#	except KeyError:
	#		pass

class gcontrols():
	def __init__(self,puppet,key_map):		
		self.puppet = puppet
		self.key_map = key_map
		self.k_time = {}
		for k in dtap_keys:
			self.k_time[k] = time.get_ticks()
					
	def add_input(self,key):
		try:
			command = self.key_map[key]
			self.puppet.commands.add(command)
			try: #see if it's a doubletap
				ot = self.k_time[command]
				nt = time.get_ticks()
				if nt-ot < dtap_time:
					self.puppet.commands.add("DT_"+command)
				self.k_time[command] = nt
			except KeyError:
				pass
		except KeyError:
			pass
			
	def rmv_input(self,key):
		try:
			command = self.key_map[key]
			#selfpuppet.commands[command] = True
			self.puppet.commands.remove(command)
			#print "released",command
		except KeyError:
			pass

