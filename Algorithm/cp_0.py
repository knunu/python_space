from operator import itemgetter
import re

word_list = list()
word_dict = dict()

while True:
    temp_list = [re.sub(r'[^a-zA-Z]', '', x.lower())[0] + re.sub(r'[^a-zA-Z]', '', x.lower())[-1] for x in input().split()]
    if len(temp_list):
        word_list += temp_list
    else:
        break

for word in word_list:
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1

word_dict = sorted(word_dict.items(), key=itemgetter(1), reverse=True)
for word, value in word_dict:
    print("%s , %d" % (word, value))
