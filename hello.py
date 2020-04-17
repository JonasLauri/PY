from urllib.request import urlopen
data = urlopen("https://docs.python.org/3/tutorial/modules.html")
data_box = []
for bytes in data:
    bytes_text = bytes.decode('utf8').split()
    for text in bytes_text:
            data_box.append(text)

data.close()

for word in data_box:
    print(word)

print("completed")

    
