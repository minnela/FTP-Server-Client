# FTP-Server-Client
FTP Server &amp; Client in Pyhton
import io
from io import StringIO
import shutil
from ftplib import FTP
from tkinter import *
import os
import glob
from tkinter import filedialog

ftp = FTP('')
ftp.connect('localhost',1200)
ftp.login(user='minnela', passwd='italy')
ftp.cwd('.')

os.chdir("C:/istemci")

root = Tk()
root.geometry("1350x700+300+150")
root.resizable(width=True, height=True)


        
def klasor_degistir():
    ftp.cwd('./'+e2.get())
    RemoteServerFileFolderList.delete('1.0', END)
    for i in ftp.nlst():
        RemoteServerFileFolderList.insert(END,str(i)+"\n")

def geri_git():
    ftp.cwd('../')
    RemoteServerFileFolderList.delete('1.0', END)
    for i in ftp.nlst():
        RemoteServerFileFolderList.insert(END,str(i)+"\n")
        
def dosya_ac():
    to_bytes = bytes(acilacakDosyayaVerilecekString.get(), "UTF-8")
    yazilacak_yazı = io.BytesIO(to_bytes)
    ftp.storbinary('STOR '+acilacakDosya.get(), yazilacak_yazı)
    RemoteServerFileFolderList.delete('1.0', END)
    for i in ftp.nlst():
        RemoteServerFileFolderList.insert(END,str(i)+"\n")
    
def klasor_ac():
    ftp.mkd(uzakSunucudaAcilacakKlasor.get())
    RemoteServerFileFolderList.delete('1.0', END)
    for i in ftp.nlst():
        RemoteServerFileFolderListinsert(END,str(i)+"\n")
        
def dosya_sil():
    ftp.delete(silinecekDosya.get())
    RemoteServerFileFolderList.delete('1.0', END)
    for i in ftp.nlst():
        RemoteServerFileFolderList.insert(END,str(i)+"\n")

def klasor_sil():
    ftp.rmd(silinecekKlasor.get())
    RemoteServerFileFolderList.delete('1.0', END)
    for i in ftp.nlst():
        RemoteServerFileFolderList.insert(END,str(i)+"\n")


def dosya_indir():
    targerfilename = 'C:/istemci/'+str(indirilecekDosyaIsmi.get()) 
    localfile = open(targerfilename, 'wb')
    ftp.retrbinary('RETR '+str(indirilecekDosyaIsmi.get()), localfile.write, 1200)
    localfile.close()
    T2.delete('1.0', END)
    for file in os.listdir(os.getcwd()):
        T2.insert(END,str(file)+"\n")        
        
def adini_degistir():
    ftp.rename(isimiDegisecekDosya.get(), isimiDegisecekDosyaYeniIsim.get())
    RemoteServerFileFolderList.delete('1.0', END)
    for i in ftp.nlst():
        RemoteServerFileFolderList.insert(END,str(i)+"\n")
                
###########################################################################################################        
def change_working_directory_local():
    os.chdir('./'+e4.get()) #./ = ŞU ANKİ DOSYA DİZİNİNİ İFADE EDİYOR
    T2.delete('1.0', END)
    for file in os.listdir(os.getcwd()):
        T2.insert(END,str(file)+"\n")

def go_back_local():
    if os.getcwd() != ("C:\istemci"):
        os.chdir('../') # ../ = BİR ÜST DOSYAYA GİT. Bİ ÖNCEKİ DOSYA
    T2.delete('1.0', END)
    for file in os.listdir(os.getcwd()):
        T2.insert(END,str(file)+"\n")
        
def uploadFile():
    filename = download_filename_entry2.get() 
    ftp.storbinary('STOR '+filename, open(os.getcwd()+"/"+filename, 'rb'))
    RemoteServerFileFolderList.delete('1.0', END)
    for i in ftp.nlst():
        RemoteServerFileFolderList.insert(END,str(i)+"\n")
        
def createFileLocal():
    file = open(create_file_local.get(), "w+") 
    file.write(create_file_local_input_text.get()) 
    file.close()
    T2.delete('1.0', END)
    for file in os.listdir(os.getcwd()):
        T2.insert(END,str(file)+"\n")
        
def deleteFileLocal():
    os.remove(delete_filename_entry_local.get())
    T2.delete('1.0', END)
    for file in os.listdir(os.getcwd()):
        T2.insert(END,str(file)+"\n")

def deleteDirectoryLocal():
    dirname = os.getcwd()+"\\"+delete_directory_entry_local.get()
    dirname=dirname.replace('\\','/')
    shutil.rmtree(dirname)
    T2.delete('1.0', END)
    for file in os.listdir(os.getcwd()):
        T2.insert(END,str(file)+"\n")
        
def renameFileLocal():
    os.rename(rename_file_local_first.get(),rename_file_local_last.get())
    T2.delete('1.0', END)
    for file in os.listdir(os.getcwd()):
        T2.insert(END,str(file)+"\n")    
        

def createDirectoryOnLocal():
    os.mkdir(create_directory_on_local_directory_name.get())
    T2.delete('1.0', END)
    for file in os.listdir(os.getcwd()):
        T2.insert(END,str(file)+"\n")   

    


# In[ ]:


#indirme yeri
l = Label(root,text="İndirme Bölgesi").place(x=10,y=5)
e = Entry(root)
e.insert(END, 'C:/istemci')
e.configure(state='readonly')
e.place(x=120,y=5)        
        
#UZAK SUNUCU DOSYALARI
remote_server_label = Label(root,text="Uzak sunucu dosyaları").place(x=5,y=40)
RemoteServerFileFolderList = Text(root, height=20, width=35)
RemoteServerFileFolderList.place(x=5,y=60)

for i in ftp.nlst():
    RemoteServerFileFolderList.insert(END,str(i)+"\n")  

#uzak sunucuda klasor acmak
remote_server_label = Label(root,text="Klasör Aç").place(x=5,y=400)
uzakSunucudaAcilacakKlasor = Entry(root)
uzakSunucudaAcilacakKlasor.place(x=100,y=400)
btn = Button(root, text='Klasörü Yarat', command=klasor_ac).place(x=200,y=395)
l = Label(root,text="♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫").place(x=5,y=440)


#klasor degistirmek
e2 = Entry(root)
e2.insert(END, '')
e2.place(x=300,y=60)
btn = Button(root, text='Çalışma Klasörünü Değiştir', command=klasor_degistir).place(x=430,y=55)
#geri gitmek
btn = Button(root, text='GoBack', command=geri_git).place(x=580,y=55)


#uzaktan dosya indirmek
btn = Button(root, text='Dosyayı İndir', command=dosya_indir).place(x=430,y=85)
indirilecekDosyaIsmi = Entry(root)
indirilecekDosyaIsmi.place(x=300,y=90)
l = Label(root,text="✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ").place(x=300,y=125)

#sunucuda dosya aç
btn = Button(root, text='Dosya Aç', command=dosya_ac).place(x=220,y=470)
l = Label(root,text="Dosya Adı").place(x=5,y=470)
acilacakDosya = Entry(root)
acilacakDosya.place(x=95,y=470)
l = Label(root,text="Yazılacak Yazı").place(x=5,y=500)
acilacakDosyayaVerilecekString = Entry(root)
acilacakDosyayaVerilecekString.place(x=95,y= 500)


#sunucudan dosya sil
btn = Button(root, text='Dosyayı sil', command=dosya_sil).place(x=430,y=175)
silinecekDosya = Entry(root)
silinecekDosya.place(x=300,y=180)

#sunucudan klasör silme
btn = Button(root, text='Klasörü sil', command=klasor_sil).place(x=430,y=205)
silinecekKlasor = Entry(root)
silinecekKlasor.place(x=300,y=210)

#yeniden adlandırma
btn = Button(root, text='Yeniden Adlandir', command=adini_degistir).place(x=530,y=310)
l = Label(root,text="Dosya ismi").place(x=300,y=300)
isimiDegisecekDosya = Entry(root)
isimiDegisecekDosya.place(x=400,y=305)
l = Label(root,text="Yeni isim").place(x=300,y=330)
isimiDegisecekDosyaYeniIsim = Entry(root)
isimiDegisecekDosyaYeniIsim.place(x=400,y= 330)

####################################################################################################

#UPLOAD DIRECTORY
l = Label(root,text="Yükleme Bölgesi").place(x=705,y=5)
e = Entry(root)
e.insert(END, 'C:/uzakdizin')
e.configure(state='readonly')
e.place(x=805,y=5)   


#LOCAL FILES
remote_server_label = Label(root,text="Local Files (C:/istemci)").place(x=705,y=40)
T2 = Text(root, height=20, width=35)
T2.place(x=705,y=60)


for file in os.listdir(os.getcwd()):
    T2.insert(END,str(file)+"\n")

#CHANGE DIRECTORY
e4 = Entry(root)
e4.insert(END, '')
e4.place(x=1000,y=60)
btn = Button(root, text='Çalışma klasörünü değiştir', command=change_working_directory_local).place(x=1130,y=55)
l = Label(root,text="⚝ ⚝ ⚝ ⚝ ⚝ ⚝ ⚝ ⚝ ⚝ ⚝ ⚝ ⚝ ⚝ ⚝ ⚝ ⚝ ⚝ ⚝ ⚝ ⚝ ⚝ ⚝ ").place(x=1000,y=120)
#GO BACK
btn = Button(root, text='Geri', command=go_back_local).place(x=1280,y=55)


#UPLOAD FILE 
btn = Button(root, text='Dosya Yükle', command=uploadFile).place(x=1130,y=85)
download_filename_entry2 = Entry(root)
download_filename_entry2.place(x=1000,y=90)

#CREATE DIRECTORY ON LOCAL 
remote_server_label = Label(root,text="Klasör yarat").place(x=700,y=400)
create_directory_on_local_directory_name = Entry(root)
create_directory_on_local_directory_name.place(x=800,y=400)
btn = Button(root, text='Klasör yarat', command=createDirectoryOnLocal).place(x=900,y=395)    

#CREATE FILE 
btn = Button(root, text='Dosya yarat', command=createFileLocal).place(x=920,y=460)
l = Label(root,text="Dosya ismi").place(x=700,y=450)
create_file_local = Entry(root)
create_file_local.place(x=800,y=450)
l = Label(root,text="Yazılacak yazı").place(x=700,y=475)
create_file_local_input_text = Entry(root)
create_file_local_input_text.place(x=800,y= 475)

#DELETE FILE FROM LOCAL
btn = Button(root, text='Dosyayı sil', command=deleteFileLocal).place(x=1150,y=175)
delete_filename_entry_local = Entry(root)
delete_filename_entry_local.place(x=1000,y=180)

#DELETE DIRECTORY FROM LOCAL
btn = Button(root, text='Klasörü sil', command=deleteDirectoryLocal).place(x=1150,y=200)
delete_directory_entry_local = Entry(root)
delete_directory_entry_local.place(x=1000,y=205)

#RENAMING REMOTE FILE
btn = Button(root, text='Yeniden Adlandır', command=renameFileLocal).place(x=1225,y=310)
l = Label(root,text="Dosya ismi").place(x=1000,y=300)
rename_file_local_first = Entry(root)
rename_file_local_first.place(x=1080,y=305)
l = Label(root,text="Yeni isim").place(x=1000,y=330)
rename_file_local_last = Entry(root)
rename_file_local_last.place(x=1080,y= 330)
l = Label(root,text="Minnela’s Work").place(x=900,y=600)


# In[ ]:


root.mainloop()

print("done")


# In[ ]:




