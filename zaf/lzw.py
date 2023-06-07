class Lzw:
  def create_enc_dict(self):
    return {chr(n): n for n in range(0, 256)}

  def encode(self, input):
    dict = self.create_enc_dict()
    seq = input[0]
    code = 255
    res = []
    for i in range(1, len(input)):
      current_char = input[i]
      if seq + current_char in dict:
        seq += current_char
      else:
        res.append(dict[seq] if len(seq) > 1 else ord(seq))
        code += 1
        dict[seq + current_char] = code
        seq = current_char

    res.append(dict[seq] if len(seq) > 1 else ord(seq))
    return ''.join(list(map(lambda n: chr(n), res)))

  def decode(self, input):
    return None

if __name__ == "__main__":
  e = Lzw().encode("ABABA")
  print(e)
