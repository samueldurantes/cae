class Lzw:
  def __init__(self):
    self.dict = {chr(n): n for n in range(0, 256)}

  def encode(self, input):
    seq = input[0]
    code = 255
    res = []
    for i in range(1, len(input)):
      current_char = input[i]
      if seq + current_char in self.dict:
        seq += current_char
      else:
        res.append(self.dict[seq] if len(seq) > 1 else ord(seq))
        code += 1
        self.dict[seq + current_char] = code
        seq = current_char

    res.append(self.dict[seq] if len(seq) > 1 else ord(seq))
    return res

  def decode(self, input):
    return None

if __name__ == "__main__":
  lzw = Lzw()

  print(lzw.encode("hehe"))
