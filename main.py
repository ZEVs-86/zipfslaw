import operator
import codecs
import matplotlib.pyplot as plt

filename = "bible.txt"
file = codecs.open("E:\\PythonProjects\\word-counter\\" + filename, "r+", "utf_8_sig")
wordcount = {}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

file.close()

wordcount_sorted = sorted(wordcount.items(), key=operator.itemgetter(1), reverse=True)

counts = []

for x in wordcount_sorted:
    word = x[0]
    count = x[1]
    if count > 10:
        print("{}: {}".format(word, count))
        counts.append(count)

print(counts)
plt.plot(counts)
plt.ylabel('Frequency')
plt.show()
