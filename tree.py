

def triangle(n):
    for i in range(n):
        for j in range(n-i):
            print(' ', end=' ')
        for k in range(2*i+1):
            print('*',end=' ')
        print()


def trunk(n):
    for i in range(n):
        for j in range(n-1):
            print(' ', end=' ')
        print('* * *')


def pattern():
  triangle(4)
  triangle(4)
  trunk(4)



if __name__ == "__main__":
    pattern()