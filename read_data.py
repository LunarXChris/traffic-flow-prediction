import os
dir = "C:/Users/user/Desktop/pems/"
fastrak = 'i580w'
etc = [13601,
13501,
13301,
13101,
13001,
3701,
24001,
6001]

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
            if int(val[1]) in etc:
                fout = open(dir + 'out/' + fastrak + '_' + file, "a")

                fout.write(line)

                fout.close()
                pass
            line = f.readline()

        f.close()
