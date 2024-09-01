from jes4py import *
def encode(string, keyletters):
  alpha="abcdefghijklmnopqrstuvwxyz1234567890 "
  secret = ""
  for letter in string:
    index = alpha.find(letter)
    secret = secret+keyletters[index]
  return secret
def decode(secret , keyletters):
  alpha="abcdefghijklmnopqrstuvwxyz1234567890 "
  clear = ""
  for letter in secret:
    index = keyletters.find(letter)
    clear = clear+alpha[index]
  return clear
secert = encode("muath alhurtumi 2238766","cdefghijklmnopqrstuvwxyzab9753128640 ")
clear = decode(secert,"cdefghijklmnopqrstuvwxyzab9753128640 ")
printNow(secert)
printNow(clear)
