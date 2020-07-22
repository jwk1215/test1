import sys

#fasta에 대한 클래
class FASTA:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.count = {}
    
    def count_base(self):
        with open(self.file_name, 'r') as handle:
            for line in handle:
                if line.startswith(">"):
                    continue
                line = line.strip()
                for s in line:
                    if s in self.count:
                        self.count[s] += 1
                    else:
                        self.count[s] = 1
    def FASTQ:
        def __init__(self, file_name:str):
            self.file_name = file_name
            self.read_num = 0

        def count_read_num(self):
            cnt = 0
            with open(self.file_name, 'r') as handle:
                for line in handle:
                    if cnt %4 == 0:
                        header = line.strip()
                    elif cnt % 4 ==1:
                        seq = line.strip()
                    elif cnt % 4 == 3:
                        qual = line.strip()
                    cnt +=1


if __name__ == "__main__":
    if len(sys.argv) !=2:
        print("#usage python {sys.argv[0] [fasta]")
        sys.ext()
    
    file_name = sys.argv[1]
    t = FASTQ(file_name)
    t.count_read_num()
    print(t.read_num)


    #file_name = sys.argv[1]
    #t = FASTA(file_name)
    #t.count_base()
    #print(t.count)
