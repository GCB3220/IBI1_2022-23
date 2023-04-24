codons = input('stop codons: ') # input
xfile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
yfile = open(f'{codons}_stop_genes.fa', 'w')
f_in = xfile.read()
seq_list = f_in.split('>') # get each DNA sequence
for i in seq_list:
    if i.endswith(f'{codons}\n'): # end with TGA
        seq = i.split(']')
        seq = seq[1] # the main body
        name = i.split() # DNA name
        yfile.write('>'+name[0])
        yfile.write(f'{seq}\n')
    else: continue

y = open(f'{codons}_stop_genes.fa')
inp = y.read()
print(inp)