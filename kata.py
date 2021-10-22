# TDD Kata https://gitlab.com/cherry-chain/kata/string-calculator-kata
# Author : Federica Laurino
# Date: 22th October 2021

###############################
# STEP 1 : sum integers in a string (max 2 integers). Empty string returns 0.

def test_1(fun):
	assert fun("") == 0
	assert fun("1") == 1
	assert fun("1,2") == 3

def add_1(numbers: str) -> int:
	# case 0
	if not numbers:
		return 0
	# case 1
	elif len(numbers) == 1:
		return int(numbers)
	else:
		# case 2
		l = numbers.split(",") 
		return int(l[0]) + int(l[1])

test_1(add_1)

###############################
# STEP 2 : sum multiple integers in a string. Empty string returns 0.

def test_2(fun):
	# make sure previous tests still work
	test_1(fun)
	# new test
	assert fun("1,2,3,4,5") == 15

def add_2(numbers: str) -> int:
	res = 0
	if numbers: # if not case 0 
		l = numbers.split(",")
		for el in l:
			res += int(el)
	return res

test_2(add_2)

###############################
# STEP 3: sum multiple integers in a string allowing for multiple lines.
# Empty string returns 0.

def test_3(fun):
	# make sure previous tests still work
	test_2(fun)
	# new test
	assert fun("1\n2") == 3
	assert fun("1,2\n3,4\n5") == 15

def add_3(numbers: str) -> int:
	res = 0
	if numbers: # if not case 0
		lines = numbers.split("\n")
		for l in lines:
			for n in l.split(","):
				res+=int(n)
	return res

test_3(add_3)

# alternative implementation
# import re

# def add_3(numbers: str) -> int:
# 	res = 0
# 	if numbers:
# 		l = re.split(",|\n", numbers)
# 		for el in l:
# 			res+=int(el)
# 	return res

###############################
# STEP 4: sum multiple integers in a string allowing for multiple lines
# and different delimiter. Empty string returns 0.

def test_4(fun):
	# make sure previous tests still work
	test_3(fun)
	# new test
	assert fun("//.\n1.2.3") == 6
	assert fun("//...\n1...2\n3") == 6

def add_4(numbers: str) -> int:
	res = 0
	if numbers: # if not case 0
		lines = numbers.split("\n")
		# choose delimiter
		delimiter = "," # default
		if lines[0][0:2] == "//":
			delimiter = lines[0][2::] # new delimiter
			lines = lines[1::] #lines to be read
		# sum numbers
		for l in lines:
			for n in l.split(delimiter):
				res += int(n)
	return res

test_4(add_4)

###############################
# STEP 5: sum multiple integers in a string allowing for multiple lines
# and different delimiter. Empty string returns 0. Raising exception in
# case of negative numbers and print all negatives

def test_5(fun):
	# make sure previous tests still work
	test_4(fun)
	# new test
	try:
		fun("1,2,3,4,-1,-2")
	except NegativesError as e:
		assert(e.msg == "negatives not allowed: -1,-2")

class NegativesError(Exception):
	"""Exception printing negative numbers if present"""
	def __init__(self, neg):
		self.msg = "negatives not allowed: {}".format(",".join(neg))
		super(NegativesError,self).__init__(self.msg)

def add_5(numbers: str) -> int:
	res = 0
	if numbers: # if not case 0
		lines = numbers.split("\n")
		# choose delimiter
		delimiter = "," # default
		if lines[0][0:2] == "//":
			delimiter = lines[0][2::] # new delimiter
			lines = lines[1::] # lines to be read
		# sum numbers if no negatives
		negatives = []
		for l in lines:
			for n in l.split(delimiter):
				if not negatives: # no negatives so far
					res += int(n)
				if(int(n)<0):
					negatives.append(n)
		if negatives:
			raise NegativesError(negatives)
	return res

test_5(add_5)

###############################
# STEP 6: sum multiple integers in a string allowing for multiple lines
# and different delimiter. Numbers bigger than 1000 are ignored.
# Empty string returns 0. Raising exception in case of negative numbers
# and print all negatives. 

def test_6(fun):
	# make sure previous tests still work
	test_5(fun)
	# new test
	assert fun("//.\n1.2\n2000") == 3 

class NegativesError(Exception):
	"""Exception printing negative numbers if present"""
	def __init__(self, neg):
		self.msg = "negatives not allowed: {}".format(",".join(neg))
		super(NegativesError,self).__init__(self.msg)

def add_6(numbers: str) -> int:
	res = 0
	if numbers: # if not case 0
		lines = numbers.split("\n")
		# choose delimiter
		delimiter = "," # default
		if lines[0][0:2] == "//":
			delimiter = lines[0][2::] # new delimiter
			lines = lines[1::] # lines to be read
		# sum numbers if no negatives
		negatives = []
		for l in lines:
			for n in l.split(delimiter):
				if (int(n)<=1000) & (not negatives): # small numbers ignored and no negatives so far
					res += int(n)
				if(int(n)<0):
					negatives.append(n)
		if negatives:
			raise NegativesError(negatives)
	return res


test_6(add_6)


