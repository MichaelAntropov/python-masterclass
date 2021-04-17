# with open("binary", "bw") as bin_file:
#     bin_file.write(bytes(range(17)))
#
# with open("binary", "br") as bin_file_2:
#     for b in bin_file_2:
#         print(b)
a = 65534  # FF FE
b = 65535  # FF FF
c = 65536  # 00 01 00 00
x = 2998302  # 00 2D C0 1E

with open("binary", "bw") as bin_file:
    bin_file.write(a.to_bytes(2, "big"))
    bin_file.write(b.to_bytes(2, "big"))
    bin_file.write(c.to_bytes(4, "big"))
    bin_file.write(x.to_bytes(4, "big"))
    bin_file.write(x.to_bytes(5, "little"))

with open("binary", "br") as bin_file:
    e = int.from_bytes(bin_file.read(2), "big")
    f = int.from_bytes(bin_file.read(2), "big")
    g = int.from_bytes(bin_file.read(4), "big")
    h = int.from_bytes(bin_file.read(4), "big")
    j = int.from_bytes(bin_file.read(4), "big")

    print(e, f, g, h, j, sep=" : ")

