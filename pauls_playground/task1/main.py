from pauls_playground.task1.data_reader import DataReader


if __name__ == '__main__':
    data_esa = DataReader()
    data_esa.load_data(path='esa_data.dat')

    data_nasa = DataReader()
    data_nasa.load_data(path='nasa_data.dat')
    # print()
    # print(data_nasa.read_one)


    # data_finder = DataCompare()
    # print(data_nasa.data_read_one)

