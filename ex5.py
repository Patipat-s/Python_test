txt_ip = input("Choose A B C D F : ")
grade = {'A':'80,100','B':'70,80','C':'60,70','D':'50,60','F':'0,50'}

if (txt_ip.upper() in grade):
    print(grade[txt_ip.upper()])
else:
    print('Wrong please choose grade again')