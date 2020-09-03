#step1 iter to find all models info, and get base model name

import requests
import xlwt

from lxml import etree


workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('汽车之家')
worksheet.write(0,0,'车型')
worksheet.write(0,1,'细分车型')
worksheet.write(0,2,'总评分')
worksheet.write(0,3,'总评分参与人数')
worksheet.write(0,4,'百公里油耗评分')
worksheet.write(0,5,'百公里油耗评分参与人数')
worksheet.write(0,6,'厂商指导价')
worksheet.write(0,7,'二手指导价')
worksheet.write(0,8,'正面评价标签')
worksheet.write(0,9,'负面评价标签')
worksheet.write(0,10,'空间得分')
worksheet.write(0,11,'空间得分高于/低于')
worksheet.write(0,12,'空间得分高于/低于百分比')
worksheet.write(0,13,'动力得分')
worksheet.write(0,14,'动力得分高于/低于')
worksheet.write(0,15,'动力得分高于/低于百分比')
worksheet.write(0,16,'操控得分')
worksheet.write(0,17,'操控得分高于/低于')
worksheet.write(0,18,'操控得分高于/低于百分比')
worksheet.write(0,19,'油耗得分')
worksheet.write(0,20,'油耗得分高于/低于')
worksheet.write(0,21,'油耗得分高于/低于百分比')
worksheet.write(0,22,'舒适性得分')
worksheet.write(0,23,'舒适性得分高于/低于')
worksheet.write(0,24,'舒适性得分高于/低于百分比')
worksheet.write(0,25,'外观得分')
worksheet.write(0,26,'外观得分高于/低于')
worksheet.write(0,27,'外观得分高于/低于百分比')
worksheet.write(0,28,'内饰得分')
worksheet.write(0,29,'内饰得分高于/低于')
worksheet.write(0,30,'内饰得分高于/低于百分比')
worksheet.write(0,31,'性价比得分')
worksheet.write(0,32,'性价比得分高于/低于')
worksheet.write(0,33,'性价比得分高于/低于百分比')
worksheet.write(0,34,'id')
worksheet.write(0,35,'motherId')
workbook.save('./moreData/modelMoreInfo1.xls')

for i in range(4467,12000):
    
    print(i+1,47500)
    
    try:
    
        url = 'https://k.autohome.com.cn/spec/'+str(i)+'/'
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}
        r = requests.get(url,headers=headers).text
        h = etree.HTML(r)

        title = h.xpath('/html/body/div[2]/div[3]/div[1]/div/a/text()')

        goodLabels = h.xpath('//*[@id="tab-10"]/div[2]/div//*[@class=" "]/text()')
        badLabels = h.xpath('//*[@id="tab-10"]/div[2]/div//*[@class=" dust"]/text()')

        space = h.xpath('/html/body/div[2]/div[4]/div/div/div/dl/dd/div/ul[1]/li[2]/div[2]/text()')
        HLspace = h.xpath('/html/body/div[2]/div[4]/div/div/div/dl/dd/div/ul[1]/li[2]/div[3]/i/@class')
        Pspace = h.xpath('/html/body/div[2]/div[4]/div/div/div/dl/dd/div/ul[1]/li[2]/div[3]/text()')

        power = h.xpath('/html/body/div[2]/div[4]/div/div/div/dl/dd/div/ul[1]/li[3]/div[2]/text()')
        HLpower = h.xpath('/html/body/div[2]/div[4]/div/div/div/dl/dd/div/ul[1]/li[3]/div[3]/i/@class')
        Ppower = h.xpath('/html/body/div[2]/div[4]/div/div/div/dl/dd/div/ul[1]/li[3]/div[3]/text()')

        control = h.xpath('/html/body/div[2]/div[4]/div/div/div/dl/dd/div/ul[1]/li[4]/div[2]/text()')
        HLcontrol = h.xpath('/html/body/div[2]/div[4]/div/div/div/dl/dd/div/ul[1]/li[4]/div[3]/i/@class')
        Pcontrol = h.xpath('/html/body/div[2]/div[4]/div/div/div/dl/dd/div/ul[1]/li[4]/div[3]/text()')

        cost = h.xpath('/html/body/div[2]/div[4]/div/div/div/dl/dd/div/ul[1]/li[5]/div[2]/text()')
        HLcost = h.xpath('/html/body/div[2]/div[4]/div/div/div/dl/dd/div/ul[1]/li[5]/div[3]/i/@class')
        Pcost = h.xpath('/html/body/div[2]/div[4]/div/div/div/dl/dd/div/ul[1]/li[5]/div[3]/text()')

        comfort = h.xpath('/html/body/div[2]/div[4]/div/div/div/dl/dd/div/ul[2]/li[2]/div[2]/text()')
        HLcomfort = h.xpath('/html/body/div[2]/div[4]/div/div/div/dl/dd/div/ul[2]/li[2]/div[3]/i/@class')
        Pcomfort = h.xpath('/html/body/div[2]/div[4]/div/div/div/dl/dd/div/ul[2]/li[2]/div[3]/text()')

        looking = h.xpath('/html/body/div[2]/div[4]/div/div/div/dl/dd/div/ul[2]/li[3]/div[2]/text()')
        HLlooking = h.xpath('/html/body/div[2]/div[4]/div/div/div/dl/dd/div/ul[2]/li[3]/div[3]/i/@class')
        Plooking = h.xpath('/html/body/div[2]/div[4]/div/div/div/dl/dd/div/ul[2]/li[3]/div[3]/text()')

        inner = h.xpath('/html/body/div[2]/div[4]/div/div/div/dl/dd/div/ul[2]/li[4]/div[2]/text()')
        HLinner = h.xpath('/html/body/div[2]/div[4]/div/div/div/dl/dd/div/ul[2]/li[4]/div[3]/i/@class')
        Pinner = h.xpath('/html/body/div[2]/div[4]/div/div/div/dl/dd/div/ul[2]/li[4]/div[3]/text()')

        cost_performance = h.xpath('/html/body/div[2]/div[4]/div/div/div/dl/dd/div/ul[2]/li[5]/div[2]/text()')
        HLcost_performance = h.xpath('/html/body/div[2]/div[4]/div/div/div/dl/dd/div/ul[2]/li[4]/div[3]/i/@class')
        Pcost_performance = h.xpath('/html/body/div[2]/div[4]/div/div/div/dl/dd/div/ul[2]/li[5]/div[3]/text()')

        names = [space,power,control,cost,comfort,looking,inner,cost_performance]
        HLs = [HLspace,HLpower,HLcontrol,HLcost,HLcomfort,HLlooking,HLinner,HLcost_performance]
        Ps = [Pspace,Ppower,Pcontrol,Pcost,Pcomfort,Plooking,Pinner,Pcost_performance]



        price = h.xpath('//*[@id="price"]/span[1]/a/text()')
        secondHandPrice = h.xpath('//*[@id="price"]/span[2]/a/span')

        allScore = h.xpath('/html/body/div[2]/div[4]/div/div/div/dl/dd/ul/li[2]/span[1]/span[2]/text()')
        allPeople = h.xpath('/html/body/div[2]/div[4]/div/div/div/dl/dd/ul/li[2]/span[2]/text()')

        petrolCost = h.xpath('/html/body/div[2]/div[4]/div/div/div/div/div/div/p/span[2]/text()')
        petrolPeople = h.xpath('/html/body/div[2]/div[4]/div/div/div/div/div/div/p/text()')
        
    except:
        print(title)
    
    
    try:
        a = h.xpath('/html/body/div[2]/div[2]/div/a[4]/@href')
        newUrl = 'https://k.autohome.com.cn'+a[0]
        r = requests.get(newUrl,headers=headers).text
        h = etree.HTML(r)
        bigTitle = h.xpath('/html/body/div[4]/div[3]/div[1]/div[1]/a/text()')
        print(bigTitle)
    except:
        workbook.save('./moreData/modelMoreInfo1.xls')    
        
    worksheet.write(i+1,34,i)
    worksheet.write(i+1,35,a)

    try:
        worksheet.write(i+1,0,bigTitle)
    except:
        workbook.save('./moreData/modelMoreInfo1.xls')
    try:
        worksheet.write(i+1,1,title)
    except:
        workbook.save('./moreData/modelMoreInfo1.xls')
    try:
        worksheet.write(i+1,2,allScore)
    except:
        workbook.save('./moreData/modelMoreInfo1.xls')
    try:
        worksheet.write(i+1,3,allPeople)
    except:
        workbook.save('./moreData/modelMoreInfo1.xls')
    
    try:
        worksheet.write(i+1,5,petrolPeople[1][7:-30])
    except:
        workbook.save('./moreData/modelMoreInfo1.xls')
    try:
        worksheet.write(i+1,4,petrolCost)
        worksheet.write(i+1,6,price)
        worksheet.write(i+1,7,secondHandPrice)
        worksheet.write(i+1,8,goodLabels)
        worksheet.write(i+1,9,badLabels)
    except:
        workbook.save('./moreData/modelMoreInfo1.xls')
    try:
        worksheet.write(i+1,10,space[0][38:42])
        worksheet.write(i+1,11,HLspace)
    except:
        workbook.save('./moreData/modelMoreInfo1.xls')
    try:
        worksheet.write(i+1,12,Pspace[1][:-34])
    except:
        workbook.save('./moreData/modelMoreInfo1.xls')
    try:
        worksheet.write(i+1,13,power[0][38:42])
        worksheet.write(i+1,14,HLpower)
    except:
        workbook.save('./moreData/modelMoreInfo1.xls')
    try:
        worksheet.write(i+1,15,Ppower[1][:-34])
    except:
        workbook.save('./moreData/modelMoreInfo1.xls')
    try:
        worksheet.write(i+1,16,control[0][38:42])
        worksheet.write(i+1,17,HLcontrol)
    except:
        workbook.save('./moreData/modelMoreInfo1.xls')
    try:
        worksheet.write(i+1,18,Pcontrol[1][:-34])
    except:
        workbook.save('./moreData/modelMoreInfo1.xls')
    try:
        worksheet.write(i+1,19,cost[0][38:42])
        worksheet.write(i+1,20,HLcost)
    except:
        workbook.save('./moreData/modelMoreInfo1.xls')
    try:
        worksheet.write(i+1,21,Pcost[1][:-34])
    except:
        workbook.save('./moreData/modelMoreInfo1.xls')
    try:
        worksheet.write(i+1,22,comfort[0][38:42])
        worksheet.write(i+1,23,HLcomfort)
    except:
        workbook.save('./moreData/modelMoreInfo1.xls')
    try:
        worksheet.write(i+1,24,Pcomfort[1][:-34])
    except:
        workbook.save('./moreData/modelMoreInfo1.xls')
    try:
        worksheet.write(i+1,25,looking[0][38:42])
        worksheet.write(i+1,26,HLlooking)
    except:
        workbook.save('./moreData/modelMoreInfo1.xls')
    try:
        worksheet.write(i+1,27,Plooking[1][:-34])
    except:
        workbook.save('./moreData/modelMoreInfo1.xls')
    try:
        worksheet.write(i+1,28,inner[0][38:42])
        worksheet.write(i+1,29,HLinner)
    except:
        workbook.save('./moreData/modelMoreInfo1.xls')
    try:
        worksheet.write(i+1,30,Pinner[1][:-34])
    except:
        workbook.save('./moreData/modelMoreInfo1.xls')
    try:
        worksheet.write(i+1,31,cost_performance[0][38:42])
        worksheet.write(i+1,32,HLcost_performance)
    except:
        workbook.save('./moreData/modelMoreInfo1.xls')
    try:
        worksheet.write(i+1,33,Pcost_performance[1][:-34])
    except:
        workbook.save('./moreData/modelMoreInfo1.xls')
        
        
    workbook.save('./moreData/modelMoreInfo1.xls')