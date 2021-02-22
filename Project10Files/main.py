gSum = 0  # глобальная сумма
gList = []  # глобальный список предложений
gSumFile = []  # глобальный список сумм в каждом файле


def searchWordMessage():
    print("Введите слово для поиска: ")
    return input()


def redText(text):
    while text[-2] == '.':
        text = text.replace('.', '', 1)
    return text


def searchFunc(names, word):
    for i in range(0, len(names)):
        f1 = open(names[i] + '.txt', 'r', encoding='utf8')
        text = f1.read().replace('.', '..').replace('!', '..').replace('...', '..').replace('?', '..')  # БАГ С ТОЧКОЙ
        text = text.split('. ')

        global gList, gSum
        localSumm = 0

        for j in range(len(text)):
            temp = text[j].find(word)  # Находим слово в тексте
            while temp != -1:
                if (temp == 0 or text[j][temp - 1] == ' ') and (
                        text[j][temp + len(word)] == ' ' or text[j][temp + len(word)] == '.' or
                        text[j][temp + len(word)] == ','):
                    localSumm += 1
                    gSum += 1
                    text[j] = redText(text[j])  # Исправление количества точек в конце предложения
                    gList.append(text[j])  # Список предложений с искомыми словами
                temp = text[j].find(word, temp + 1)  # Находим следующее слово в тексте

        global gSumFile
        gSumFile[i][1] += localSumm
        f1.close()


print("Список имён файлов - от 1 до 10-ти.")
print("Введите через пробел, в каких файлах искать: ")
fileNames = list(input().split())
for i in range(len(fileNames)):
    gSumFile.append([])
    gSumFile[i].append(fileNames[i])
    gSumFile[i].append(0)

buff = 0
while not buff:
    searchFunc(fileNames, searchWordMessage())
    print('Чтобы найти ещё одно слово, введите - 0')
    print('Чтобы продолжить, введите любую другую цифру')
    buff = int(input())

print('\nИскомые слова встречаются всего ', gSum, ' раз(-а).\nИз них:', sep='')
for i in range(len(gSumFile)):
    print("В файле ", gSumFile[i][0], ".txt - ", gSumFile[i][1], " раз(-а).", sep='')

f2 = open('result.txt', 'w', encoding='utf8')
for i in gList:
    f2.write(i + '\n')
f2.close()
