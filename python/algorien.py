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
	def split_incr(a):
		"""method to create an list with split characters and add previous characters for each loop"""
		arr = list(a.lower())
		final_array = []
		item = ''
		"""
		example with 'beach':
		will become -> ['b', 'be', 'bea', 'beac', 'beach',
						'h', 'hc', 'hca', 'hcae', 'hcaeb']
		also, to avoid space problem, add a condition
		"""
		for x in range(2):
			for character in arr:
				if(character != ' '):
					item += character
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
		for character in result[0]:
			if(character in result[1]):
				pct += 1
		pct /= len(result[1])

		return round((pct * 100), 2)
