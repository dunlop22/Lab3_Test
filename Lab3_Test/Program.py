import os   #Проверка существования файла с данными
import random   #Случайное перемешивание

class FileReader():
    #todo проверить наличие файла, считать вопросы и ответы
    def CheckFileExist(self, namefile):        
        if os.path.isfile(namefile):
            return True
        return False

    def CheckInfoInFile(self, namefile):
        if (os.stat(namefile).st_size==0):
            return False
        return True

    

class Game():
    
    def mixQuestion(self, question_orig):
        #Создание копии
        question_mix = question_orig.copy()
        random.shuffle(question_mix)
        return question_mix

