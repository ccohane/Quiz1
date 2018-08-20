import json
def readcurrency(file):
    with open(file,"r") as file:
        data=[word for line in file for word in line.split()]
        #print(data)
        list1=[]
        for x in range(0,len(data),2):
            dictionary={"Symbol": data[x], "Rate": data[x+1]}
            list1.append(dictionary)
        return list1


def save(filename,data):
    dictionary={"data": data}
    with open(filename,"w")as outputFile:
        json.dump(data,outputFile)

        
    
print(readcurrency("currency.txt"))

save("file.json", readcurrency("currency.txt"))
