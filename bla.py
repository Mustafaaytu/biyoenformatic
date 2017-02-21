class DNA:
		

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
d= DNA
d.olustur()
dna=d.duzenle()

	 
       
	