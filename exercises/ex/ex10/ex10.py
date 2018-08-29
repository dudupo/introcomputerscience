class Node:
	def __init__(self, data = "", pos = None, neg = None):
		self.data = data
		self.positive_child = pos
		self.negative_child = neg

	def _gen(self, f, g ,yieldpath=False ):
		if self.positive_child is None and self.negative_child is None:
			yield self.data

		_nextnode = self.positive_child if f(self.data , g) else self.negative_child
		yield from _nextnode._gen(f, g, yieldpath)
		if yieldpath :
			yield self.data

	def dfs(self, onlyleafs = False, leafplace = False):
		if self.positive_child is None and self.negative_child is None:
			yield self.data if not leafplace else self
		else :
			for _node in [ self.positive_child , self.negative_child ]:
				yield from _node.dfs(onlyleafs , leafplace)
			if not onlyleafs :
				yield self.data


class Record:
	def __init__(self, illness, symptoms):
		self.illness = illness
		self.symptoms = symptoms
	def __iter__(self):
		return iter([(self.illness , self.symptoms)])

def parse_data(filepath):
	with open(filepath) as data_file:
		records = []
		for line in data_file:
			words = line.split()
			records.append(Record(words[0], words[1:]))
		return records


class Diagnoser:
	def __init__(self, root):
		self.__root = root

	def get_root(self):
		return self.__root

	def diagnose(self, symptoms):
		return next(self.__root._gen(lambda a , b : a in b, symptoms))

	def calculate_error_rate(self, records):
		return sum( self.diagnose(symptoms) !=  illness for record in records for illness , symptoms in record ) / len(records)

	def all_illnesses(self):
		return list(self.__root.dfs(onlyleafs = True))

	def most_common_illness(self, records):
		histogram = { illness : 0 for illness in self.all_illnesses() }
		common_illness , phases = self.__root.data , 0
		for record in records :
			for _illness , symptoms in record :
				illness = self.diagnose(symptoms)
				histogram[illness] += 1
				if histogram[illness] > phases :
					common_illness , phases = illness , histogram[illness]
		return illness

	def paths_to_illness(self, illness):

		def _paths_to_illness(_node, illness):
			paths = []
			if _node.data == illness:
				paths.append([])

			if _node.positive_child is None and _node.negative_child is None:
				return _node.data == illness , [[]]

			for _value , (issymptom_of_illness , positivepaths) in zip([True , False] , [ \
			  _paths_to_illness(_node.positive_child, illness),
			   _paths_to_illness(_node.negative_child,illness)]):
				if issymptom_of_illness :
					for path in positivepaths:
						paths.append( [_value] + path)

			return len(paths) > 0 , paths

		return _paths_to_illness(self.__root , illness)[1]

from copy import deepcopy
def build_tree(records, symptoms):

	root , temp = None , Node({})
	for symptom in reversed(symptoms):
		root = Node(symptom)
		root.positive_child = deepcopy( temp )
		root.negative_child = deepcopy( temp )
		temp = root

	diagnoser = Diagnoser(root)
	for record in records :
		for _illness , symptoms in record :
			_leafdict = diagnoser.diagnose(symptoms)
			if _illness not in _leafdict:
				_leafdict[_illness] = 0
			_leafdict[_illness] += 1

	for _node in root.dfs( onlyleafs = True , leafplace = True ):
		_node.data = max( _node.data.keys(),
		 key = lambda _illness : _node.data[_illness] )
	return diagnoser

from itertools import combinations
def optimal_tree(records, symptoms, depth):
	return min([build_tree( records , option )
	 for option in combinations(symptoms , depth)],
	  key = lambda diagnoser :  diagnoser.calculate_error_rate(records) )

if __name__ == "__main__":

	# Manually build a simple tree.
	#                cough
	#          Yes /       \ No
	#        fever           healthy
	#   Yes /     \ No
	# influenza   cold


	flu_leaf = Node("influenza", None, None)
	cold_leaf = Node("cold", None, None)
	inner_vertex = Node("fever", flu_leaf, cold_leaf)
	healthy_leaf = Node("healthy", None, None)
	root = Node("cough", inner_vertex, healthy_leaf)

	diagnoser = Diagnoser(root)

	# Simple test
	diagnosis = diagnoser.diagnose(["cough"])
	if diagnosis == "cold":
		print("Test passed")
	else:
		print("Test failed. Should have printed cold, printed: ", diagnosis)

	records = [ Record( "cold" , ["cough" , "fever" ]) , Record( "cold" , ["cough"]  )]
	print( diagnoser.paths_to_illness("cold") )
	print( diagnoser.most_common_illness(records) )
	print( diagnoser.calculate_error_rate(records) )


	records = [ Record("healthy" , [] ) ,  Record("cold" , ["cough"])  ,  Record( "influenza" ,["cough" , "fever"])]
	symptoms =  [  "cough" , "fever" ]
	diagnosis = optimal_tree(records , symptoms, 1)
	for data in diagnosis.get_root().dfs(onlyleafs = False):
		print(data)


	# Add more tests for sections 2-7 here.
