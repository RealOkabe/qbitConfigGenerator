import os, json

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
def createAnimeFolders(animeNamesList):
    for animeName in animeNamesList:
        fullPath = os.path.join(downloadFolder, animeName)
        os.makedirs(fullPath, exist_ok = True)

# Function to create regex of anime name
def createAnimeRegex(animeName):
    return ('.*' + animeName.replace(' ', '.*') + '.*')

# Function to get the json config
def readAnimeConfig():
    configFile = open('anime.json')
    jsonData = json.load(configFile)
    return jsonData

# Function to generate configs according to anime names
def generateAnimeConfigs(animeNamesList, downloadFolder):
    sampleConfig = readAnimeConfig()
    theConfig = sampleConfig['Anime']
    sampleConfig.pop('Anime')
    for animeName in animeNamesList:
        theConfig['mustContain'] = createAnimeRegex(animeName)
        theConfig['savePath'] = os.path.join(downloadFolder, animeName)
        sampleConfig[animeName] = theConfig
        with open(animeName + '.json', 'w') as animeFile:
            json.dump(sampleConfig, animeFile)
            sampleConfig.pop(animeName)
