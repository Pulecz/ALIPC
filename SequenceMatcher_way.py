from difflib import SequenceMatcher

from sys import argv
text1 = open(argv[1]).read()
text2 = open(argv[2]).read()
m = SequenceMatcher(None, text1, text2)
print(f"{argv[1]} and {argv[2]} are {m.ratio()*100}% similar")
