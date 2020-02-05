import os, shutil
# folder_path = str(input('Enter the folder path:\t'))
folder = input("Enter the file path:\t")
folder_path = r'{path}'.format(path=folder)
# folder_path = r'F:\Mixed2'
dict_extensions = {
    'audio_extensions' : {1:'.mp3',2:'.wav',3:'.flac'},
    'video_extensions' : {1:'.mp4',2:'.mkv',3:'.MKV',4:'.flv',5:'.mpeg',6:'.m4a'},
    'document_extensions' : {1:'.doc',2:'.pdf',3:'.txt'},
}

def reassemble(folder_path,dict_extensions):
    audio = os.path.join(folder_path,"Audio_folder")
    video = os.path.join(folder_path,"Video_folder")
    doc = os.path.join(folder_path,"Document_folder")

    if(os.path.exists(audio)==0):
        os.makedirs(audio)
    if(os.path.exists(video)==0):
        os.makedirs(video)
    elif(os.path.exists(doc)==0):
        os.makedirs(doc)
    
    for file in os.listdir(folder_path):
        if(file.endswith(dict_extensions['audio_extensions'][1])) or (file.endswith(dict_extensions['audio_extensions'][2])) or (file.endswith(dict_extensions['audio_extensions'][3])):
                t=os.path.join(folder_path,file)
                shutil.move(t,audio)
        elif(file.endswith(dict_extensions['video_extensions'][1])) or (file.endswith(dict_extensions['video_extensions'][2])) or (file.endswith(dict_extensions['video_extensions'][3])) or (file.endswith(dict_extensions['video_extensions'][4])) or (file.endswith(dict_extensions['video_extensions'][5])) or (file.endswith(dict_extensions['video_extensions'][6])):
                t=os.path.join(folder_path,file)
                shutil.move(t,video)
        elif(file.endswith(dict_extensions['document_extensions'][1])) or (file.endswith(dict_extensions['document_extensions'][2])) or (file.endswith(dict_extensions['document_extensions'][3])):
                t=os.path.join(folder_path,file)
                shutil.move(t,doc)
reassemble(folder_path,dict_extensions)
