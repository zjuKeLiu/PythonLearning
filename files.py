def main():
    try:
        with open('no1.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定文件')
    except LookupError:
        print('指定了未知的编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误')
    finally:
        if f:
            f.close()
if __name__ == '__main__':
    main()
