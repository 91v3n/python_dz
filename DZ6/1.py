print ((lambda x: x[1] if len(x) == 2 else -1)([i for i, j in enumerate(['qwe', 'asd', 'zxc', 'qwe', 'ertqwe']) if j == "qwe"]))