import blosum as bl
bl62 = bl.BLOSUM(62) # BLOSUM62 matrix

def bl(name1, name2):
    point = 0
    amino = 0
    protein1 = open('ACE2_%s.fa'%name1).read()
    seq1 = protein1.split()[-1] # get amino acids

    protein2 = open('ACE2_%s.fa'%name2).read()
    seq2 = protein2.split()[-1]

    for i in range(len(seq1)):
        point = point+bl62[seq1[i]][seq2[i]] # get score
        if seq1[i] == seq2[i]: # count number of identical amino acids
            amino = amino+1
    percent = amino/len(seq1)

    print("protein are:\n", protein1, protein2, "\n",
          "alignment score :", point, "\n",
          "percent of identical amino acid: ", percent)

bl('mouse', 'cat')
bl('mouse', 'human')
bl('human', 'cat')
