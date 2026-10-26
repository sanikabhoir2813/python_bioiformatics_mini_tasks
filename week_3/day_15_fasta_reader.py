with open("sequence.fasta", "r") as file:
    lines = file.readlines()

header = lines[0].strip()
sequence = "".join(line.strip() for line in lines[1:])

print("FASTA Header:", header)
print("Sequence:", sequence)
print("Sequence Length:", len(sequence))

a_count = sequence.count("A")
t_count = sequence.count("T")
g_count = sequence.count("G")
c_count = sequence.count("C")

print("A:", a_count)
print("T:", t_count)
print("G:", g_count)
print("C:", c_count)

gc_content = ((g_count + c_count) / len(sequence)) * 100
print("GC Content:", round(gc_content, 2), "%")