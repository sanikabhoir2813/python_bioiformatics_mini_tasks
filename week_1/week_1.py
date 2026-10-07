dna="ACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGCTGCTGGTGGTCTACCCTTGGACCCAGAGGTTCTTTGAGTCCTTTGGGGATCTGTCCACTCCTGATGCTGTTATGGGCAACCCTAAGGTGAAGGCTCATGGCAAGAAAGTGCTCGGTGCCTTTAGTGATGGCCTGGCTCACCTGGACAACCTCAAGGGCACCTTTGCCACACTGAGTGAGCTGCACTGTGACAAGCTGCACGTGGATCCTGAGAACTTCAGGCTCCTGGGCAACGTGCTGGTCTGTGTGCTGGCCCATCACTTTGGCAAAGAATTCACCCCACCAGTGCAGGCTGCCTATCAGAAAGTGGTGGCTGGTGTGGCTAATGCCCTGGCCCACAAGTATCACTAAGCTCGCTTTCTTGCTGTCCAATTTCTATTAAAGGTTCCTTTGTTCCCTAAGTCCAACTACTAAACTGGGGGATATTATGAAGGGCCTTGAGCATCTGGATTCTGCCTAATAAAAAACATTTATTTTCATTGCAA"

print("DNA Sequence:", dna)
print("Length:", len(dna))

a_count = 0
t_count = 0
g_count = 0
c_count = 0

for base in dna:
    if base == "A":
        a_count += 1
    elif base == "T":
        t_count += 1
    elif base == "G":
        g_count += 1
    elif base == "C":
        c_count += 1

print("A:", a_count)
print("T:", t_count)
print("G:", g_count)
print("C:", c_count)

gc_count = g_count + c_count
gc_percentage = (gc_count / len(dna)) * 100

print("GC Count:", gc_count)
print("GC Percentage:", gc_percentage)

print("First 3 bases:", dna[:3])
print("Last 3 bases:", dna[-3:])

valid = True

for base in dna:
    if base != "A" and base != "T" and base != "G" and base != "C":
        valid = False

if valid:
    print("Sequence is valid DNA.")
else:
    print("Sequence contains an invalid base.")