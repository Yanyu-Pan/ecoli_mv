#!/usr/bin/env python
#coding=utf-8
#导入模块，初始传递命令、变量等
import argparse
import glob
import pandas as pd
import os
import shutil
parser = argparse.ArgumentParser(description = '\n该脚本用于根据匹配特征，将相应序列文件复制到新的文件夹(自动在当前文件夹创建，不用你管)，便于后续分析')
required = parser.add_argument_group('选项')
#optional = parser.add_argument_group('可选项')
required.add_argument('-i','--input', metavar = 'xx.csv', help = '输入信息文件csv,文件内部间隔符为,', required = True)
required.add_argument('--region', metavar = ' ', help = '地区信息，如山东,多个请用"，"间隔',default='/*')
required.add_argument('--Tsamp', metavar = ' ', help = '采样时间，如2017,多个请用"，"间隔',default='/*')
required.add_argument('--Tseq', metavar = ' ', help = '测序时间，如2018,多个请用"，"间隔',default='/*')
required.add_argument('--Osero', metavar = ' ', help = 'O血清型，如O157，多个请用"，"间隔',default='/*')
required.add_argument('--Hsero', metavar = ' ', help = 'H血清型，如H4，多个请用“，”间隔',default='/*')
required.add_argument('--mlst', metavar = ' ', help = 'ST型别，如st120,多个请用"，"间隔',default='/*')
required.add_argument('--stx', metavar = ' ', help = '志贺毒素，如stx2k,多个请用"，"间隔',default='/*')
required.add_argument('--type', metavar = ' ', help = '测序类型，sketch或complete',default='/*')

args = parser.parse_args()
#导入panda包
#打开文件,可\s+间隔多个空格
data = pd.read_table(args.input,sep=',')
#参数传递命名
didi=(args.region)
shishi=(args.Tsamp)
seqtime=(args.Tsamp)
mlsts=(args.mlst)
stxx=(args.stx)
typee=(args.type)
oos=(args.Osero)
hhs=(args.Hsero)
#将输入参数中的间隔替换为|
didi2=didi.replace(',','|')
shishi2=shishi.replace(',','|')
seqtime2=seqtime.replace(',','|')
mlsts2=mlsts.replace(',','|')
stxx2=stxx.replace(',','|')
typee2=typee
oos2=oos.replace(',','|')
hhs2=hhs.replace(',','|')
#匹配地区列符合的行
diqu = data["地区"].str.contains(didi2)
diqu2 = data[diqu].head()
#匹配采样时间列符合的行
shijian = diqu2["采样时间"].astype(str).str.contains(shishi2)
shijian2 = diqu2[shijian].head()
print(shijian2)
#匹配测序时间列符合的行
cexu = shijian2["测序时间"].astype(str).str.contains(seqtime2)
cexu2 = shijian2[cexu].head()
print(cexu2)
#匹配st型符合的行
st = cexu2["mlst"].str.contains(mlsts2)
st2 = cexu2[st].head()
print(st2)
#匹配stx符合的行
zhihe = st2["stx"].str.contains(stxx2)
zhihe2 = st2[zhihe].head()
print(zhihe2)
#匹配测序类型符合的行
celei = zhihe2["测序类型"].str.contains(typee2)
celei2 = zhihe2[celei].head()
print(celei2)
#匹配O血清型符合的行
oxueq = celei2["O血清型"].str.contains(oos2)
oxueq2 = celei2[oxueq].head()
print(oxueq2)
#匹配H血清型符合的行
hxueq = oxueq2["H血清型"].str.contains(hhs2)
hxueq2 = oxueq2[hxueq].head()
print(hxueq2)
#匹配选中的序列文件名
lie1 = hxueq2.loc[:,'菌株编号']+"*fa*"
name1=[]
#print os.getcwd()
for i in lie1:
    name1.append(glob.glob(i))
#print(name1)
from itertools import chain
name2=list(chain(*name1))
print(name2)
#for i in lie11:
#for namess in lie11:
#    try:
#        shutil.copy(namess,lujing)
#    except:
#        print("5555")
#新建输出文件夹，设置文件路径
os.system("mkdir PleaseUse")
lujing="./PleaseUse"
hxueq2.to_csv("PleaseUse/output.csv", index=False) 
for namess in name2:
    try:
        shutil.copy(namess,lujing)
    except:
        print("******出错了，兄弟！******")
print("******run done. 兄弟！******")
