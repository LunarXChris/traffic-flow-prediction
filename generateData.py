import os
dir = "C:/Users/user/Desktop/pems/out/"
month = 'feb 2012'
dir += month + '/'
out = "C:/Users/user/Desktop/pems/out/"
fastrak = 'i580w'

flow = []

for file in os.listdir(dir):
    print(file)

    file_path = os.path.join(dir, file)
    if os.path.isdir(file_path):
        pass
    elif os.path.splitext(file_path)[1] == '.txt':
        f = open(file_path, "r")

        line = f.readline()
        while line:
            val = line.split(",")
            flow.append(val[2][:-1])
            line = f.readline()

        f.close()

i = 24
num = 0
f_input = open(out + fastrak + '_' + month + '_input.txt', 'w')
f_target = open(out + fastrak + '_' + month + '_target.txt', 'w')
while i < len(flow):
    x_data = flow[i - 24]
    for j in range(i - 23, i):
        x_data += ' ' + flow[j]
    # print(x_data)
    f_input.write(x_data + '\n')
    y_data = flow[i]
    for k in range(1,8):
        y_data += ' ' + flow[i + k]
    # print(y_data)
    f_target.write(y_data + '\n')
    i += 8
    num += 1
f_input.close()
f_target.close()
print(num)