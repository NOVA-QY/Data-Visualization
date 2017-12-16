import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename='death_valley_2014.csv'
with open(filename) as f:
    #创建阅读器对象
    reader=csv.reader(f)
    #next()函数返回文件中的下一行
    header_row=next(reader)

    ''' #打印文件头及其位置
    for index,column_header in enumerate(header_row):
        print(index,column_header) '''
    
    #从文件中获取最高温、最低温、并添加日期
    dates,highs,lows = [],[],[]
    for row in reader:
        
        #错误检查
        try:
            current_date=datetime.strptime(row[0],"%Y-%m-%d")
            high=int(row[1])#转换为int型
            low=int(row[3])
        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    # print(highs)

    #根据数据绘制图形
    fig=plt.figure(dpi=128,figsize=(10,6))
    #给图标区域着色
    ''' 
        alpha   指定颜色的透明度,0位完全透明,1表示完全不透明
        fill_between()  接受一个x值系列和两个y值系列
    '''
    plt.plot(dates,highs,c='red',alpha=0.5)
    plt.plot(dates,lows,c='blue',alpha=0.5)
    plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

    #设置图形的格式
    plt.title("Daily high and low temperatures-2014",fontsize=24)
    plt.xlabel('',fontsize=16)
    fig.autofmt_xdate() #避免相互重叠
    plt.ylabel("Temperature(F)",fontsize=16)
    plt.tick_params(axis='both',which='major',labelsize=16)

    plt.show()
