
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

#执行API调用并存储响应
''' 
    r                   响应对象
    status_code         响应对象包含的状态码：200代表成功
 '''
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print("Status code:",r.status_code)

#将API响应存储在一个变量中
response_dict=r.json()
print("Total repositories:",response_dict['total_count'])

#探索有关仓库的信息
repo_dicts=response_dict['items']

names,stars=[],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

#可视化
my_style=LS('#333366',base_style=LCS)       #定义一种样式，将基色设置为深蓝色

    #创建一个配置对象，包含传递给Bar()的所有定制
my_config=pygal.Config()
my_config.x_label_rotation=45
my_config.show_legend=False
my_config.title_font_size=24
my_config.label_font_size=14
my_config.major_label_font_size=18
my_config.truncate_label=15
my_config.show_y_guides=False
my_config.width=1000
    

''' #创建条形图，设置了样式、传递另外两个样式实参：让标签绕x轴线旋转45度、隐藏图例
chart=pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False) '''

chart=pygal.Bar(my_config,style=my_style)
chart.title='Most-starred Python Projects on Github'
chart.x_labels=names

chart.add('',stars)
chart.render_to_file('python_repos.svg')

''' print("Repositories returned:",len(repo_dicts))

#研究第一个仓库
repo_dict=repo_dicts[0]
print("\nKeys:",len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

    #概述最受欢迎的仓库
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print("Name:",repo_dict['name'])
    print("Owner:",repo_dict['owner']['login'])
    print("Stars:",repo_dict['stargazers_count'])
    print("Repository:",repo_dict['html_url'])
    # print("Created:",repo_dict['created_at'])
    # print("Updated:",repo_dict['updated_at'])
    print("Description:",repo_dict['description'])

#处理结果
print(response_dict.keys()) '''

