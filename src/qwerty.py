# Jenny, one of Cornell's esteemed PHD students was up all night at Olin,
# writing important documentation for a cutting-edge emoji keyboard. 
# Unfortunately, as an esteemed PHD student, Jenny was used to typing
# on a DVORAK keyboard, and all the Olin computers use QWERTY keyboards!
# Your objective is to take the scrambled messages Jenny wrote on the
# QWERTY keyboards, and convert them to the correct format, assuming
# she had used a DVORAK keyboard
# Assume that Jenny's intended message only contains letters

def qwerty(message):
    qwerty = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>? "
    dvorak = "`1234567890[]',.pyfgcrl/=\\aoeuidhtns-;qjkxbmwvz~!@#$%^&*(){}\"<>PYFGCRL?+|AOEUIDHTNS_:QJKXBMWVZ "
    new = ""
    for i in range(len(message)):
      c = message[i]
      n = qwerty[dvorak.index(c)]
      new += n
    return new