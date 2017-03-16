# -*- coding: utf-8 -*-
import re
from collections import Counter
import matplotlib.pyplot as plt

with open("coli.fasta") as f:
	
	fasta=f.read()
	for genome in fasta.split(">")[1:]:
		header, genomseq = genome.splitlines()[0], "".join(genome.splitlines()[1:])
		counts=Counter(genomseq)
		#print(genomseq)
		genomSeqLen=0
		genomSeqLen=counts["A"]+counts["T"]+counts["G"]+counts["C"]
		#print(genomSeqLen)
		#print("A:",counts["A"])
		#print("T:",counts["T"])
		#print("G:",counts["G"])
		#print("C:",counts["C"])
		#print("R:",counts["R"])
def grafFonc(liste):
	plt.plot(range(0,len(liste)),liste)	
	plt.show()

def c_gc_skewness(pieceSeqLen):
	
	sGCBuffer=[0]
	for i in range(0,genomSeqLen,pieceSeqLen):	
		genome=genomseq[i:i+pieceSeqLen]
		countsGenom=Counter(genome)
		G,C=countsGenom["G"],countsGenom["C"]
		try:
			sGC=(float)(G-C)/(G+C)
		except ZeroDivisionError:
			sGC=0
		#print(genome)
		sGCBuffer.append((sGCBuffer[-1]+sGC))
		#print "G sayisi: ",G,"c:",C," ",sGC
		#print(genome ,"G:sayisi=",G,"C:sayisi=",C,"GC Kayması= ",sGC)
	
	grafFonc(sGCBuffer)
c_gc_skewness(20)







