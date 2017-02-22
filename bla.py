class DNA:
		
	def __init__(self, name,ds,seq,df,type_mod,description):
		self.NAME	=name
		self.DS		=ds
		self.SEQ	=seq
		self.DF		=df
		self.TYPE_MOD	=type_mod
		self.DESCRIPTION=description
		
		
	def goster(self):
		length=len(self.SEQ)
		dna={
		  'name'        : self.NAME,
		   'DS'         : self.DS,
		   'seq'        : self.SEQ,
		   'DF'         : self.DF,
		    'len'       : length,
		   'type'       : self.TYPE_MOD,
		   'description': self.DESCRIPTION
		}
		return dna	
	

	def olustur():
		dna={
		  'name'        : '',
		   'DS'         : '5',
		   'seq'        : '' ,
		   'DF'         : '3',
		    'len'       : '0',
		   'type'       : 'DNA',
		   'description':''
		}
		
		print(dna)

	def duzenle():
		name		=input("Enter the name:")
		seq 		=input("Enter the seq:")	
		length		=len(seq)
		description	=input("Enter the description:")
		
		dna={
		  'name'        : '',
		   'DS'         : '5',
		   'seq'        : '' ,
		   'DF'         : '3',
		    'len'       : '0',
		   'type'       : 'DNA',
		   'description':''
		}
		dna['name']=name
		dna['seq']=seq
		dna['leg']=length
		dna['description']=description
		print(dna)	

#d.olustur()

#d=DNA("DNA",5,"atgatgat",3,"DNA","First DNA")


	 
       
	
