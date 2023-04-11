import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
  def test1(self):
    self.assertEqual(englishToFrench("Hello, how are you?"), "Bonjour, comment es-tu?")

  def test2(self):
    self.assertNotEqual(englishToFrench("Hello, how are you?"), "Hello, comment es-tu")

class TestFrenchToEnglish(unittest.TestCase):
  def test1(self):
    self.assertEqual(frenchToEnglish("Bonjour, comment es-tu?"), "Hello, how are you?")

  def test2(self):
    self.assertNotEqual(frenchToEnglish("Bonjour, comment es-tu?"), "Hola, how est tu")

unittest.main()