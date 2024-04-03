import os, json

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

# Function to generate configs and create the anime name folders
def generateAnimeConfigs(animeNamesList, downloadFolder):
    sampleConfig = readAnimeConfig()
    theConfig = sampleConfig['Anime']
    sampleConfig.pop('Anime')
    for animeName in animeNamesList:
        season = input(f"Is this a new season of the anime: {animeName}? If yes, then just enter the season number. Otherwise, just press Enter\n")
        if season:
            animeName = os.path.join(animeName, f"Season {season}")
        fullPath = os.path.join(downloadFolder, animeName)
        os.makedirs(fullPath, exist_ok = True)
        theConfig['mustContain'] = createAnimeRegex(animeName)
        theConfig['savePath'] = fullPath
        sampleConfig[animeName] = theConfig
        with open(animeName + '.json', 'w') as animeFile:
            json.dump(sampleConfig, animeFile)
            sampleConfig.pop(animeName)

# Function to create regex of anime name
def createAnimeRegex(animeName):
    return ('.*' + animeName.replace(' ', '.*') + '.*')

# Function to get the json config
def readAnimeConfig():
    configFile = open('sample/anime.json')
    jsonData = json.load(configFile)
    return jsonData

# Function to generate configs according to anime names
def generateAnimeConfigs():
    animeNamesList = readAnimeNames()
    downloadFolder = input("Enter the path where you want to store the downloads: ")
    generateAnimeConfigs(animeNamesList, downloadFolder)
