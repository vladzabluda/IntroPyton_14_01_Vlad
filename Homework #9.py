import os


path = 'C:\\Users\\admin\\PycharmProjects\\IntroPyton_14_01_Vlad'
files = os.listdir(path)
for file in sorted(files)[:1]:

   # print(files)
    file_path = os.path.join(path, file)


    with open("names.txt", "r") as txt_file:
        data = []
        for line in txt_file.readlines():
            data.append(line.strip())
        data = [x.replace('\t', ' ') for x in data]

    #print(data)
for i in data:
    lst = i.split()
    print(lst[1])



