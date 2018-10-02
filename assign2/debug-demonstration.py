#!/usr/bin/env python
DNA_sequence = raw_input("Name of sequence to analyze?\n") #Input of the DNA Sequence
codons = {  'TTT': 'F', 'TCT': 'S', 'TAT': 'Y', 'TGT': 'C', 'TTC': 'F', 'TCC': 'S', 'TAC': 'Y', 'TGC': 'C', 'TTA': 'L', 'TCA': 'S', 'TAA': '*', 'TGA': '*', 'TTG': 'L', 'TCG': 'S', 'TAG': '*', 'TGG': 'W', 'CTT': 'L', 'CCT': 'P', 'CAT': 'H', 'CGT': 'R', 'CTC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R', 'CTA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R', 'CTG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R','ATT': 'I', 'ACT': 'T', 'AAT': 'N', 'AGT': 'S', 'ATC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S', 'ATA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R', 'ATG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R', 'GTT': 'V', 'GCT': 'A', 'GAT': 'D', 'GGT': 'G', 'GTC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G', 'GTA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G', 'GTG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'} #Predefined dictionary by professor

#There are three important pieces for this to work:
#1. The current codon
#2. The codon counter - Controls the current codon.
#3. The protein sequence that is built.

current_codon = "" #Initalize the codon. This will have a maximum of 3 nucleotides at once.

codon_counter=0 #Initalize the codon counter to zero. This is used to keep control of the # of nucleotides in the protein sequence builder.

protein_sequence = str() #Declare the protein sequence as an empty string.

##BUILD THE PROTEIN SEQUENCE

for i in range(len(DNA_sequence)): #loop over the entire DNA sequence that the user entered.
    current_codon=current_codon+DNA_sequence[i] #add an element to the current codon
    print("Adding " + DNA_sequence[i] + " into the current codon.")
    print ("and now it looks like this: " + current_codon)
    codon_counter+=1 #add to the counter 
    print("Does current codon have 3 nucleotides to intrepret yet?")
    if(codon_counter%3==0): #if the current codon has 3 nucleotides,
        print("Yes it does.")
        #then we can interpret the current codon counter, and turn it into a protein.

        codon_counter = 0 #reset the codon counter for the next 3 elements.
        if(current_codon in codons and codons[current_codon]=="*"): #if the current codon is a stopper, 
            print("...and it is a stopper codon.")
            protein_sequence=protein_sequence+codons[current_codon] #then signal that it is a stopper
            break #and BREAK the loop

        elif(current_codon in codons and codons[current_codon]!="*"): #if the current codon is NOT a stopper,
            print("...and it is NOT stopper codon.")
            protein_sequence=protein_sequence+codons[current_codon] # then interpret the current codon and add it to the protein sequence.
            #Since this is not a stopper, then the loop will continue (hence no break statement)

        elif('!!!' in protein_sequence): #if the current codon is a mutation, 
            print("...and it is a MUTATION codon.")
            protein_sequence=protein_sequence+"!!!" #then intrepret the current codon and add a mutation flag to the protein sequence
            #Since the mutation is not considered a stopper, then the loop will continue (hence no break statement)

        else: #If the input is giberish
            break
            print("...and... I dont know what the heck it is.[IF YOU SEE THIS, YOU PROBABLY ENTERED SOMETHING IN WRONG]")
        #IT IS IMPORTANT THAT THIS STATEMENT IS AT THE END OF THE IF-ELSE CHAIN, AND NOT BEFORE IT.
        current_codon="" #Reset the current codon to nothing AFTER it has interperted the previous codon's results .
        print("RESETTING Current codon AND codon counter to intrepret next 3 nucleotides.")
    else:
        print("No it does not. Adding 1 to the codon_counter.")
print "complete coding sequence" 

###STEP TWO: OUTPUT 

print "DNA Sequence: %s\nRNA sequence: %s\nProtein Sequence: %s" % (DNA_sequence, DNA_sequence.replace('T','U'), protein_sequence) #prints out the information with the respective print statement.
if(protein_sequence[0]=='M' and protein_sequence[len(protein_sequence)-1]=="*"):
    print "internal partial coding sequence"
elif(protein_sequence[0]=='M' and protein_sequence[len(protein_sequence)-1]!="*"):
    print "5'-partial coding sequence"
elif(protein_sequence[0]!='M' and protein_sequence[len(protein_sequence)-1]=="*"):
    print "3'-partial coding sequence"
else:
    print "frame-shift in coding sequence"
