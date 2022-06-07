import unittest

from translator import english_to_french, french_to_english

class TestenglishToFrench(unittest.TestCase): 
    def test_english_to_french(self):
        # test for the translation of a null input.
        # self.assertEqual(english_to_french(''),'')
        # test for the translation of 'Hello.'
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        # test for the translation of 'death' not equal to 'la vie.'
        self.assertNotEqual(english_to_french('death'), 'la vie')


class TestfrenchToEnglish(unittest.TestCase): 
    def test_french_to_english(self):
        # test for the translation of a null input.
        # self.assertEqual(french_to_english(''),'')
        # test for the transtlation of 'Bonjour.'
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        # test for the translation of 'école' not equal to 'movie.'
        self.assertNotEqual(french_to_english('école'), 'movie')

if __name__=='__main__':
    unittest.main()