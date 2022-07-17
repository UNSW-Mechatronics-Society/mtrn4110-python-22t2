t = ('MTRNSoc', '2022')
print(t)
# ('MTRNSoc', '2022')

tList = list(t)
tList[-1] = '2023'  # the index -1 accesses the last item
print(tList)
# ['MTRNSoc', '2023']