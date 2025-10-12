def print_finland_flag():
    flag = []
    for row in range(11):
        line = "" 
        for col in range(18):
            if (5 <= col <= 7) or (3 <= row <= 5):
                line += "\033[44m  \033[0m"  
            else:
                line += "\033[47m  \033[0m" 
        flag.append(line)
    print("Флаг Финляндии：")
    for line in flag:
        print(line)
print_finland_flag()