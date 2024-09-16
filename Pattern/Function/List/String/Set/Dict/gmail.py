s = 'viprameshkumar8085@gmail.com'

if s[0].isnumeric():
    print("not valid starting number")
elif s[0] == ' ':
         print("not valid space")
elif '_' in s:
     print("not support underscore")
else:
    if s[0] == '.':
        print("starting dot not support")
    else:
        if '@gmail.com' in s.lower():
            print("valid your email ID")
            print("Successful Created: ",s)
           
        else:
             print("haven't @gmail.com: try")