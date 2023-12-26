from eof.download import download_eofs
from datetime import datetime
import os
for i in os.listdir('D:\DEC_烏溪\SLC'):
        flag=0
        date = datetime.strptime(i.split('_')[5][:8], '%Y%m%d')
        if(os.path.isdir(rf'D:\ORBITS\{i.split("_")[0]}\{date.year}\{date.month}\aux_poeorb')):
            for j in os.listdir(rf'D:\ORBITS\{i.split("_")[0]}\{date.year}\{date.month}\aux_poeorb'):
                d1,d2 = j.split('_')[6:]
                d1 = datetime.strptime(d1[1:9], '%Y%m%d')
                d2 = datetime.strptime(d2[:8], '%Y%m%d')
                if d1 <= date <= d2: 
                    # print(i+'-> is existed')
                    flag=1
                    break
        if flag==0:
            try:
                download_eofs(None, ['S1A', 'S1B'],i,rf'D:\ORBITS\{i.split("_")[0]}\{date.year}\{date.month}\aux_poeorb',
                            cdse_user='alt41450@gmail.com',cdse_password='BM4zt4fFbH3Wf_T')
                print(i+'->download successful')
            except Exception as e:
                    print(i+'->download failed')
                    print(e)