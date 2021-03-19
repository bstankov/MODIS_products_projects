#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      bob.stankovic
#
# Created:     12/02/2021
# Copyright:   (c) bob.stankovic 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import requests
import re, os, sys
from datetime import date
import numpy as np
#from bitBucke_func import download_hdf

def mkdir(dirname, remove=True, chdir=False):
    import shutil
    """create a directory dirnme.  if it iexists     , it is removed by shutil.rmtree
    """
    if os.path.isdir(dirname):
        if remove:
            shutil.rmtree(dirname)
        else:
            return False  # did not make new directory
    os.mkdir(dirname)
    return
def re_read_urlbase(url_base):
    '''  read the content from the web and get ready for parsing '''

    mod10_req = requests.get(url_base)  #read folders and sort them
    print(mod10_req.status_code)
    print(mod10_req.ok)
    mod10_sadrzaj = mod10_req.text
    #print(dir(req))
    mod10_stripped = re.sub('<[^<]+?>', '',mod10_sadrzaj)
    mod10_size = len(mod10_stripped)
    print("leng:", mod10_size)   #there are 73697
    return mod10_stripped
def write_file_out(targets, outF ):
    with open(outF, 'w') as out_file:
        for i in targets:
            out_file.write(str(i.strip()))

            out_file.write('\n')
    return

def get_MOD10A1F_hdfs():
    '''read the NSIDC web content, parse it for daily folders
    identify the most recent folder and go and grab 4 HDF files covering AB  '''
    #downloading folder for MOD10A1F.061 data products
    base = "https://n5eil01u.ecs.nsidc.org/MOST/MOD10A1F.061/"
    folders_req = re_read_urlbase(base)

    #identify pattern "2020.02.12"
    #identify folders that start with 2021
    pattern = re.compile(r'2021[.]\d{2}[.]\d{2}')
    ##    matches = pattern.finditer(stripped)
    matches = pattern.findall(folders_req )

    y = []  #store years
    m = []  #STORE months
    d = []    #store days
    for match in matches:
        #convert unicode to a string
        utf8string =  match.encode("utf-8")
        #split a line to extract year, month and days
        #splits =utf8string.split('.')  #separate year from month and day
        splits =  match.split('.')
        d.append(splits[2])
        m.append(splits[1])
        y.append(splits[0])

    amonth = np.array(m)[-1]  #identify the most recent month
    ayear = np.array(y)[-1]    #identify the most recent year
    aday= np.array(d)[-1]   #identify the most recent day
    print("ayear: ",ayear, type(ayear))
    print("last date:", ayear, amonth, aday, type(amonth), type(aday))
    #create directory
    root = r"U:\RS_Task_Workspaces\NDSI\data"
    dirname = os.path.join(root, ayear+'_'+amonth +'_'+aday)
    print("dirname:",dirname)
    mkdir( dirname, remove=True, chdir=False)
    #****************************************************

    url_base = "%s%s.%s.%s/"  % (base,ayear,amonth, aday )
    print("urlbase:", url_base)
    #read the most recent folder's content...
    mod10a1f_stripped = re_read_urlbase(url_base)
    print("leng:",len(mod10a1f_stripped ))
    content_leng = len(mod10a1f_stripped )

    #identify necessary tiles covering Alberta
    hdf_dir=['h10v03','h10v04','h11v02','h11v03','h12v02','h12v03']
    key = ['.hdf','.xml']
    key_1 = 'hdf.xml'

    targets = []   #it contains hdf files to be downloaded
    if content_leng < 5000:
        print("you move out and reduce day and search for previous day")
        #IN CASE THE MOST RECENT FOLDER MISSING NEEDED FILES WE download data from
        #previous day folder
        aday = int(aday) - 1
        print("new aday: ", aday)
        #create a folder to download
        dirname = os.path.join(root, ayear + '_' + amonth + '_' + str(aday).zfill(2))  #Insert zfill...
        print("previous dirname:", dirname)
        mkdir(dirname, remove=True, chdir=False)
        #then we work with a previous day where we read entire folder

        url_base_1 = "%s%s.%s.%s/" % (base, ayear, amonth, str(aday).zfill(2))
        print("urlbase_1:", url_base_1)
        mod10a1f_stripped = re_read_urlbase(url_base_1    )
        #print("sadrz:", mod10a1f_stripped)
        for line in mod10a1f_stripped.split('\n'):
            if (key[0] in line and not key[1] in line):
                line_1 = line.split('.hdf')
                final_name = line_1[0]+'.hdf'
                print("fin_name:",final_name)
                for j in hdf_dir:
                    if j in final_name:
                        print("fname:",final_name)
                        targets.append(os.path.join(url_base_1,str(final_name.strip())))
        print("previous day target:",targets)
        # a textfile to list all files to be downloaded
        outF = os.path.join(dirname, "mod10A1f_list.txt")
        #write data for download into a text file
        write_file_out(targets, outF)
        #

    else:
        print("onda je full directory and you are in else and you create latest directory ")

        for line in mod10a1f_stripped.split('\n'):
            #if (key[0] in line):
            if (key[0] in line and not key[1] in line):
                line_1 = line.split('.hdf')
                #print("line_1:",line_1)
                final_name = line_1[0]+'.hdf'
                for j in hdf_dir:
                    if j in final_name:
                        print("for inpU:",final_name)
                        targets.append(os.path.join(url_base,str(final_name.strip())))
        print("targets:",targets)
        outF = os.path.join(dirname, "mod10A1f_list.txt")

        # write data for download into a text file
        write_file_out(targets, outF )


    return outF

#generat a textfile to be downloaded
outfile = get_MOD10A1F_hdfs()
print("dirname:",outfile)

#download files from the textfile using 'bitBucket.py" script
saveDir = os.path.dirname(outfile)
files = os.path.basename(outfile)
#download_hdf('-d' saveDir, '-f' files)
com = "python bitBucket.py -d " + saveDir + ' -f ' + outfile
os.system(com)

