import re
seq = "ATGCAATCGACTACGATCTGAGAGGGCCTAA"
seq1 = re.findall(r'ATG.+TAA', seq)
seq2 = re.findall(r'ATG.+TGA', seq)
seq3 = re.findall(r'ATG.+TAG', seq)
print(len(seq2+seq1))