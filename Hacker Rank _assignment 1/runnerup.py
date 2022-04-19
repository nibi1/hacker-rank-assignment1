if __name__ == '__main__':

    
    i = int(input())
    lis = list(map(int,input().split()))
    print(sorted(list(set(lis)))[-2])
    '''z = max(lis)'''
    '''while max(lis) == z:
        lis.remove(max(lis))
    print(max(lis)) '''
