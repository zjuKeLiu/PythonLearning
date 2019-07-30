import time

def main():
    with open('E:/workofpython/knowledge/no1.txt', 'r', encoding='utf-8') as f:
        print(f.read())
    
    with open('E:/workofpython/knowledge/no1.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    with open('E:/workofpython/knowledge/no1.txt') as f:
        lines = f.readlines()
        print(lines)

if __name__ == '__main__':
    main()