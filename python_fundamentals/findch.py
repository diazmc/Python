word_list = ['hello','world','my','name','is','Anna']
char = 'o'
new_list = []
for letter in word_list:
    if letter.find(char) != -1:
        new_list.append(letter)
        
print new_list