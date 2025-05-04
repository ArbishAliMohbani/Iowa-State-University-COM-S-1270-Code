def analyzeBook(title):
    with open(title+".txt", "r") as file:
        content = file.read()
        content.replace('_', '').replace('"', '').replace(',', '').replace('.', '').replace('-', '').replace('?', '').replace('!',  '').replace("'", "").replace('(', '').replace(')', '').replace(':', '').replace('[', '').replace(']', '').replace(';', '')
        content_list = content.split()
        count = {}
        for i in range(0, len(content_list)):
            if content_list[i].isalpha():
                if content_list[i] in count:
                    count[content_list[i]] = count[content_list[i]]+1
                else:
                    count[content_list[i]] = 1
        return count


def outputAnalysis(countDict, title):
    with open(title+"_words.txt", "w") as file:
        keys = list(countDict.keys())
        for  word in keys:
            file.write(word+" "+str(countDict[word]))
            file.write("\n")

def main():
    title = input("Please Enter Your Book Title: ")
    countDict = analyzeBook(title)
    outputAnalysis(countDict, title)

if __name__ == "__main__":
    main()
