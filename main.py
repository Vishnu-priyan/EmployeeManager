import tkinter as tk

        
class Employee(tk.Tk):
    def __init__(self,parent):
        tk.Tk.__init__(self,parent)
        self.wm_title("EMPLOYEE MANAGEMENT")
        self.minsize(width=444, height=444)
        self.maxsize(width=444, height=444)
        self.mytitle = tk.Label(self,text = """
-----------------------------------------------------------------------------------------------------------------
                  WELCOME TO EMPLOYEE MANAGEMENT          
                    v1.10              
                      created by Vishnu                  
-----------------------------------------------------------------------------------------------------------------"""
)
        
        self.mytitle.grid(row=0,column=0,columnspan=2)
        self.fname = tk.Label(self,text="First name").grid(row=1)
        self.lname = tk.Label(self,text="Last name").grid(row=2)
        self.dob = tk.Label(self,text="DoB").grid(row=3)
        self.email= tk.Label(self,text="Email").grid(row=4)
        self.qual= tk.Label(self,text="Qualification").grid(row=5)
        
        self.fnameval,self.lnameval,self.dobval\
,self.emailval,self.qualval = tk.StringVar(),tk.StringVar(),\
tk.StringVar(),tk.StringVar(),tk.StringVar()
        
        self.e_fname = tk.Entry(self,textvariable=self.fnameval)
        self.e_lname = tk.Entry(self,textvariable=self.lnameval)
        self.e_dob = tk.Entry(self,textvariable=self.dobval)
        self.e_email = tk.Entry(self,textvariable=self.emailval)
        self.e_qual = tk.Entry(self,textvariable=self.qualval)
        self.e_fname.grid(row=1,column=1)
        self.e_lname.grid(row=2,column=1)
        self.e_dob.grid(row=3,column=1)
        self.e_email.grid(row=4,column=1)
        self.e_qual.grid(row=5,column=1)

        
        self.saveb = tk.Button(self, text="Save Profile", command=self.save_profile)
        self.saveb.grid(row=6,column=0)
        self.viewb = tk.Button(self, text="View Profiles", command=self.view_profile)
        self.viewb.grid(row=6,column=1)

    def save_profile(self):
        window = tk.Toplevel(self)
        window.minsize(width=344, height=344)
        window.maxsize(width=344, height=344)
        label = tk.Label(window,text = "Welcome "+self.e_fname.get())
        label.grid(row=0,column=0)
    
    def view_profile(self):
        window = tk.Toplevel(self)
        window.minsize(width=344, height=344)
        window.maxsize(width=344, height=344)
        label = tk.Label(window,text = "Welcome "+self.e_fname.get())
        label.grid(row=0,column=0)

        
if __name__ == "__main__":
    samp = Employee(None)
    samp.mainloop()
