# Представьте, что вы шпионы)
# Придумайте шифр, в котором буквы заменяются на какие-то символы
# и реализуйте шифроватор и дешифроватор
def coder(string, key):
    code_str = ''
    for el in string:
        code_str += chr(key + ord(el))
    return code_str


def decoder(string, key):
    decode_str = ''
    for el in string:
        decode_str += chr(ord(el) - key)
    return decode_str
