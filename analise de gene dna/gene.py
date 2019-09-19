# Human_18S_rRNA.fasta = Human 18S rRNA gene, complete
# Escherichia_coli_16S_RNA = Escherichia coli strain U 5/41 16S ribosomal RNA gene, partial sequence
# analise ribosomal comparando os nucleotideos do DNA humano com a bacteria Escherichia

bacteria = open("Escherichia_coli_16S_RNA.fasta").read()

saida_bac = open("bacteria.html", "w")

cont = {}

for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        cont[i+j] = 0

bacteria = bacteria.replace("\n","")

for k in range(len(bacteria)-1):
        cont[bacteria[k]+bacteria[k+1]] += 1

print(cont)