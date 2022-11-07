def read_file(file, mod):
    f = open(file, mod) 
    data = f.read().splitlines()
    list = []
    for line in data:
        line = line.split(';')
        list.append(line)
    f.close()
    print(list[1,1])
    return list
# if __name__== '__main__':
data = 'processing_model.csv'
