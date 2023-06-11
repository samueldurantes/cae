import unittest
from cae.lzw import Lzw

class TestLzw(unittest.TestCase):
  def test_encode_0(self):
    self.assertEqual(Lzw().encode("hehe"), "heĀ")
    self.assertEqual(Lzw().encode("ABABA"), "ABĀA")
    self.assertEqual(Lzw().encode("ABBABBBABBA"), "ABBĀāăA")

  def test_decode_0(self):
    lzw = Lzw()
    str = "hehe"
    enc = lzw.encode(str)

    self.assertEqual(lzw.decode(enc), str)

  def test_decode_1(self):
    lzw = Lzw()
    str = "ABABA"
    enc = lzw.encode(str)

    self.assertEqual(lzw.decode(enc), str)

  def test_decode_2(self):
    lzw = Lzw()
    str = "ABBABBBABBA"
    enc = lzw.encode(str)

    self.assertEqual(lzw.decode(enc), str)

if __name__ == "__main__":
  unittest.main()
