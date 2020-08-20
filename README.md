# ecoli_mv
STEC管理提取小工具

# Author  
Yanyu Pan

# usage  

usage: ecoli_mv.py [-h] -i xx.csv [--region ] [--Tsamp ] [--Tseq ] [--Osero ]  
                   [--Hsero ] [--mlst ] [--stx ] [--type ]  

该脚本用于根据匹配特征，将相应序列文件复制到新的文件  
夹(自动在当前文件夹创建，不用你管)，便于后续分析  

optional arguments:  
  -h, --help            show this help message and exit  

选项:  
  -i xx.csv, --input xx.csv  
                        输入信息文件csv,文件内部间隔符为,  
  --region              地区信息，如山东,多个请用"，"间隔  
  --Tsamp               采样时间，如2017,多个请用"，"间隔  
  --Tseq                测序时间，如2018,多个请用"，"间隔  
  --Osero               O血清型，如O157，多个请用"，"间隔  
  --Hsero               H血清型，如H4，多个请用“，”间隔  
  --mlst                ST型别，如st120,多个请用"，"间隔  
  --stx                 志贺毒素，如stx2k,多个请用"，"间隔  
  --type                测序类型，sketch或complete  
 
Example:  
```
#help
python3 ecoli_mv.py -h
#提取地区为山东，采样时间为2017和2018年的O157草图和完成图的全部菌株。
python3 ecoli_mv.py -i xxx.csv --region 山东 --Tsamp 2017,2018 --Osero O157 --type sketch,complete
```
# input Files  

必须指定一个菌株背景信息表 -i xxx.csv  
内部格式为：  
```
菌株编号,测序类型,地区,测序时间,采样时间,stx,mlst,O血清型,H血清型
stec123,sketch,山东,2020,2018,stx1a,,O157,H7
stec55,complete,上海,2018,2018,stx1a,stx2k,,,
```
# Output Files  
提取(复制)的菌株在PleaseUse文件夹内


