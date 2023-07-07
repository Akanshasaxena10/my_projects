from tkinter import*
from tkinter import ttk
from PIL import Image
from PIL import ImageTk


class Login_Window:##class-login-window
    '''creating window for the registration_login system.root means window here'''
    def __init__(self,root):##constructor-initialize
        self.root = root
        self.root.title('Login')
        self.root.geometry('1550x800+0+0')##height,width,x axis and y axis.
        
        self.bg = ImageTk.PhotoImage(file = r'/home/user/Desktop/git_mywork/my_projects/Registration_login_system_Mysql/Summer-Desktop-Wallpaper-HD-Free-download-620x349.jpg/Summer-Desktop-Wallpaper-HD-Free-download-620x349.jpg')
        lbl_bg = Label(self.root,image = self.bg)###with the help of label will show the image
        lbl_bg.place(x=0,y=0, relwidth = 1, relheight = 1)##setting the picture
        
        
        
        
        
''''creating object to call the main'''        
if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)##created app object to run the window that is root.Passing root to login window.
    root.mainloop()       