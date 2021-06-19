# @Author  : Ymadr
# @FileName: main.py
# @Software: PyCharm
import json  # 引入json包
import time  # 引入时间包
import requests as r  # 引入requests包
import csv  # 引入CSV包

lj = input("请输入要爬取的第三方api链接(http/https):")  # 要获取的接口链接
id = input("api输出json值中的唯一键值:")  # json输出中每条内容所对应的唯一数字键值s
wb = input("api输出json值中的文本键值:")  # json输出中问文本所对应的键值
cs = input("请输入要获取的次数:")  # 在控制台输入获取的次数，控制获取次数
sm = input("每获取一次睡眠(s):")  # 设置每循环一次睡眠时间，防止速度过快被第三方接口拉黑

f = open('yiyan.csv', 'a', encoding='utf-8', newline='')  # 创建CSV文件 将获取的数据储存
csv_writer = csv.writer(f)  # 基于文件对象构建 csv写入对象

a = 0  # 赋值a初始值0
while a < int(cs):  # 进行判断a<输入值进行循环

    res = r.get('{}'.format(lj))  # get第三方接口获取json内容
    d = json.loads(res.text)  # 将json格式数据转换为字典

    csv_writer.writerow([d['{}'.format(id)], d['{}'.format(wb)]])  # 写入csv文件存储

    a = a + 1  # 每循环一次a增加1
    time.sleep(int(sm))  # 每循环一次睡眠时间

    print("----------------------------------------------------------")
    print("正在抓取新的一言...")
    print("已抓取数量\033[31m{}\033[0m/\033[32m{}\033[0m".format(int(a), int(cs)))  # 输出已完成数量和设置的总数量

f.close()  # 关闭csv文件


