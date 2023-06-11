import heapq
from collections import Counter

class Node:
  def __init__(self, char, freq):
    self.char = char
    self.freq = freq
    self.left = None
    self.right = None

  def __lt__(self, other):
    return self.freq < other.freq

class Huffman:
  def get_freq(self, input):
    counter = Counter(input)
    result = [(char, count) for char, count in counter.items()]
    return result

  def build_tree(self, freq_list):
    queue = []
    for char, freq in freq_list:
      heapq.heappush(queue, Node(char, freq))

    while len(queue) > 1:
      left_node = heapq.heappop(queue)
      right_node = heapq.heappop(queue)

      merged_freq = left_node.freq + right_node.freq
      merged_node = Node(None, merged_freq)
      merged_node.left = left_node
      merged_node.right = right_node

      heapq.heappush(queue, merged_node)

    return heapq.heappop(queue)

  def build_codemap(self, tree):
    codemap = {}

    def traverse_tree(node, code=""):
      if node.char:
        codemap[node.char] = code
      else:
        traverse_tree(node.left, code + "0")
        traverse_tree(node.right, code + "1")

    traverse_tree(tree)
    return codemap

  def encode(self, input):
    freq = self.get_freq(input)
    tree = self.build_tree(freq)
    codemap = self.build_codemap(tree)

    input_encoded = ''.join(list(map(lambda c: codemap[c], input)))
    return (codemap, input_encoded)

if __name__ == "__main__":
  h = Huffman()
  codemap, input_encoded = h.encode('Hello, World!')
  print(codemap, input_encoded)
