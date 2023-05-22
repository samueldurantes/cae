import unittest
from zaf.lzw import Lzw

class TestLzw(unittest.TestCase):
  def test_encode_0(self):
    self.assertEqual(Lzw().encode('hehe'), [104, 101, 256])
    self.assertEqual(Lzw().encode('ABBABBBABBA'), [
                     65, 66, 66, 256, 257, 259, 65])
    self.assertEqual(Lzw().encode('ABABA'), [65, 66, 256, 65])


if __name__ == '__main__':
  unittest.main()
