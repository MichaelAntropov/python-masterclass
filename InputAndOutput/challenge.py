with open("sample.txt", "a") as sample_file:
    multiply_list = []
    for i in range(2, 13):
        multiply_list.append("{0:>2} times 2 is {1:<2}\n".format(i, i * 2))
    sample_file.writelines(multiply_list)
