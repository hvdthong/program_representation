import pandas as pd


def read_file(fname):
    with open(fname) as f:
        content = f.readlines()
    return [x.strip() for x in content]


if __name__ == '__main__':
    # data = pd.read_csv('latest.csv', delimiter=',')
    # # data = pd.read_csv('example.csv', delimiter=',')
    # print(data.head())
    # print(len(data))
    # exit()

    fname = 'latest.csv'
    data = read_file(fname=fname)
    title, data = data[0:1], data[1:]
    parts = 10
    num_each_part = int(len(data) / parts)
    chunks = [data[x:x+num_each_part] for x in range(0, len(data), num_each_part)]
    print(len(data), num_each_part)
    print(len(chunks))