import os

downloadFolder = input("Enter the path to torrent download folder: ")

# Function to read anime names from file called animenames.txt
# Just need to make a txt file containing anime titles separated by \n
# For example:
# Death Note
# Tokyo Ghoul
# ...
def readAnimeNames():
    animeNamesFile = open('animenames.txt', 'r')
    animeNamesData = animeNamesFile.read()
    animeNamesList = animeNamesData.split('\n')
    animeNamesFile.close()
    return animeNamesList

# Function to create the anime name folders
def createAnimeFolders():
    animeNamesList = readAnimeNames()
    for animeName in animeNamesList:
        fullPath = os.path.join(downloadFolder, animeName)
        os.makedirs(fullPath, exist_ok = True)
