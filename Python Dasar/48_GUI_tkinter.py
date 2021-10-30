import tkinter

main_window = tkinter.Tk()          #membuat gui program

def event_tekan():
    label2 = tkinter.Label(main_window, text = "berhasil ditekan ")
    label2.pack()

label = tkinter.Label(main_window,text = "halo, saya adalah \nGUI sederhana \ndengan menggunakan python")
tombol = tkinter.Button(main_window,text = "KLIK DISINI",command = event_tekan)

label.pack()
tombol.pack()
main_window.mainloop()