import base64;
inp = open("rockyou.txt", "br");
outp = open("rockyou-base64-new.txt","w");
for x in inp:
    print(base64.b64encode(x).decode("utf-8"))
inp.close()
outp.close()
