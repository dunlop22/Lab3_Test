import os   #Проверка существования файла с данными

class FileReader():
    #todo проверить наличие файла, считать вопросы и ответы
    def CheckFileExist(self, namefile):        
        if os.path.isfile(namefile):
            return True
        return False
