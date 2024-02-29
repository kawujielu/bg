import os
import time

#symbols = ['alt', 'xai', 'hbar', 'arb', 'fet', 'ach', 'sei', 'bnx', 'combo', 'sfp', 'xvg', 'skl', 'gdc', 'idex', 'celr', 'omg', 'ctk', 'tru', 'dar', 'lit']
symbols = ['key','nkn','meme','zrx','chr','pyth','rdnt','rsr','lrc']
# 指定目录路径
directory = '/usr/local/strategy'
# 使用os模块遍历目录
files_list = []
cp_mkdir = 'ssv/bg3'
cp_file = 'ssv_bg3.py'
cp_len = len(cp_mkdir)
for root, dirs, files in os.walk(directory):
    # 使用glob模块获取指定文件
    if root[-cp_len:] == cp_mkdir:
        for s in symbols:
            print(root[:-4], s)
            os.system(f"cp -rf {root[:-4]} /usr/local/strategy/{s}")
            os.system(f'mv /usr/local/strategy/{s}/bg3/{cp_file} /usr/local/strategy/{s}/bg3/{s}_bg3.py')
            os.system(f"rm /usr/local/strategy/{s}/bg3/*.log*")
            os.system(f"ls /usr/local/strategy/{s}/bg3")
            
            with open(f'/usr/local/strategy/{s}/bg3/bg.yaml', 'r') as f:
                hedge_data = f.readlines()

            for k, i in enumerate(hedge_data):
                if "symbol" in i:
                    num_data = i.split(':')
                    if '#' in num_data[1]:
                        num = num_data[1].split("#")[0].replace(" ", '')
                        symbol = f'{s}/usdt'
                        print(num, symbol)
                        hedge_data[k] = i.replace(num, symbol)

            with open(f'/usr/local/strategy/{s}/bg3/bg.yaml', 'w', encoding='utf-8') as f:
                for i in hedge_data:
                    f.writelines(i)
