

codon_dict = {
         'ATA': 0, 'ATC': 0, 'ATT': 0, 'ATG': 0,
         'ACA': 0, 'ACC': 0, 'ACG': 0, 'ACT': 0,
         'AAC': 0, 'AAT': 0, 'AAA': 0, 'AAG': 0,
         'AGC': 0, 'AGT': 0, 'AGA': 0, 'AGG': 0,
         'CTA': 0, 'CTC': 0, 'CTG': 0, 'CTT': 0,
         'CCA': 0, 'CCC': 0, 'CCG': 0, 'CCT': 0,
         'CAC': 0, 'CAT': 0, 'CAA': 0, 'CAG': 0,
         'CGA': 0, 'CGC': 0, 'CGG': 0, 'CGT': 0,
         'GTA': 0, 'GTC': 0, 'GTG': 0, 'GTT': 0,
         'GCA': 0, 'GCC': 0, 'GCG': 0, 'GCT': 0,
         'GAC': 0, 'GAT': 0, 'GAA': 0, 'GAG': 0,
         'GGA': 0, 'GGC': 0, 'GGG': 0, 'GGT': 0,
         'TCA': 0, 'TCC': 0, 'TCG': 0, 'TCT': 0,
         'TTC': 0, 'TTT': 0, 'TTA': 0, 'TTG': 0,
         'TAC': 0, 'TAT': 0, 'TAA': 0, 'TAG': 0,
         'TGC': 0, 'TGT': 0, 'TGA': 0, 'TGG': 0,
          }

''' 'ATA ATC ATT' : 'I' door de codonnen zo op te stellen kan er
een list worden gemaakt met .split(), van de codonnen die gelijk staan aan
een aminozuur'''
codon_table = {
                'I':'ATA ATC ATT', 'M':'ATG' ,
                'T':'ACA ACC ACG ACT',
                'N':'AAC AAT', 'K':'AAA AAG' ,
                'S':'AGC AGT' , 'R':'AGA AGG' ,
                'L':'CTA CTC CTG CTT',
                'P':'CCA CCC CCG CCT',
                'H':'CAC CAT', 'Q':'CAA CAG',
                'R':'CGA CGC CGG CGT',
                'V':'GTA GTC GTG GTT' ,
                'A':'GCA GCC GCG GCT',
                'D':'GAC GAT' , 'E':'GAA GAG' ,
                'G':'GGA GGC GGG GGT' ,
                'S':'TCA TCC TCG TCT' ,
                'F':'TTC TTT' ,  'L':'TTA TTG',
                'Y':'TAC TAT' ,  '_':'TAA TAG TGA',
                'C':'TGC TGT' ,  'W':'TGG'
    }  



## fasta_bestand = "mRNA.fasta"
open_fasta = open(input('Please type the files you wish to use: '), 'r')

waarde = ""
for line in open_fasta:
    line = line.strip()
    if not line.startswith('>'):
        for character in line:
            waarde += character
            if len(waarde) == 3:
                codon_dict[waarde] +=1
                waarde = ""




keys = codon_table.keys()
key_list = list(keys)

for i in key_list:
    maximum,maxima = 0, ''
    codon = codon_table[i]
    codon = codon.split()
    for characters in codon:
        if codon_dict[characters] > maximum:
            maximum = codon_dict[characters]
            maxima = characters
            print(maximum,"|", characters)
print("\nTranslation successful!")

    

open_fasta.close()
    

# *voor* elk aminozuur:
# *loop* door codontabel:
#   *als* amino uit de codontabel hetzelfde is als aminozuur
