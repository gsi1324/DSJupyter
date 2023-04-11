#학번 : 202104367
#학과 : 컴퓨터공학과
#이름 : 전상인
# Node 클래스 정의
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


# LinkedList 클래스 정의
class LinkedList:

	# 초기화 메소드
	def __init__(self):
		dummy = Node("dummy")
		self.head = dummy
		self.tail = dummy

		self.current = None
		self.before = None

		self.num_of_data = 0

	# append 메소드 (insert - 맨 뒤에 노드 추가, tail과 node의 next, 데이터 개수 변경)
	def append(self, data):
		new_node = Node(data)
		self.tail.next = new_node
		self.tail = new_node

		self.num_of_data += 1

	# delete 메소드 (delete - current 노드 삭제, 인접 노드의 current, next 변경, 데이터 개수 변경)
	def delete(self):
		pop_data = self.current.data

		if self.current is self.tail:
			self.tail = self.before
	
		self.before.next = self.current.next
		# 중요 : current가 next가 아닌 before로 변경된다.
		self.current = self.before 

		self.num_of_data -= 1

		return pop_data

	# first 메소드 (search1 - 맨 앞의 노드 검색, before, current 변경)
	def first(self):
		# 데이터가 없는 경우 첫번째 노드도 없기 때문에 None 리턴
		if self.num_of_data == 0: 
			return None

		self.before = self.head
		self.current = self.head.next

		return self.current.data

	# next 메소드 (search2 - current 노드의 다음 노드 검색, 이전에 first 메소드가 한번은 실행되어야 함)
	def next(self):
		if self.current.next == None:
			return None

		self.before = self.current
		self.current = self.current.next

		return self.current.data

	# size 메소드
	def size(self):
		return self.num_of_data 
	
	def traverse_all(self):
		if self.num_of_data == 0:
			print("Empty LinkedListT")
			return None
		
		self.first()
	
		print('head',end='')
		while self.current.next!= None: #조건을 self.current로 해놓으면 self.first() 함수가 current의 다음이 None일때 current와 before의 위치를 옮기지 않으므로 무한루프에 걸린다
			print(f'-> {self.current.data} ',end='')
			self.next()

		#self.first() 함수가 current의 다음이 None일때 current와 before의 위치를 옮기지 않으므로 마지막 원소만 따로 처리해준다.
		print(f'-> {self.current.data} -> null')

	

	def insert_at(self, position, new_data):
		count = 1
		new_node = Node(new_data)
		self.first()

		if self.num_of_data == 0:
			print("Empty LinkedListI")
			return None
		
		if position <= 0:
			print("Position Input Error")
			return None
		
		if position > self.num_of_data :
			self.append(new_data)
			print("Exceed Position. Append Data")

		else:
			while count != position:
				count +=1
				self.next()
			
			self.before.next = new_node
			new_node.next = self.current
			self.num_of_data +=1


		
	def remove(self, key):
		self.first()
		pos = 1
		before_delete = self.num_of_data

		if self.num_of_data == 0:
			print("Empty LinkedListR")
			return None
			
		while self.current.next != None:
			if key == self.current.data:
				self.delete()
				print(f"{pos}번째 데이터를 삭제합니다.")

			self.next()
			pos += 1
		if self.current.data == key:
			self.delete()
			print(f"{pos}번째 데이터를 삭제합니다.")
		
		if before_delete == self.num_of_data:
			print("해당하는 원소가 없습니다.")