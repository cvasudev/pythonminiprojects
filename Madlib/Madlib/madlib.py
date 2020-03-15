def getdata():
    param = {}
    values = ["place","name","adjective","verb","time"]
    for i in values:
        if i == "time":
            temp = input(f"Please enter a {i}(morning,noon,afternoon,evening or night) : ")
        else:
            temp = input(f"Please enter a {i} : ")
        param.update({i:temp})
    return param


# main program
words = list
with open("story.txt","r") as story:
    for i in story:
        words = i.split()

val = getdata()
keygen = str
for i in words:
    if i[0]=="<":
        if i[len(i)-1]==".":
            keygen = i[1:len(i)-2]
        elif i[len(i)-1]==">":
            keygen = i [1:len(i)-1]
        if keygen in val.keys():
            temp = words.index(i)
            words[temp]=val[keygen]
            if i[len(i)-1]== ".":
                words[temp]+="."

final_story = " ".join(words)

print(final_story)
            
            
            
    
