import numpy as np

class Operate:
    def __init__(self, path):
        self.file_path = path

    # 返回字符型数据列表
    def read_txt(self):
        with open(self.file_path, 'r') as f:
            file = f.read()
        data = file.split()
        data = np.array(data)
        data = data.astype(np.float64)
        data = data.reshape(-1, 6)
        return data
    # 将数据写入txt
    def write_txt(self, data_list):
        print("please input a list that length is more than 1")
        if isinstance(data_list[0], str) and len(data_list) > 1:       # 数据存储格式为字符串时,['1 2 3', '2 3 4']
            for data in data_list:
                with open(self.file_path, 'a') as f:
                    file = f.writelines(data)
                    file = f.writelines('\n')
        elif isinstance(data_list[0], list) and len(data_list) > 1:     # 数据存储格式为浮点列表时，[[1, 2, 3], [2, 3, 4]]
            for data in data_list:
                data_str = str(data)[1:-1]
                data_str = data_str.replace(',', '')
                with open(self.file_path, 'a') as f:
                    file = f.writelines(data_str)
                    file = f.writelines('\n')
        else:
            print("##================================##")
            print("list length or data type is illegal!")
            print("##================================##")

if __name__ == '__main__':
    file_path = 'data.txt'
    # 文本读取测试
    op = Operate(file_path)
    txt = op.read_txt()
    print(txt)
    # 字符串类型输入测试
    # In1 = 8.1
    # In2 = 8.2
    # In3 = 8.3
    # In4 = 8.4
    # In5 = 8.5
    # In6 = 8.6
    # str1 = str(In1)
    # str2 = str(In2)
    # str3 = str(In3)
    # str4 = str(In4)
    # str5 = str(In5)
    # str6 = str(In6)
    # str_all = str1 + ' ' + str2 + ' ' + str3 + ' ' + str4 + ' ' + str5 + ' ' + str6
    # str_list = []
    # for i in range(2):
    #     str_list.append(str_all)
    # op.write_txt(str_list)
    # 浮点列表型输入
    data_list = [[1.1, 1.2, 1.4, 1.6, 1.7, 1.8], [2.3, 3.5, 5.4, 4.1, 7.5, 5.8]]
    op.write_txt(data_list)