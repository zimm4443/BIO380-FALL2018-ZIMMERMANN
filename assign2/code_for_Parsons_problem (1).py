break
print "frame-shift in coding sequence"
for i in range(len(DNA_sequence)):
#!/usr/bin/env python
if(codon_counter%3==0):
codons = {  'TTT': 'F', 'TCT': 'S', 'TAT': 'Y', 'TGT': 'C', 'TTC': 'F', 'TCC': 'S', 'TAC': 'Y', 'TGC': 'C', 'TTA': 'L', 'TCA': 'S', 'TAA': '*', 'TGA': '*', 'TTG': 'L', 'TCG': 'S', 'TAG': '*', 'TGG': 'W', 'CTT': 'L', 'CCT': 'P', 'CAT': 'H', 'CGT': 'R', 'CTC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R', 'CTA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R', 'CTG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R','ATT': 'I', 'ACT': 'T', 'AAT': 'N', 'AGT': 'S', 'ATC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S', 'ATA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R', 'ATG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R', 'GTT': 'V', 'GCT': 'A', 'GAT': 'D', 'GGT': 'G', 'GTC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G', 'GTA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G', 'GTG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'}
DNA_sequence = raw_input("Name of sequence to analyze?\n")
codon_counter = 0
print "3'-partial coding sequence"
current_codon = ""
codon_counter+=1
elif(protein_sequence[0]=='M' and protein_sequence[len(protein_sequence)-1]!="*"):
codon_counter=0
protein_sequence=protein_sequence+codons[current_codon]
if(current_codon in codons and codons[current_codon]=="*"):
elif(current_codon in codons and codons[current_codon]!="*"):
protein_sequence=protein_sequence+codons[current_codon]
else:
if(protein_sequence[0]=='M' and protein_sequence[len(protein_sequence)-1]=="*"):
protein_sequence=protein_sequence+"!!!"
break
current_codon=""
print "internal partial coding sequence"
print "DNA Sequence: %s\nRNA sequence: %s\nProtein Sequence: %s" % (DNA_sequence, DNA_sequence.replace('T','U'), protein_sequence)
print "complete coding sequence"
elif('!!!' in protein_sequence):
elif(protein_sequence[0]!='M' and protein_sequence[len(protein_sequence)-1]=="*"):
print "5'-partial coding sequence"
current_codon=current_codon+DNA_sequence[i]
else:
protein_sequence = str()
