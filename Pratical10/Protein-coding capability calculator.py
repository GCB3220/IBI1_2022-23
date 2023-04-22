import re
def capability(dna):
     DNA = dna.upper()
     if re.findall(r'ATG.+TGA', DNA):
         print(re.findall(r'ATG.+TGA', DNA))
         x = str(re.findall(r'ATG.+TGA', DNA))
         percent = (len(x) - 4) / len(DNA) * 100
         if percent >= 50:
             print("protein coding:", percent)
         elif percent <= 10:
             print("non-coding:", percent)
         else:
             print("unclear")
     else:
         print("not know")


a = 'atgllltga'
capability(a)

while 1 == 1:
    b = input("DNA: ")
    capability(b)
