class Direction:
	def __init__(self,start):
		if start == 5:
			self.__start, self.__finish =5,3
		elif start == 3:
			self.__start, self.__finish =3,5
		else:
			self.__start, self.__finish =5,3

	@property
	def start(self):
		return self.__start

	@start.setter

	def start(self,value):
		if   value == 5:
			self.__start, self.__finish = 5,3
		elif value == 3:	
			self.__start, self.__finish = 3,5


	@property
	def finish(self):
		return self.__finish

	def complementary(self):
		self.__start,self.__finish =self.__finish,self.__start
		
	def __repr__(self):
		return "() '->()'".format(self.__start,self.__finish)
	
	def __eq__(self,other):
		if other.start == self.__start:
			return True


