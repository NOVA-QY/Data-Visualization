**使用API调用请求数据**

	https://api.github.com/search/repositories?q=language:python&sort=stars
	此调用返回Github托管的python项目，以及有关最受欢迎的仓库的信息  
	https://api.github.com/		将请求发送到Github网站中响应API调用的部分  
	search/repositories		让API搜索Github上的所有仓库  
	?				表示要传递一个实参  
	q=				表示开始指定查询  
	&sort=stars			指定将项目按照获得的星级进行排序
***
**监视API的速率限制**

	在浏览器中输入https://api.github.com/rate_limit
	显示:  
	"search": {			搜索API的速率限制  
	"limit": 10,		每分钟10个请求限制  
	"remaining": 10,		所剩配额  
	"reset": 15135669861	将配额重置的Unix时间  
	},
***
**设置图表的外观Config实例**
	x_label_rotation	标签绕x轴的旋转角度  
	show_legend		隐藏图例  
	title_font_size		标题大小  
	label_font_size		标签大小  
	major_font_size		主标签大小  
	truncate_label		将较长的项目名缩短为的长度  
	show_y_guides		水平线显示（隐藏）  
	width			宽度  
***
