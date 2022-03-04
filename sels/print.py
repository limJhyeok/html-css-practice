class basic_print:
	"""
	 조건에 맞게 인쇄
	
	 inputs:
	 - conditions


	 returns:
	 - 인쇄
	"""
	def __init__(self, conditions):
		pass

class word_set_print(basic_print):
	"""
	단어 세트 print(basic_print 조건 추가)
	
	inputs:
	- conditions
		인쇄 template 선택(시험지, 리스트, 카드 등)
		문항 수 조절(10, 20, 50, ...)
		단수 조절(1단, 2단, 3단)

	returns:
	- 인쇄

	"""
	def __init__(self, conditions):
		pass

class sentence_set_print(basic_print):
	"""
	문장 세트 print

	inputs:
	- conditions
		빈칸 만들어 인쇄(bool): 추천 빈칸 또는 선생님이 직접 클릭을 통해 빈칸 생성
	
	returns:
	- 인쇄

	"""
	def __init__(self, condtions):
		pass