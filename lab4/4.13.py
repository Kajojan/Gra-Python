napis="abbaabba"
j=1
p=0
for i in napis:
    if len(napis)%2==0:
        if i == napis[len(napis)-j]:
            p=p+1
        j=j+1
if p==len(napis):
    print("Palindron")
else:
    print("Nie Palindron")
