from moviepy.video.io.VideoFileClip import VideoFileClip
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os


print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"+
      "Welcome to Whatsapp video splitter v_1.0.0\n"+
      "copyrights nilanka manoj www.github.com/nilankamanoj\n"+
      "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n"+
      "select video file from file browser : \n\n")
Tk().withdraw()
file_name = askopenfilename()
print(file_name)


clip = VideoFileClip(file_name)
if(clip.duration/30 > int(clip.duration/30)):
        clip_count = int(clip.duration/30) + 1
else:
        clip_count = int(clip.duration/30)

print( str(clip.duration) + " for "+ str(clip_count)+" clips" )

save_path = "C:\\Users\\"+os.getlogin()+"\\Videos\\Whatsapp_splitter\\" + file_name.split("/")[-1].split(".")[0] + "\\"

if not os.path.exists(save_path):
	os.makedirs(save_path)
def get_first(i):
        with VideoFileClip(file_name) as video:
                new = video.subclip(0, 30)
                new.write_videofile(save_path+"clip0.mp4", audio_codec='aac')
                

def get_i(i):
        with VideoFileClip(file_name) as video:
                new = video.subclip((i*30), (i+1)*30)
                new.write_videofile(save_path+"clip"+str(i)+".mp4", audio_codec='aac')
                

def get_last(i):
        with VideoFileClip(file_name) as video:
                new = video.subclip((clip_count-1)*30, clip.duration)
                new.write_videofile(save_path+"clip"+str(clip_count-1)+".mp4", audio_codec='aac')
                
        
        

get_first(0)
        
for i in range(1, clip_count-1):	
        get_i(i)

get_last(0)

            
