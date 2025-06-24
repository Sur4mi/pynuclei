#Removes all the characters from a given sequence which are not DNA or RNA bases

def dna_rna_cleaner(sequence):
    bases = ['A', 'C', 'T', 'G', 'U']
    sequence.upper().strip()
    cleaned_seq = ''
    for s in sequence:
        if s in bases:
            cleaned_seq += s
        else:
            continue
    return cleaned_seq

# Output the lenght of a given sequence

def lenght_seq(sequence):
    sequence.strip()
    lenght_seq = len(sequence)
    return lenght_seq

# Convert DNA bases in RNA bases (T to U) in a given sequence

def dna_to_rna(sequence):
    sequence.upper().strip()
    rna_sequence = sequence.replace('T', 'U')
    return rna_sequence

# Calculates the % of GC of a given sequence

def percentage_gc(sequence):
    sequence.upper().strip()
    c_count = sequence.count('C')
    g_count = sequence.count('G')
    gc_percentage = ((c_count + g_count)/len(sequence))*100
    return gc_percentage

# Output the reverse of a given sequence

def reverse(sequence):
    sequence.upper().strip()
    rev_seq = sequence[::-1]
    return rev_seq
    
# Output the complementary of a given sequence

def complementary(sequence):
    sequence.upper().strip()
    complementary = ""
    for s in sequence: 
        if s == 'A': 
            s = s.replace('A', 'T')
            complementary += s
        elif s == 'T':
            s = s.replace('T', 'A')
            complementary += s
        elif s == 'G':
            s = s.replace('G', 'C')
            complementary += s
        elif s == 'C':
            s = s.replace('C', 'G')
            complementary += s
    return complementary
