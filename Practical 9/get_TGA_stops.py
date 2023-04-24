xfile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
yfile = open('TGA_genes.fa', 'w')
f_in = xfile.read()
seq_list = f_in.split('>') # get each DNA sequence
for i in seq_list:
    if i.endswith('TGA\n'): # end with TGA
        seq = i.split(']')
        seq = seq[1] # the main body
        name = i.split() # DNA name
        yfile.write('>'+name[0])
        yfile.write(f'{seq}\n')
    else: continue
