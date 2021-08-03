from PIL import Image
from zipfile import ZipFile
import requests
import os
import re

Last_Chapter=199
end_folder='Main'
pic_download_directory=r'C:\Users\Lenovo\Desktop\Test\Main\\'
chapter_convertor_directory=r"C:\Users\Lenovo\Desktop\Test\Chapters\\"
Main_Directory=r'C:\Users\Lenovo\Desktop\Test\\'
link="http://images.mangafreak.net:8080/downloads/Kanojo_Okarishimasu_"
name_of_manga="Kanojo Okarishimasu Ch "
image=[]
im1=[]




def delete_element(list_object, pos):
    """Delete element from list at given index
     position (pos) """
    if pos < len(list_object):
        list_object.pop(pos)

######################### Getting the files
for i in range(0,Last_Chapter):
    name=f"{name_of_manga}"+str(i+1)
    link1=link+str(i+1)
    url = link1
    r = requests.get(url, allow_redirects=True)
    with open(f'{end_folder}\\{name}', 'wb')as fff:
        fff.write(r.content)
    with ZipFile(f'{end_folder}\\{name}', 'r') as zip:
        zip.extractall(f"{end_folder}\\")
    os.remove(f'{end_folder}\\{name}')
    j=0
    ####################### Converting and adding to pdf
    for filename in os.listdir(f"{pic_download_directory}"):
        if filename=='error_log':
            os.remove(f'{pic_download_directory}error_log')
    
    for filename in sorted(os.listdir(f"{pic_download_directory}"), key = lambda x: tuple([int(i) for i in re.split(r'_|\.jpg', x)[-3:-1]])):
        f = os.path.join(f"{pic_download_directory}", filename)
        with Image.open(f'{f}') as ff:
            image.append(ff)
            print(f)
            im1.append(image[j].convert('L'))
            j=j+1
    j=0
    im1[0].save(f'{chapter_convertor_directory}'+name+'.pdf',save_all=True, append_images=im1[1:])
    ######################### Refreshing
    image=[]
    im1=[]
    ########################## Deleting
    for filename in os.listdir(f"{end_folder}"):
        f = os.path.join(f"{end_folder}", filename)
        os.remove(f'{Main_Directory}'+f'{f}')

