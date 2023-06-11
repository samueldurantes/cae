import unittest
from zaf.huffman import Huffman

class TestHuffman(unittest.TestCase):
  def test_encode_0(self):
    huffman = Huffman()

    self.assertEqual(huffman.encode("aabbbc")[1], "111100010")
    self.assertEqual(huffman.encode("Hello, World!")[1], "100000101011111010100111001111011010001101")
    self.assertEqual(huffman.encode("samuel")[1], "1100011101101100")

if __name__ == "__main__":
  unittest.main()
