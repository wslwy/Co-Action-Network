import random

fi = open("local_test", "r")
ftrain = open("local_train_splitByUser", "w")
ftest = open("local_test_splitByUser", "w")

# test划分为90% 训练，10% 测试
while True:
    rand_int = random.randint(1, 10)
    noclk_line = fi.readline().strip()
    clk_line = fi.readline().strip()
    if noclk_line == "" or clk_line == "":
        break
    if rand_int == 2:
        # print >> ftest, noclk_line
        # print >> ftest, clk_line
        print(noclk_line, file=ftest)
        print(clk_line, file=ftest)
    else:
        # print >> ftrain, noclk_line
        # print >> ftrain, clk_line
        print(noclk_line, file=ftrain)
        print(clk_line, file=ftrain)
        

