if __name__ == '__main__':
    N = int(raw_input())
    list = []
    queries = []
    for i in range(N):
        queries.append(raw_input().split())
    for x in range(0,N):
        for i in range(0, len(list)):
            list[i] = int(list[i])
        if(queries[x][0] == "append"):
            list.append(queries[x][1])
        elif(queries[x][0] == "remove"):
            list.remove(int(queries[x][1]))
        elif(queries[x][0] == "sort"):
            list.sort()
        elif(queries[x][0] == "pop"):
            list.pop()
        elif(queries[x][0] == "insert"):
            list.insert(int(queries[x][1]),queries[x][2])
        elif(queries[x][0] == "reverse"):
            list.reverse()
        elif(queries[x][0] == "print"):
            print(list)
