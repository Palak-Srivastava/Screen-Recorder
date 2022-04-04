from tkinter import *
import pyscreenrec

root=Tk()
root.geometry("400x600")
root.title("Screen Recorder")
root.config(bg="#000")
root.resizable(False,False)

def start_rec():
	file=Filename.get()
	rec.start_recording(str(file+".mp4"),5)

def pause_rec():
	rec.pause_recording()

def resume_rec():
	rec.resume_recording()

def stop_rec():
	rec.stop_recording()

rec=pyscreenrec.ScreenRecorder()

#icon
image_icon=PhotoImage(file="icon.png")
root.iconphoto(False,image_icon)

#background images
image1=PhotoImage(file="yelllow.png")
Label(root,image=image1,bg="#000").place(x=-2,y=80)

image2=PhotoImage(file="blue.png")
Label(root,image=image2,bg="#000").place(x=223,y=200)

#heading
lbl=Label(root,text="Screen Recorder",bg="#000",font="poppins 23 bold",fg="#fff")
lbl.pack(pady=20)

image3=PhotoImage(file="recording.png")
Label(root,image=image3,bd=2).pack(pady=30)

#entry
Filename=StringVar()
entry=Entry(root,textvariable=Filename,width=15,font="poppins 15")
entry.place(x=120,y=360)
file=Filename.set("   Display Name")

#button
start=Button(root,text="Start",font="poppins 25 bold",bg="#fff",fg="#000",bd=0,command=start_rec)
start.place(x=132,y=260)

image4=PhotoImage(file="pause.png")
pause=Button(root,image=image4,bd=0,bg="#000",command=pause_rec)
pause.place(x=60,y=470)

image5=PhotoImage(file="resume.png")
resume=Button(root,image=image5,bd=0,bg="#000",command=resume_rec)
resume.place(x=160,y=470)

image6=PhotoImage(file="stop.png")
stop=Button(root,image=image6,bd=0,bg="#000",command=stop_rec)
stop.place(x=260,y=470)

root.mainloop()