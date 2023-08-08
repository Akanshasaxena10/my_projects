from tkinter import *
from PIL import ImageTk



'''add functionality to log in button to login page'''
def login_page():
    signup_window.destroy()##to clean the signup window to reach to login page
    import signin
    

signup_window = Tk()##tk class for window
signup_window.title('Signup Page')##title method
signup_window.resizable(False,False)

background = ImageTk.PhotoImage(file = 'bg.jpg')##created image object

bgLaabel = Label(signup_window,image = background)
bgLaabel.grid()##grid method -it gives rows and columns on the window..by default it is 0 and 0
'''creating a frame to include the signup window '''
frame = Frame(signup_window,bg='white')##frame class will have the sign up window with object frame
frame.place(x=554,y=140,)

heading = Label(frame,text = 'CREATE AN ACCOUNT',font = ('Microsoft Yahei UI Light',16,'bold'),bg ='black',fg ='firebrick1')##added text on label
heading.grid(row = 0,column= 0,padx=15,pady=10)

'''Creating rows for sign up window entry details'''
emailLabel = Label(frame,text='Email',font = ('Microsoft Yahei UI Light',12,'bold'),bg ='white',fg ='firebrick1')
emailLabel.grid(row=1,column=0,sticky='W',padx=25)

emailEntry = Entry(frame,width=25,font=('Microsoft Yahei UI Light',12,'bold'),bg ='firebrick1',fg ='black')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

'''username row'''
usernameLabel = Label(frame,text='Username',font = ('Microsoft Yahei UI Light',12,'bold'),bg ='white',fg ='firebrick1')
usernameLabel.grid(row=3,column=0,sticky='W',padx=25)

usernameEntry = Entry(frame,width=25,font=('Microsoft Yahei UI Light',12,'bold'),bg ='firebrick1',fg ='black')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

'''password row'''
passwordLabel = Label(frame,text='Password',font = ('Microsoft Yahei UI Light',12,'bold'),bg ='white',fg ='firebrick1')
passwordLabel.grid(row=5,column=0,sticky='W',padx=25)

passwordEntry = Entry(frame,width=25,font=('Microsoft Yahei UI Light',12,'bold'),bg ='firebrick1',fg ='black')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)

'''Confirm password'''
conpasswordLabel = Label(frame,text='Confirm Password',font = ('Microsoft Yahei UI Light',12,'bold'),bg ='white',fg ='firebrick1')
conpasswordLabel.grid(row=7,column=0,sticky='W',padx=25)

conpasswordEntry = Entry(frame,width=25,font=('Microsoft Yahei UI Light',12,'bold'),bg ='firebrick1',fg ='black')
conpasswordEntry.grid(row=8,column=0,sticky='w',padx=25)

termsandconditions = Checkbutton(frame,text='I agree to the Terms & Conditions',font=('Microsoft Yahei UI Light',10,'bold'),fg ='firebrick1',bg ='white', activebackground ='firebrick1',activeforeground='white',cursor='hand2')
termsandconditions.grid(row=9,column=0,pady=15,padx=10)

'''signup button'''

signupButton = Button(frame,text='Signup',font=('Open Sans',18,'bold'),bd=0,bg='firebrick1',fg='white',activebackground='firebrick1',activeforeground='white',width=10)
signupButton.grid(row=10,column=0,pady=10)

'''redirect button'''
alredyaccountLabel = Label(frame,text="Don't have an account?",font=('Open Sans','12','bold'),bg='white',fg='firebrick1')
alredyaccountLabel.grid(row=11,column=0,sticky='w',padx=25,pady=10)

loginButton = Button(frame,text='Log in',font=('Open Sans',12,'bold underline'),bg='white',fg='blue',bd=0,cursor='hand2',activebackground='white',activeforeground='blue',command=login_page)
loginButton.place(x=240,y=360)
signup_window.mainloop()##using mainloop 