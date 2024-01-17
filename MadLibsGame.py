class MadLibsGame:
    def __init__(self,file, addToLib, partsOfSpeech):
        try:
            self.file = file
            # print("self.file line 4 ran")
            self.fileStr = self.getFileStr(self.file)
            # print("getfilestr line 6 ran")
            self.wordCount = self.getLibCount()
            # print("getlibCount line 8 ran")
        except:
            print( 'obj not fully created.')
        finally:
            self.addToLib = addToLib
            self.partsOfSpeech = partsOfSpeech
            self.finalStr = self.formatLib(*addToLib, self.fileStr)
            # print("final string init\n" +self.finalStr)

    def __str__(self):
        return f"wordCount: {self.wordCount}\nwords: {self.addToLib}\npartsofspeech: {self.partsOfSpeech}\nfinalStr:\n{self.finalStr}";
    
    def getLibCount(self):
        try:
            return self.fileStr.count('{}');
        except:
            print("bad Object");

    def getFileStr(self, filePath):
        try:
            file = open(filePath)
            # print("open worked")
            fileStr = file.read()
            # print("read worked")
            file.close()
            # print("close worked")
            return fileStr;
        except:
            print("bad file name in FileStr");

    def formatLib(self, *args):
        return args[-1].format(*args);
    
def playMadLibs(filePath):
    addToLib = []
    partsOfSpeech = []
    try:
        file = open(filePath)
        # print("open worked")
        fileStr = file.read()
        # print("read worked")
        wordCount = fileStr.count('{}')
        # print("count worked")
        file.close()
        # print("close worked")
    except:
        return "file named incorrectly";
    print('There are ' f'{wordCount}' ' blank words in your MadLib.')
    for i in range(int(wordCount)):
        partsOfSpeech.append(input("Please enter part of speech for word " f'{i+1}' ": "))
    for wordType in partsOfSpeech:
        addToLib.append(input("Please enter a " f'{wordType}: '))
    game = MadLibsGame(filePath, addToLib, partsOfSpeech)
    #return fileStr.format(*addToLib);
    return game;


# def main():

#     ### *** when running section 1, comment out section 2, and vice versa ** ###


#     ######################################### begin section 1
#     libgame = playMadLibs('madlib.txt')
#     print(libgame)
#     print(type(libgame))
#     print('libgame wordCount:', libgame.wordCount)
#     print('libgame words:', libgame.addToLib)
#     print('libgame partsOfSpeech:', libgame.partsOfSpeech)
#     print('libgame file str:\n' + libgame.fileStr)
#     print('libgame finalStr:\n' + libgame.finalStr)
#     ######################################### end section 1

#     # ######################################## begin section 2
#     # addToLib = [7,6,5,4,3,2,1]
#     # partsOfSpeech = [1,2,3,4,5,6,7]
#     # libGame2 = MadLibsGame('madlib.txt', addToLib, partsOfSpeech)
#     # # libGame3 = MadLibsGame('madlib.txt', addToLib, partsOfSpeech, getLibCount('madlib.txt'), madLibs(*addToLib, getFileStr('madlib.txt')))
#     # # print(libGame2.__eq__(libGame3))
#     # print(type(libGame2))
#     # print('libgame2\n' + str(libGame2))
    
#     # ######################################## end section 2
    
#     return

# main()