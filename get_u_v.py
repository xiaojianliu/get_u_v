# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 16:15:52 2017

@author: bling
"""
import numpy as np
import netCDF4
from datetime import datetime,timedelta
def get_u_v(time,lon,lat,layer):
    url = '''http://www.smast.umassd.edu:8080/thredds/dodsC/fvcom/hindcasts/30yr_gom3?u[0:1:90414][0:1:44][0:1:90414],v[0:1:90414][0:1:44][0:1:90414]'''       
    nc = netCDF4.Dataset(url)
    args=['u','v']
    data = {}
    for arg in args:
        data[arg] = nc.variables[arg]
    Times=np.load('Times.npy')
    Time=[]
    for a in np.arange(len(Times)):
        #print Times[a][:-10]
        
        if Times[a][-9:-7]=='60':
            #print Times[a][:-10]
            #print Times[a][:-7]
            mm=str(datetime.strptime(Times[a][:-10], '%Y-%m-%d'+'T'+'%H:%M')+timedelta(hours=1/float(60)))+':00'
            Times[a]=mm
            #print Times[a]
            Time.append(datetime.strptime(Times[a][:], '%Y-%m-%d'+' '+'%H:%M:%S:00'))
            continue
        Time.append(datetime.strptime(Times[a][:-7], '%Y-%m-%d'+'T'+'%H:%M:%S'))
    lonc=np.load('lonc.npy')
    latc=np.load('latc.npy')
    t=[]
    #print 'len(Time)',len(Time)
    print time
    for a in np.arange(len(Time)):
        t.append(abs(Time[a]-time))
    #print Time
    print 't',len(t)
    t1=np.argmin(t)
    print 't1',t1
    dis=[]
    for a in np.arange(len(lonc)):
        dis.append((lonc[a]-lon)*(lonc[a]-lon)+(latc[a]-lat)*(latc[a]-lat))
    l=np.argmin(dis)
    print 'l',l
    return data['u'][t1][layer][l],data['v'][t1][layer][l]
time='1985-07-01T12:00:00'#start_times =[dt.datetime(2010,5,19,9,13,0,0)]
time=datetime.strptime(time, '%Y-%m-%d'+'T'+'%H:%M:%S')
lon=-68.1202774
lat=43.80513
layer=0
u,v=get_u_v(time,lon,lat,layer)
print u,v
    
            
    
    
