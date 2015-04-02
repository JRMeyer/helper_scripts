### Maybe useful, somewhat generalized functions:

def scan_for_files(dir_to_scan, extension=".txt", subDirs=True):
    import os
    import glob
    numFiles=0
    if subDirs == False:
        files = os.listdir(dir_to_scan)
        for f in files:
            if extension.lower() in f.lower():
                print(f)
                numFiles+=1
    elif subDirs == True:
        for path, dirs, files in os.walk(dir_to_scan):
            for d in dirs:
                for f in glob.iglob(os.path.join(path, d, extension)):
                    print f
                    numFiles+=1
    print "Search matched: ", str(numFiles), " files"


def copy_all_files(dir_to_scan, dir_to_copy, extension=".txt", 
                   delete_org = True):
    import os
    import glob  
    import shutil
    for path, dirs, files in os.walk(dir_to_scan):
        for d in dirs:
            for f in glob.iglob(os.path.join(path, d, extension)):
                shutil.copyfile(f, (dir_to_copy + os.path.basename(f)))
                if delete_org==True:
                    os.remove(f)
                else:
                    pass


def delete_all_files(dir_to_scan, extension="*.txt"):
    import os
    import glob  
    for path, dirs, files in os.walk(dir_to_scan):
        for d in dirs:
            for f in glob.iglob(os.path.join(path, d, extension)):
                os.remove(f)


def regex_sub_in_files(dirName, toMatch, theSub):
    """ Takes a directory of files, scans each file for the regexpr 'toMatch', 
    and then substitutes the match with the character string 'theSub'. """
    import re
    import os 
    listFiles = os.listdir(dirName)
    for filePath in listFiles:
        f = open((dirName + filePath), "r")
        fText = f.read()
        f.close()
        newText = re.sub(toMatch, theSub, fText, count=1)
        newF = open((dirName + filePath + ".new"), "w")
        newF.write(newText)
        newF.close()


def csv_to_list(fileName, delim):
    """ Takes a csv file and its delimiter and returns a table
    of the structure table[row][col]."""
    import csv
    with open(fileName, "Ur") as f:
        global data
        data = list(rec for rec in csv.reader(f,delimiter=delim))
        print("Your data is now in the global object 'data' --- Enjoy!")

