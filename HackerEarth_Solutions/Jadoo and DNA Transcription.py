comp={'G':'C','C':'G','T':'A','A':'U'}
RNA=[]
DNA=(input())
for i in DNA:
    if i in comp:RNA.append(comp[i])
    else:
        print("Invalid Input")
        exit()
print("".join(RNA))