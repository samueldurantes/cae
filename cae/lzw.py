class Lzw:
  def create_enc_dict(self):
    return {chr(n): n for n in range(0, 256)}

  def create_dec_dict(self):
    return {n: chr(n) for n in range(0, 256)}

  def encode(self, input):
    dict = self.create_enc_dict()
    seq = input[0]
    code = 256
    res = []
    for i in range(1, len(input)):
      current_char = input[i]
      if seq + current_char in dict:
        seq += current_char
      else:
        res.append(dict[seq] if len(seq) > 1 else ord(seq))
        dict[seq + current_char] = code
        code += 1
        seq = current_char

    res.append(dict[seq] if len(seq) > 1 else ord(seq))
    return "".join(list(map(lambda n: chr(n), res)))

  def decode(self, input):
    dict = self.create_dec_dict()
    seq = out = input[0]
    res = [out]
    code = 256
    for i in range(1, len(input)):
      current_code = ord(input[i])
      if current_code < code:
        entry = dict[current_code]
      else:
        entry = seq + out

      res.append(entry)
      out = entry[0]
      dict[code] = seq + out
      code += 1
      seq = entry
    return "".join(res)

if __name__ == "__main__":
  lzw = Lzw()
  e = lzw.encode("ABBABBBABBA")
  d = lzw.decode(e)
  print(d)
