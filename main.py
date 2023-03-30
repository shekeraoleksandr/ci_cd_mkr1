def read_data(filename):
    with open(filename, 'r') as f:
        data = [line.strip(',') for line in f]
    return data

def main(file_name):
    data = read_data(file_name)
    return
if __name__ == '__main':
    main('test.txt')
