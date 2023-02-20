from huffman import encode, decode

res = encode("input.txt", "output.txt")
decode("output.txt", "decode.txt", res)