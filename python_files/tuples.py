if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tup=tuple(x for x in integer_list)
    print(hash(tup))
