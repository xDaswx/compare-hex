
def read_bytes(file):
    with open(file, 'rb') as f:
        bytes = f.read(10)
        hexlist = []
        print(f'File: {file}')
        for b in bytes:
            hexlist.append(b)
            print('{0:0{1}x}'.format(b, 2), end=' ',)
        print('\n')

if __name__ == "__main__":
    file1 = "file_name1"
    file2 = "file_name2"
    bytes1 = read_bytes(file1)
    bytes2 = read_bytes(file2)
