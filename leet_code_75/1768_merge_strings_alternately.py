import itertools

r = ""
for (i,j) in itertools.zip_longest("hola", "adios"):
    if i is not None:
        r += i
    if j is not None:
        r += j

print(r)