class report:
	def __init__(self):
		pass

	def set_report():
		"""
		set별로 학생들 성적 비교
		
		inputs:
		- 학생 정보
		- set 정보
		- detail(bool): click을 통해 더 자세한 성적표 분석 가능(ex. 각 응시차수 마다 달라지는 정답률 추이)
		- etc

		returns:
		- set별 학생들 성적 화면
		
		"""
		pass

	def student_situation():
		"""
		지정한 날짜 이후의 학생 학습 현황

		inputs:
		- 날짜
		- 학생 정보 

		returns:
		- 지정한 날짜 이후 학생 학습 현황 화면

		"""

	def listening_record():
		"""
		학생이 녹음한 listening 결과 듣기

		inputs:
		- 학생정보

		returns:
		- student's listening record
		"""

	def report_print:
		"""
		inputs:
		- conditions
			암기학습(bool)
			리콜학습(bool)
			스펠학습(bool)
			매칭/스크램블(bool): 최고 성적 print
			반복횟수
			테스트(최고): 학생의 최고점수 print
			테스트(최종): 학생의 최종(최신)점수 print
			오답범위(생략, 최종, 누적): 화면에 표시될 오답 목록

		returns:

		"""

	def message_parent:
		"""
		학생의 학습결과 부모님께 카톡으로 URL 전송

		inputs:
		- 학생 정보
		- 부모님 정보
		- 학습 결과

		returns:
		- URL 생성
		- 카톡 전송
		"""

	def init_report:
		"""
		학생 report 초기화(재학습 용도 활용)

		inputs:
		- 학생 정보
		- 학습 정보

		returns:
		_ delete student's study record
		"""

	def message_student(conditions):
	"""
	선생님이 학생에게 메시지를 보낼 수 있는 기능
	
	inputs:
	- 선생님 정보(ID, class)
	- 학생 정보(ID, ...)
	- message 정보
	- conditions
	
	returns:
	- message 발송
	
	"""
	pass

class management:
	"""
	클래스 코드
	클래스 학생 추가 등록 제한 여부(bool)
	알림 설정(conditions)
	speaking 알림 설정(bool)
	학생이 선생님께 쪽찌 쓰기(bool)
	테스트 정책(일괄적 테스트 설정을 위한 사항)
	"""
	def __init__(self, class_cord):
		self.class_cord = class_cord # class_cord: random primary key

		pass

	def islimit_enroll:
		"""
		클래스 학생 추가 등록 제한 여부
		클래스 코드를 이용해 무단으로 클래스에 들어오는 방식 차단

		inputs:
		- limit(bool):

		returns:
		- class cord를 이용한 회원가입 차단
		"""

	def set_alarm:
		"""
		학생이 테스트를 제출할 때에 따른 선택적 알림 설정

		inputs:
		- options
			1. 테스트 제출할 때마다
			2. 테스트 점수 > 목표점수
			3. 테스트 점수 == 만점
			4. 알림 거부

		returns:
		- options에 따른 알림 설정

		"""

	def alarm:
		"""
		set_alarm 설정에 따라 선생님에게 알림 발송

		inputs:
		- set_alarm

		return:
		- 선생님께 alarm 발송
		"""

	def set_speaking_alarm:
		"""
		스피킹 테스트 결과 알림 설장

		inputs:
		- set(bool)

		returns:
		- speaking 알림 설정
		"""

	def test_policy:
		"""
		일괄적 테스트 설정을 위한 테스트 정책 set

		inputs:
		- conditions
			출제 문항수: 총 출제하고 싶은 문항의 수
			percent 사용: 각 항목별로 %사용하여 문항 설정(ex. 단어제시(객관식): 70%, 의미제시(주관식): 30%)
			etc
			
		returns:
		- 설정에 맞게 모든 test에 일괄 처리
		"""