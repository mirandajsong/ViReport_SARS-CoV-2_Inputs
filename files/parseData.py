inputFile = "covid19Seqs.fasta"

fastaFile = "covid19SeqsFixed.fasta"

fastaInput = open(inputFile, "r")
contents = fastaInput.readlines()

fastaOutput = open(fastaFile, "w+")

lineCount = 0;
for line in contents:
    if ">" in line:
        if lineCount != 0:
            fastaOutput.write("\n")
            lineCount = lineCount + 1
        fastaOutput.write(line.rstrip()[0:-2] + "\n")
        lineCount = lineCount + 1
    else:
        fastaOutput.write(line.rstrip())
