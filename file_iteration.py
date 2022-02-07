"""
print words that are >= 5 chars, each on its own line
"""
open_file = open("file_iteration_input.txt", "r")
for line in open_file:
    word_array = line.split()

replace1 = "."
replace2 = ","
replace3 = "("
replace4 = ")"
replace5 = "'"

for i, e in enumerate(word_array):
    word_array[i] = e.replace(replace1, "")
for i, e in enumerate(word_array):
    word_array[i] = e.replace(replace2, "")
for i, e in enumerate(word_array):
    word_array[i] = e.replace(replace3, "")
for i, e in enumerate(word_array):
    word_array[i] = e.replace(replace4, "")
for i, e in enumerate(word_array):
    word_array[i] = e.replace(replace5, "")

for word in word_array:
    if len(word) >= 5:
        print(word)
        
open_file.close()