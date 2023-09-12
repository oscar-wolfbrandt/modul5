
#1#
list = ["hej", "hej1", "hej2", "hej3"]
for x in list:
    print(x)

#2#
list[0]="hejdå"
print(list[0])

#3#
list.append("hejdå1")
print(list)

#4#
y = len(list)
print(y)

#5#
list.pop(4)
for x in list:
    print(x)

#6 och 7 #
rep = 0 
f = 1
while 2 > f:    
    ord = input("skriv ett ord:")
    list.append(ord)
    print(list)
    bort = int(input("skriv ett ord du vill ta bort"))
    list.pop(bort)
    print(list)

#8#
list1 = [{
    "bil1": "sak1",
    "bil2": "sak2",
    "bil3": "sak3",
    "bil4": "sak4",
}]
print(list1)

