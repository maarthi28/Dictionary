import urllib.request 
import re
print("\t -------------- DICTIONARY --------------")
flag='y'
while flag == 'y':
    url = "https://dictionary.cambridge.org/dictionary/english/"
    word = input("\nENTER THE WORD: ")
    word=word.replace(" ","-")
    url = url + word
    try:
        data = urllib.request.urlopen(url).read()
        try:
            newdata = data.decode("utf") 
        except:
            print('\n')
        try:
            newdata = data.decode('windows-1252') 
        except:
            print('\n')
        m=re.search('meta name="description" content="',newdata)
        start=m.end()
        end=start+500
        newdata1=newdata[start:end]
        m=re.search('"',newdata1)
        end=m.start()
        data=newdata1[0:end-13]
        index=data.find("The most popular dictionary and thesaurus.")
        if index != 0:
            print(data.replace(":",".\n"))
        else:
            print("\nOOPS...WORD NOT FOUND!")
    except:
        print("\nOOPS...WORD NOT FOUND!!")
    flag=(input('\nENTER "Y" TO CONTINUE, "N" TO EXIT :')).lower()
print("\nTHANK YOU!!!")
