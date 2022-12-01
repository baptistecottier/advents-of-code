from AoC_tools import read_input

captcha=read_input()
captcha_answer_1=sum([int(captcha[i])*(captcha[i]==captcha[(i+1)%len(captcha)]) for i in range(len(captcha))])
captcha_answer_2=sum([int(captcha[i])*(captcha[i]==captcha[(i+int(len(captcha)/2))%len(captcha)]) for i in range(len(captcha))])

print('The first answer to the captcha is', captcha_answer_1, 'and the second answer to the captcha is', captcha_answer_2)