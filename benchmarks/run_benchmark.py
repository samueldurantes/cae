#!/usr/bin/env python3
from cae.lzw import Lzw
from cae.huffman import Huffman

def print_benchmark(path):
  with open(path, 'r') as file:
    file_content = file.read()
    file_size = len(file_content.encode("utf-8"))

  try:
    lzw_size = len(Lzw().encode(file_content).encode("utf-8"))
  except:
    lzw_size = "Not supported"

  huffman_size = len(Huffman().encode(file_content)[1]) // 8

  print("\n--------------------------------------------\n")
  print(f"File: {path}")
  print(f"Original size: {file_size} bytes")
  print(f"Compressed size with LZW: {lzw_size} bytes") if type(lzw_size) != str else print(f"Compressed size with LZW: {lzw_size}")
  print(f"Compressed size with Huffman: {huffman_size} bytes\n")
  print(f"Reduction with LZW: {100 - round(lzw_size * 100 / file_size, 3)}%") if type(lzw_size) != str else print(f"Reduction with LZW: {lzw_size}")
  print(f"Reduction with Huffman: {100 - round(huffman_size * 100 / file_size, 3)}%")

if __name__ == "__main__":
  paths = ["benchmarks/hamlet.txt", "benchmarks/lorem.txt", "benchmarks/casmurro.txt"]
  for path in paths:
    print_benchmark(path)
