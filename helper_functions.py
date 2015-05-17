### Somewhat general functions:

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


def copy_files(dir_to_scan, dir_to_copy, extension, recursive, 
               delete_org = False):
    import os, glob, shutil

    if recursive == False:
        for orgPath in glob.iglob(os.path.join(dir_to_scan, extension)):
            fileName, ext = os.path.splitext(os.path.basename(orgPath))
            shutil.copyfile((dir_to_scan+fileName+ext),
                            (dir_to_copy+fileName+ext))
            if delete_org==True:
                os.remove(dir_to_scan+fileName+ext)
            else:
                pass

    elif recursive == True:
        for path, dirs, files in os.walk(dir_to_scan):
            for d in dirs:
                for f in glob.iglob(os.path.join(path, d, extension)):
                    shutil.copyfile(f, (dir_to_copy + os.path.basename(f)))
                    if delete_org==True:
                        os.remove(f)
                    else:
                        pass


def rename_files(dirPath, toMatch, toSub, extension):
    """ 
    Takes a directory of files, scans each filename for the regexpr 
    'toMatch', and then substitutes match with the character string 'toSub'.
    Example: 'April_14_2015.txt' --> '4_14_2015.txt', if toMatch == 'April' and 
    toSub == '4'.
    """
    import os, glob, re
    for orgPath in glob.iglob(os.path.join(dirPath, extension)):
        fileName, ext = os.path.splitext(os.path.basename(orgPath))
        if toMatch in fileName:
            newFileName = re.sub(toMatch, toSub, fileName, count=1)
            newPath = os.path.join(dirPath, newFileName + ext)
            os.rename(orgPath, newPath)


def delete_all_files(dir_to_scan, extension="*.txt"):
    import os
    import glob  
    for path, dirs, files in os.walk(dir_to_scan):
        for d in dirs:
            for f in glob.iglob(os.path.join(path, d, extension)):
                os.remove(f)


def regex_sub_in_files(dirName, toMatch, toSub):
    """ 
    Takes a directory of files, scans each file's contents for the regexpr 
    'toMatch', and then substitutes match with the character string 'toSub'.
    """
    import re
    import os 
    listFiles = os.listdir(dirName)
    for filePath in listFiles:
        f = open((dirName + filePath), "r")
        fText = f.read()
        f.close()
        newText = re.sub(toMatch, toSub, fText, count=1)
        newF = open((dirName + filePath + ".new"), "w")
        newF.write(newText)
        newF.close()


def csv_to_list(fileName, delim):
    """ Takes a csv file and its delimiter and returns a table
    of the structure table[row][col]."""
    import csv
    with open(fileName, "Ur") as f:
        data = list(rec for rec in csv.reader(f,delimiter=delim))
    return data
