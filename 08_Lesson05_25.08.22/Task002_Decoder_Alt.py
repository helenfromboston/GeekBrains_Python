def binaryConvert(n):
    result = ''
    while n > 0:
        result = str(n % 2) + result
        n = n // 2
    return result

def decoder(binaryCode, dictionary):
    step = 0
    animal = ''
    while step < len(binaryCode):
        code = binaryCode[step:step + 6]
        if code in dictionary:
            animal += str(dictionary[code])
        step += 6
    return animal

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabetList = list(alphabet)
binaryList = [binaryConvert(i) for i in range(len(alphabet))]
binaryList = list(map(lambda x: (6-len(x)) * '0' + str(x), binaryList))
archiveAplhabet = list(zip(alphabetList, binaryList))
dictionary = {i[1]: i[0] for i in archiveAplhabet}
f = open('Task002.txt', encoding='utf-8')
animalsList = f.readlines()
f.close()
print(list(map(lambda x: decoder(x, dictionary), animalsList)))