def read_data(filename):
    with open(filename, 'r') as f:
        data = [line.strip().split(',') for line in f]
    return data


def sort_by_area(data):
    sorted_data = sorted(data, key=lambda x: int(x[1]))
    return sorted_data

def main(file_name):
    data = read_data(file_name)
    sorted_by_area = sort_by_area(data)
    print('Sorted by area: ')
    print_data(sorted_by_area)


if __name__ == '__main__':
    main('test.txt')
