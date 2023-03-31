def rep_char(c, n):
    print(c * n)

def draw_line_string(msg):
    line = rep_char("-",msg+1)

name = input("Input his/her name: ")

msg1 = f" Hello {name},"
msg2 = " Welcome to Seoul."

nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)

draw_line_string(nstr)
print(msg1)
print(msg2)
draw_line_string(nstr)

