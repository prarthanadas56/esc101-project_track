
article=''
with open('indiatoday_text.txt','r') as f:
    for line in f:
        for word in line.split():
           article=article + word + '\n' 
           with open('word1_text.txt', 'w') as file:
           	file.write(article) 


article=''
with open('ndtv_text.txt','r') as f:
    for line in f:
        for word in line.split():
           article=article + word + '\n' 
           with open('word2_text.txt', 'w') as file:
           	file.write(article)                

article=''
with open('shorts_text.txt','r') as f:
    for line in f:
        for word in line.split():
           article=article + word + '\n' 
           with open('word3_text.txt', 'w') as file:
            file.write(article)  

file1 = set(line.strip() for line in open('word1_text.txt'))
file2 = set(line.strip() for line in open('word2_text.txt'))
file3 = set(line.strip() for line in open('word3_text.txt'))

newarticle=''
for line in file1 & file2 & file3:
    if line:
    	newarticle=newarticle+line+'\n'
    	print(line)

        

with open('newword_text.txt', 'w') as file:
	file.write(newarticle)
           	 

infile = "newword_text.txt"
outfile = "cleaned_file.txt"

with open("cleaned_file.txt", "w") as f:
   f.write("TRENDING AT THIS MOMENT\n\n\n\n")

delete_list = ["in\n", "as\n", "are\n","who\n","why\n","IN\n","AS\n","ARE\n","WHO\n","WHY\n","when\n","WHEN\n","2019\n","India\n","they\n","them\n","watch\n","was\n","on\n","how\n","then\n","them\n","who\n","hi\n","read\n","INDIA\n","THEY\n","THEM\n","WATCH\n","WAS\n","ON\n","AT\n","HOW\n","THEN\n","THEM","WHO","HI","READ","the\n","be\n","to\n","off\n","and\n","for\n","as\n","you\n","this\n","that\n","her\n","by\n","we\n","all\n","Is","say","THE","BE","OFF","AND","FOR","AS","YOU","THIS","THAT","HER","BY","WE","ALL","IS","SAY","CAN","YOUR","THAN","THEN","can","your","than","then","day","DAY","me","ME","A\n","a\n","at\n"]
fin = open(infile)
fout = open(outfile, "w+")
fout.write("TRENDING AT THIS MOMENT\n\n\n\n")
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()
