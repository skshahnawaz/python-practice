# The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-
# content of "AGCTATAG" is 37.5%. For the given n DNA strings, return the ID of the sequence having highest GC content
# followed by the GC-content of that string.

def gc_percent(str): 
    count_gc = 0
    for chr in str:
        if (chr=="G" or chr=="C"):
            count_gc = count_gc + 1

    str_len = len(str)
    gc_percentage = (count_gc/str_len) * 100 
    return gc_percentage  


n = int(input("Enter number of DNA strings: "))
list_dna = []


for i in range(0,n):
    list_dna.append(input("Enter a DNA string: "))

gc_max = 0
gc_max_id = 0
for dna_string in list_dna:
    gc = gc_percent(dna_string) 
    if (gc> gc_max):
        gc_max = gc
        gc_max_id = list_dna.index(dna_string)
print(f"{gc_max_id+1}, {gc_max}")