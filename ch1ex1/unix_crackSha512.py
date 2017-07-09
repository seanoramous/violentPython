import hashlib
def testPass(cryptPass):
    #salt=cryptPass[0:2]
    #print "Salt = "+salt
    dictFile=open('words_alpha.txt','r')
    for word in dictFile.readlines():
        word=word.strip('\n')
        hashObj = hashlib.sha512(word)
        cryptWord = hashObj.
        #cryptWord = crypt.crypt(word,salt)
        #print "Word: "+word+"  |||  Cyrpt Word: "+cryptWord
        if (cryptWord == cryptPass):
            print "[+] Found Password: "+word+"\n"
            return
    print "[-] Password Not Found.\n"
    return

def main():
    passFile = open('/etc/shadow')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print "[*]i Cracking Password For: "+user+"---"+cryptPass
            testPass(cryptPass)

if __name__ == "__main__":
    main()
