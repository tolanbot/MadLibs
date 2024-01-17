import unittest
import logging
import MadLibsGame
import os

print("environ: ", os.environ.keys)

print('testing otherfile')
try:
    assert 10 == 4
    print("assertion passed")
except:
    print("assertion failed")

addToLib = [1,2,3,4,5,6,7]
partsOfSpeech = [1,2,3,4,5,6,7]

class TestMadLibs(unittest.TestCase):

    def setUp(self):
        print("test set")
        pass
    def testNumBlanks(self):
        log = logging.getLogger("DEBUG")
        log.setLevel(logging.DEBUG)
        log2 = logging.getLogger("INFOs")
        log2.setLevel(logging.INFO)

        log.debug("TestNumBlanks really printed")
        log.warning("TestWarning Printed")
        log2.info("informative")
        #libGame = MadLibsGame.playMadLibs('madlib.txt')
        libGame2 = MadLibsGame.MadLibsGame('madlib.txt', addToLib, partsOfSpeech);
        # countType =  type(libGame2.getLibCount())
        print("type of libcount:")
        self.assertEqual(libGame2.wordCount, libGame2.getLibCount())

    def testNotNull(self):
        libGame3 = MadLibsGame.MadLibsGame('madlib.txt', addToLib, partsOfSpeech);
        # libGame3 = ""
        self.assertIsInstance(libGame3, MadLibsGame.MadLibsGame)
    
    def testFileRead(self):
        libGame4 = MadLibsGame.MadLibsGame('madlib.txt', addToLib, partsOfSpeech);
        realStr = libGame4.fileStr
        print("realStr", realStr)
        self.assertIsInstance(realStr, str)


if __name__ == '__main__':
    logging.basicConfig()
    unittest.main()
