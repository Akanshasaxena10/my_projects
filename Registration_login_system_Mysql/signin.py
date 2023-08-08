from tkinter import*
import tkinter as tk
import PIL
from PIL import Image,ImageTk##to convert jpg images to jpg to png format.##PYTHON IMAGE LIBRARY


'''Functions'''
'''sign up page link'''
def signup_page():
    login_window.destroy()
    import signup

'''To clear the field once input cursor is there'''
def user_enter(event):###if username input is at username entry  then it will delete pre-written username.
    if usernameEntry.get() == 'UserName':
        usernameEntry.delete(0,END)
        
def password_enter(event):###if passwordinput is at password entry  then it will delete pre-written password.
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0,END)   
'''To hide the password and close the open eye while entering the password'''        
def hide(): ###using config method in hid function or command
    openeye.config(file='closeye.png')  
    passwordEntry.config(show='*')####to hide input text
    eyeButton.config(command=show)  
'''To show the text on the frame of password show function or command'''   
def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='') ##to show input text
    eyeButton.config(command=hide)       
    
    
'''Window'''
login_window =Tk()##root is the variable or object created to access the methods of TK class.
login_window.geometry('990x660+50+50')
login_window.resizable(0,0)##To fix the window size.
login_window.title('LOGIN PAGE')

'''Background of window'''
bg_Image = ImageTk.PhotoImage(file='bg.jpg')##created object to access bg image.
bg_Label = Label(login_window,image =bg_Image)##to add bg image to our window create a bg label with a label class.
bg_Label.place(x=0,y=0)##placing and positioning the image we use grid or place or pack method.

'''Text on window'''
heading = Label(login_window,text = 'USER LOGIN',font = ('Microsoft Yahei UI Light',23,'bold'),bg ='black',fg ='firebrick1')##added text on label
heading.place(x= 605,y = 120)

''''creating user input field'''
usernameEntry =Entry(login_window,width = 25,font =('Microsoft Yahei UI Light',11,'bold',),bd =0,fg ='firebrick1')##using Enter class for username input
usernameEntry.place(x= 580,y = 200)
usernameEntry.insert(0,'UserName')##column for username input
usernameEntry.bind('<FocusIn>',user_enter)##using binding method to Bind the entry method with function on_enter to give functionality.
'''adding frame to username'''
frame1 =Frame(login_window,width=250,height=2,bg='firebrick1')
frame1.place(x=580,y=222)###using frame class inside the login window for username input

'''creating password entry'''
passwordEntry =Entry(login_window,width = 25,font =('Microsoft Yahei UI Light',11,'bold',),bd =0,fg ='firebrick1')##using Enter class for username input
passwordEntry.place(x= 580,y = 260)
passwordEntry.insert(0,'Password')##column for password input
passwordEntry.bind('<FocusIn>',password_enter)##using binding method to Bind the entry method with function on_enter to give functionality.
'''adding frame to password'''
frame2 =Frame(login_window,width=250,height=2,bg='firebrick1')
frame2.place(x=580,y=282)###using frame class inside the login window for passwordinput

'''show/open eye image'''
openeye = PhotoImage(file='openeye.png')
eyeButton = Button(login_window,image=openeye,bd=0,bg='white',activebackground ='white',cursor ='hand2',command=hide)
eyeButton.place(x=800,y=255)

'''Forget password button'''
forgetButton = Button(login_window,text='Forgot Password',bd=0,bg='white',activebackground ='firebrick1',cursor ='hand2',
               font =('Microsoft Yahei UI Light',9,'bold'),fg ='firebrick1')
forgetButton.place(x=715,y=295)

'''login button'''
loginButton = Button(login_window,text='Login',font=('Open sans',16,'bold'),fg ='white',bg='firebrick1',activeforeground='white',activebackground='firebrick1',
                     cursor='hand2',bd=0,width=18)
loginButton.place(x=553,y=350)

'''or label'''
orLabel = Label(login_window,text='------------OR--------------',font=('Open Sans',16),fg='firebrick1',bg='white')
orLabel.place(x=583,y=400)

''''adding logo'''
facebook_logo =PhotoImage(file='facebook.png')
fbLabel=Label(login_window,image=facebook_logo,bg='white')
fbLabel.place(x=640,y=440)

google_logo =PhotoImage(file='google.png')
googleLabel=Label(login_window,image=google_logo,bg='white')
googleLabel.place(x=690,y=440)

twitter_logo =PhotoImage(file='twitter.png')
twitterLabel=Label(login_window,image=twitter_logo,bg='white')
twitterLabel.place(x=740,y=440)

'''Bottom button'''
signupLabel = Label(login_window,text='Do not have an account? ',font=('Open Sans',10,'bold'),fg='firebrick1',bg='white')
signupLabel.place(x=620,y=480)

'''Create an account button'''
newaccountButton = Button(login_window,text='Create New Account',font=('Open sans',9,'bold underline'),fg ='white',bg='firebrick1',activeforeground='blue',activebackground='white',
                     cursor='hand2',bd=0,width=18,command=signup_page)
newaccountButton.place(x=628,y=500)


login_window.mainloop()##method to create window 
