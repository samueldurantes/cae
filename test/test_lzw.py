import unittest
from zaf.lzw import Lzw

class TestLzw(unittest.TestCase):
  def test_encode_0(self):
    self.assertEqual(Lzw().encode("hehe"), "heĀ")
    self.assertEqual(Lzw().encode("ABABA"), "ABĀA")
    self.assertEqual(Lzw().encode("ABBABBBABBA"), "ABBĀāăA")

if __name__ == '__main__':
  unittest.main()
