from huffman import encode, decode

res = encode("input.txt", "output.txt")
decode("output.txt", "decode.txt", res)




from error_correcting_codes import get_packets
print(get_packets(1234))