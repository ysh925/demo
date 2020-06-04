import yaml,os

def get_yaml(file_name):
    file_path = "D:\Program Files (x86)\python\demo\Data" + os.sep + file_name + ".yaml"

    with open(file_path,'r',encoding='utf-8') as f:
        return yaml.load(f,Loader=yaml.FullLoader)


if __name__ == '__main__':
    a=get_yaml('ceshi')
    print(a)
