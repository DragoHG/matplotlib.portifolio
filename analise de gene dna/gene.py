# Human_18S_rRNA.fasta = Human 18S rRNA gene, complete
# Escherichia_coli_16S_RNA.fasta = Escherichia coli strain U 5/41 16S ribosomal RNA gene, partial sequence
# analise ribosomal comparando os nucleotideos do DNA humano com a bacteria Escherichia

# remover # para alterar entre humano e bacteria

#entrada = open("Escherichia_coli_16S_RNA.fasta").read()
entrada = open("Human_18S_rRNA.fasta").read()

#saida = open("bacteria.html", "w")
saida = open("humano.html", "w")

cont = {}

for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        cont[i+j] = 0

entrada = entrada.replace("\n","")

for k in range(len(entrada)-1):
        cont[entrada[k]+entrada[k+1]] += 1

# html

i = 1
for k in cont:
        transparencia = cont[k]/max(cont.values())
        saida.write("<div style='width:100px; border:1px solid #111; height:100px; float:left; color:#fff; background-color:rgba(0, 0, 255, "+str(transparencia)+"')>"+k+"</div>")

        if i%4 == 0:
                saida.write("<div style='clear:both'></div>")
        i+=1

saida.close()