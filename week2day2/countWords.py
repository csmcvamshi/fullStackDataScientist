with open("C:/Users/vamsh/Desktop/ai-ds/fullStackDataScientist/week2day2/fibonacci.txt","r") as f:
    count = 0
    while True:
        line = f.readline()
        if not line:   # stop when no more lines
            break
        for i in line.split():
            count += 1
    print(count)
