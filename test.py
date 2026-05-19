from transliterate import to_cyrillic, to_latin
# print(to_cyrillic("Assalom alaykum"))
# print(to_latin("Қалайсиз, ака? Ишлар яхшими?"))
# print(to_cyrillic("O'zbekiston mening vatanim"))
# string.isascii()
# print("Assalom".isascii())
# print("Қалайсиз".isascii())
s = input()
if s.isascii():
    print(to_cyrillic(s))
else:
    print(to_latin(s))