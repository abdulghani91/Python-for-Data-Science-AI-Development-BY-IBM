

text = ("Thi!s is m.y my my sam,ple! is! text to? to? sample")


text_filterring = [".","!",",","?"]
myText = text
for punc in text_filterring:
    myText = myText.replace(punc,"")
#print("formatted text results: ", myText)

myText = myText.lower()
#print("formatted text results: ", myText)

list_of_words = myText.split()
print("formatted text results list: ", list_of_words)

list_of_set = set(list_of_words)
print("formatted text results set: ", list_of_set)

list_of_dict = {}

for words in list_of_set:
    list_of_dict[words] = list_of_words.count(words)
print("list of dictionary result: ", list_of_dict)