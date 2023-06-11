# cae

Some implementations of compression algorithms for educational purposes.

## How to run

Benchmarks:

```bash
$ python3 -m benchmarks.run_benchmark
```

Tests:

```bash
# run lzw tests
$ python3 -m unittest tests/test_lzw.py

# run huffman tests
$ python3 -m unittest tests/test_huffman.py
```

## Comparison between the algorithms

The algorithms implemented are [Lempel–Ziv–Welch](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch) and [Huffman](https://en.wikipedia.org/wiki/Huffman_coding). Here's a comparison between them using some works of literature or random big texts.

| Work of art   | Original size | LZW size      | Huffman size | LZW % reduction | Huffman % reduction |
| ------------- | ------------- | ------------- | ------------ | --------------- | ------------------- |
| Hamlet        | 191726 bytes  | 119197 bytes  | 105405 bytes | 37.83%          | 45.02%              |
| Lorem Ipsum   | 9634 bytes    | 7842 bytes    | 5414 bytes   | 18.60%          | 43.80%              |
| Dom Casmurro  | 383499 bytes  | Not supported | 105405 bytes | Not supported   | 44.87%              |
