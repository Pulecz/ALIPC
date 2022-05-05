#!/usr/bin/python

debug = True

from sys import argv
text1 = open(argv[1]).readlines()
text2 = open(argv[2]).readlines()

# choose larger
larger = ""
if len(text2) > len(text1):
    larger = text2
    smaller = text1
elif len(text1) > len(text2): #else
    larger = text1
    smaller = text2

# find same packages
same = set(larger).intersection(set(smaller))
notsame = set(larger).difference(set(smaller))

print("These packages are same")
for package in same:
    print(package.strip())

#print("These packages are not same")
#for package in notsame:
#    print(package.strip())

# summary
print(f'{argv[1]} contains {len(text1)} packages\n')
print(f'{argv[2]} contains {len(text2)} packages\n\n')
print(f'Between these {len(same)} packages are same')
print(f'Between these {len(notsame)} packages are not same')

print(f'By dumb logic this means you are {len(same) / (len(larger)/100)}% compatible')

exit()
# debug
for lpackage in larger:
    if lpackage in same:
        #if debug:
            #print(f'{lpackage=} is in var same')
            #same.remove(lpackage)
            #print(same)
            #input()
        continue
    else:
        #if debug:
        #    print(f'{lpackage=} is not in var same')
        #    notsame.remove(lpackage)
        #    print(notsame)
        #    input()
        continue


