#Sequencia de DNA
dna_seq="TGGGAAAAACCCGTCTTACGGG"
rna_seq=dna_seq.replace('T','U')
print (rna_seq)

#Qual o tamanho da sequencia de DNA
print ("Tamanho da cadeia de DNA: ", len(dna_seq))

#Quantos nucleotídeos são do tipo "adenina"
print ("Nucleotídeos do tipo Adenina: ", dna_seq.count("A"))
print ("Nucleotídeos do tipo Timina: ", dna_seq.count("T"))
print ("Nucleotídeos do tipo Citosina: ", dna_seq.count("C"))
print ("Nucleotídeos do tipo Guanina: ", dna_seq.count("G"))
