import db_kb as kb
import db_ehd as ehd

SERVER = '192.168.99.100'
PORT = 32768
DB_NAME = 'ehb_base'
DB_COLLECTION = 'ehb_collection'
DB_NAME_KB = 'knowledge_base'
DB_COLLECTION_KB = 'knowledge_collection'

def findAssociations(name, keywords, fragment, date, comment, association, article):
    diagnosesList = ehd.db_ehb_find(name, SERVER, PORT, DB_NAME, DB_COLLECTION)[0] #получение списка диагнозов
    if (not diagnosesList):
        return
    similarYellowWords, oldRedWords, newGreenWords = [], [], []
    diagnosisID = 0
    for keyword in keywords:
        for diagnosis in diagnosesList: #просмотр каждого диагноза в списке диагнозов
            if (keyword.lower() in diagnosis["name"].lower()) | (keyword.lower() in diagnosis["treatment"]) | \
               (keyword.lower() in diagnosis["criterion"]):
                diagnosisID = diagnosis["id"]
                newGreenWords = keywords
                if (diagnosis["name"] not in oldRedWords): #добавление названия диагноза к красным словам
                    for word in diagnosis["name"].split():
                        if word not in oldRedWords:
                            oldRedWords.append(word)
                if (diagnosis["treatment"] not in oldRedWords): #добавление методов лечения к красным словам
                    for word in diagnosis["treatment"].split():
                        if word not in oldRedWords:
                            oldRedWords.append(word)
                if (diagnosis["criterion"] not in oldRedWords): #добавление оснований диагноза к красным словам
                    if (type(diagnosis["criterion"]) == type([])):
                        for eachString in diagnosis["criterion"]:
                            for word in eachString.split():
                                if (word not in oldRedWords):
                                    oldRedWords.append(word)
                    else:
                        for word in diagnosis["criterion"].split():
                            if (word not in oldRedWords):
                                oldRedWords.append(word)

    for word in oldRedWords: #поиск совпадающих слов
        if (word in keywords) | (word in fragment.split()):
            similarYellowWords.append(word)

    if (diagnosisID): #добавление ассоциации в базу знаний, если она найдена
        kb.db_kb_insert(date, keywords, fragment, comment, association, diagnosisID, article,
                     similarYellowWords, oldRedWords, newGreenWords, SERVER, PORT, DB_NAME_KB, DB_COLLECTION_KB) #
        #return similarYellowWords, oldRedWords, newGreenWords, diagnosisID
    else:
        return 0 #иначе вывод 0


print(findAssociations("Michail Minin", ["sensitivity", "to", "some", "foods", "caused", "by", "cavitis"], "sensitivity to some foods caused by cavitis", "15-04-2018", "", 0, 0))
#print(findAssociations("Alexey Matrosov", ["subcutaneous", "tumour"], "patients diagnosed with subcutaneous tumour", "15-04-2018", "", 0, 0))
print(findAssociations("Anna Selchina", ["pain", "caused", "by", "pseudogout"], "pain caused by pseudogout", "15-04-2018", "", 0, 0))
print(findAssociations("Anna Selchina", ["seizures", "of", "limbs"], "seizures of limbs", "15-04-2018", "", 0, 0))
