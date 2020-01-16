#!/usr/bin/python3

"""
	Algorien v0.0.1
	Project: https://github.com/ilies-t/algorien
	Author: ilies t <https://github.com/ilies-t>
	License: Apache License 2.0
"""

class Algorien:
	def __init__(self):
		pass

	@staticmethod
	def split_char(x):
		"""method to split a string for each caracters"""
		return [char for char in x]

	@staticmethod
	def split_incr(a):
		"""method to create an list with spliten caracters and add previous caracters for each loop"""
		arr = Algorien.split_char(a.lower())
		final_array = []
		item = ''
		"""
		example with 'beach':
		will become -> ['b', 'be', 'bea', 'beac', 'beach',
						'h', 'hc', 'hca', 'hcae', 'hcaeb']
		also, to avoid space problem, add a condition
		"""
		for x in range(2):
			for char in arr:
				if(char != ' '):
					item += char
					final_array.append(item)
			# reinitialize actual item to ''
			# and reverse "arr" list
			item = ''
			arr.reverse()

		return final_array

	@staticmethod
	def search(word, reference):
		pct = 0
		result = [
			Algorien.split_incr(word),
			Algorien.split_incr(reference)
		]
		# so check if each char in word array is present in reference array
		for char in result[0]:
			if(char in result[1]):
				pct += 1
		pct /= len(result[1])

		return round((pct * 100), 2)
