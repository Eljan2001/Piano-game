from tkinter import*
import os
import time
import random
menu=Tk()
menu.title('Menu')
menu.geometry('500x500+700+300')
canvas_1=Canvas(menu, width=500, height=500, bg='#000000')
canvas_1.pack()
canvas_1.create_text(245, 50, text='Menu', font=('Times', 40),  fill='blue') 

def onclick():
    menu.destroy()
    gamemode=Tk()
    gamemode.title('Gamemodes')
    gamemode.geometry('500x500+700+300')
    canvas_2=Canvas(gamemode, width=500, height=500, bg='#000000')
    canvas_2.pack()
    canvas_2.create_text(245, 50, text='Gamemodes', font=('Times', 40),  fill='blue') 

    def Easy():
        gamemode.destroy()
        root=Tk()
        root.title('Custom Game')
        root.geometry('500x600+700+300')
        root.wm_attributes('-topmost', 1)
        canvas=Canvas(root,width=500, height=600, bg='#000000')
        canvas.pack()
        canvas.create_text(245, 540, text='Score:', font=('Times', 30), fill='red') 
        
        canvas.create_rectangle(0,501,500,600,outline='white')
        margin6=canvas.create_rectangle(0,0,100,500, fill='yellow')
        margin7=canvas.create_rectangle(400,0,500,500, fill='yellow')
        margin1=canvas.create_rectangle(0,0,100,500, fill='blue')
        margin2=canvas.create_rectangle(400,0,500,500, fill='blue')

        


        variable=0

        canvas.tag_lower(margin6)
        canvas.tag_lower(margin7)
        

        COLOURS_LIST=['red', 'lightgreen']
        L=[]
        L1=[]
        L2=[0]
        L3=[0]

        class Notes:

            def __init__(self, canvas, variable):
                self.canvas=canvas
                self.variable=variable
                random_colour=random.choice(COLOURS_LIST)
                L.append(random_colour)
                self.id=canvas.create_rectangle(100, 0, 250, 250, fill=random_colour)

                if random_colour=='red':
                    random_colour='lightgreen'

                elif random_colour=='lightgreen':
                    random_colour='red'

                L1.append(random_colour)
                self.id2=canvas.create_rectangle(250, 0, 400, 250, fill=random_colour)
                self.canvas.bind_all('<KeyPress-Left>', self.main_command)
                self.canvas.bind_all('<KeyPress-Right>', self.main_command2)
                self.id3=canvas.create_text(320, 540, text=L3[0], font=('Times', 30), fill='red')

            def draw(self):
                self.canvas.move(self.id, 0, 3)
                self.canvas.move(self.id2, 0, 3)

            def eternal_loop(self):
                pos=self.canvas.coords(self.id)
                self.canvas=canvas
                random_colour=random.choice(COLOURS_LIST)
                    
                if pos[3]>=500:
                    if self.variable==0:
                        
                        L3[0]-=10
                        if L3[0]==-100:
                            root.destroy()
                            root1=Tk()
                            root1.geometry('500x500+700+300')
                            canvas1=Canvas(root1, width=500, height=500)
                            canvas1.pack()
                            canvas1.create_text(245,100,text='Game Over', font=('Times', 30))
                            canvas1.create_text(245,150,text='Your Score is:', font=('Times', 30))
                            Score=canvas1.create_text(400,150,text=L3[0], font=('Times', 30))

                            def restart():
                                root1.destroy()
                                os.startfile(r'C:\Users\elcan\Desktop/custom game.py')

                            btn=Button(root1, text='restart',font=('Times', 15), bg='#ffcc00', fg='#000000', width=30, height=3, state='normal', command=restart)
                            btn.place(x=80, y=240)
                            root1.mainloop()
                    self.variable=0
                    L[0]=random_colour
                    canvas.delete(self.id)
                    canvas.delete(self.id2)
                    canvas.delete(self.id3)
                    self.id=canvas.create_rectangle(100, 0, 250, 250, fill=random_colour)

                    if random_colour=='red':
                        random_colour='lightgreen'

                    elif random_colour=='lightgreen':
                        random_colour='red'

                    L1[0]=random_colour
                    self.id2=canvas.create_rectangle(250, 0, 400, 250, fill=random_colour)
                    self.id3=canvas.create_text(320, 540, text=L3[0], font=('Times', 30), fill='red')

            
                
                
            def main_command(self, evt):
                pos=self.canvas.coords(self.id)

                if self.variable==0:
                    
                    if L[0]=='red':
                        root.destroy()
                        root1=Tk()
                        root1.geometry('500x500+700+300')
                        canvas1=Canvas(root1, width=500, height=500)
                        canvas1.pack()
                        canvas1.create_text(245,100,text='Game Over', font=('Times', 30))
                        canvas1.create_text(245,150,text='Your Score is:', font=('Times', 30))
                        Score=canvas1.create_text(400,150,text=L3[0], font=('Times', 30))

                        def restart():
                            root1.destroy()
                            os.startfile(r'C:\Users\elcan\Desktop/custom game.py')

                        btn=Button(root1, text='restart',font=('Times', 15), bg='#ffcc00', fg='#000000', width=30, height=3, state='normal', command=restart)
                        btn.place(x=80, y=240)
                        root1.mainloop()

                    elif L3[0]==190:
                        root.destroy()
                        root1=Tk()
                        root1.geometry('500x500+700+300')
                        canvas1=Canvas(root1, width=500, height=500)
                        canvas1.pack()
                        canvas1.create_text(245,100,text='Success', font=('Times', 30))
                        canvas1.create_text(245,150,text='Your Score is:', font=('Times', 30))                        
                        Score=canvas1.create_text(400,150,text=L3[0]+10, font=('Times', 30))

                        def restart():
                            root1.destroy()
                            os.startfile(r'C:\Users\elcan\Desktop/custom game.py')

                        btn=Button(root1, text='Menu',font=('Times', 15), bg='#ffcc00', fg='#000000', width=30, height=3, state='normal', command=restart)
                        btn.place(x=80, y=240)
                        root1.mainloop()

                    elif L[0]!='red':
                        canvas.delete(self.id)
                        self.id=canvas.create_rectangle(pos, fill='white')
                        L2[0]+=10
                        L3[0]+=10

                        if pos[3]>=500:
                            canvas.delete(self.id)

                    self.variable+=1    

            def main_command2(self, evt):
                pos2=self.canvas.coords(self.id2)

                if self.variable==0:

                    if L1[0]=='red':
                        root.destroy()
                        root1=Tk()
                        root1.geometry('500x500+700+300')
                        canvas1=Canvas(root1, width=500, height=500)
                        canvas1.pack()
                        canvas1.create_text(245,100,text='Game Over', font=('Times', 30))
                        canvas1.create_text(245,150,text='Your Score is:', font=('Times', 30))
                        Score=canvas1.create_text(400,150,text=L3[0], font=('Times', 30))

                        def restart():
                            root1.destroy()
                            os.startfile(r'C:\Users\elcan\Desktop/custom game.py')

                        btn=Button(root1, text='Menu',font=('Times', 15), bg='#ffcc00', fg='#000000', width=30, height=3, state='normal', command=restart)
                        btn.place(x=80, y=240)
                        root1.mainloop()

                    elif L3[0]==190:
                        root.destroy()
                        root1=Tk()
                        root1.geometry('500x500+700+300')
                        canvas1=Canvas(root1, width=500, height=500)
                        canvas1.pack()
                        canvas1.create_text(245,100,text='Success', font=('Times', 30))
                        canvas1.create_text(245,150,text='Your Score is:', font=('Times', 30))                        
                        Score=canvas1.create_text(400,150,text=L3[0]+10, font=('Times', 30))

                        def restart():
                            root1.destroy()
                            os.startfile(r'C:\Users\elcan\Desktop/custom game.py')

                        btn=Button(root1, text='Menu',font=('Times', 15), bg='#ffcc00', fg='#000000', width=30, height=3, state='normal', command=restart)
                        btn.place(x=80, y=240)
                        root1.mainloop()

                    elif L1[0]!='red':
                        
                        canvas.delete(self.id2)
                        self.id2=canvas.create_rectangle(pos2, fill='white')
                        L2[0]+=10
                        L3[0]+=10

                        if pos2[3]>=500:
                            canvas.delete(self.id2)

                    self.variable+=1

        notes=Notes(canvas, variable)
        z=2    
        variable=1
        
        while 1:
            notes.draw()
            notes.eternal_loop()
            t=time.perf_counter()

            if variable==1:
                z=t+1
                variable+=1

            if t>=z-0.5 and t<=z:
                canvas.tag_raise(margin6)
                canvas.tag_raise(margin7)
                
                
            if t>=z and t<=z+0.5:
                canvas.tag_lower(margin6)
                canvas.tag_lower(margin7)
                
                z+=1
            root.update()
            root.update_idletasks()
            time.sleep(0.01)
            
            
        root.mainloop()

    def Medium():
        gamemode.destroy()
        root=Tk()
        root.title('Custom Game')
        root.geometry('500x600+700+300')
        root.wm_attributes('-topmost', 1)
        canvas=Canvas(root,width=500, height=600, bg='#000000')
        canvas.pack()
        
        
        canvas.create_rectangle(0,501,500,600,outline='white')
        margin6=canvas.create_rectangle(0,0,100,500, fill='yellow')
        margin7=canvas.create_rectangle(400,0,500,500, fill='yellow')
        canvas.create_text(245, 540, text='Score:', font=('Times', 30), fill='red') 
        L2=[0]

        margin1=canvas.create_rectangle(0,0,100,500, fill='blue')
        margin2=canvas.create_rectangle(400,0,500,500, fill='blue')

        



        canvas.tag_lower(margin6)
        canvas.tag_lower(margin7)
        
        variable=0
        COLOURS_LIST=['red', 'lightgreen']
        L=[]
        L1=[]
        L3=[0]

        class Notes:

            def __init__(self, canvas, variable):
                self.canvas=canvas
                self.variable=variable
                random_colour=random.choice(COLOURS_LIST)
                L.append(random_colour)
                self.id=canvas.create_rectangle(100, 0, 250, 250, fill=random_colour)

                if random_colour=='red':
                    random_colour='lightgreen'

                elif random_colour=='lightgreen':
                    random_colour='red'

                L1.append(random_colour)
                self.id2=canvas.create_rectangle(250, 0, 400, 250, fill=random_colour)
                self.canvas.bind_all('<KeyPress-Left>', self.main_command)
                self.canvas.bind_all('<KeyPress-Right>', self.main_command2)
                self.id3=canvas.create_text(320, 540, text=L3[0], font=('Times', 30), fill='red')

            def draw(self):
                self.canvas.move(self.id, 0, 4)
                self.canvas.move(self.id2, 0, 4)


            def eternal_loop(self):
                pos=self.canvas.coords(self.id)
                self.canvas=canvas
                random_colour=random.choice(COLOURS_LIST)
                    
                if pos[3]>=500:
                    if self.variable==0:
                        L3[0]-=10
                        if L3[0]==-100:
                            root.destroy()
                            root1=Tk()
                            root1.geometry('500x500+700+300')
                            canvas1=Canvas(root1, width=500, height=500)
                            canvas1.pack()
                            canvas1.create_text(245,100,text='Game Over', font=('Times', 30))
                            canvas1.create_text(245,150,text='Your Score is:', font=('Times', 30))
                            Score=canvas1.create_text(400,150,text=L3[0], font=('Times', 30))

                            def restart():
                                root1.destroy()
                                os.startfile(r'C:\Users\elcan\Desktop/custom game.py')

                            btn=Button(root1, text='restart',font=('Times', 15), bg='#ffcc00', fg='#000000', width=30, height=3, state='normal', command=restart)
                            btn.place(x=80, y=240)
                            root1.mainloop()
                    self.variable=0
                    L[0]=random_colour
                    canvas.delete(self.id)
                    canvas.delete(self.id2)
                    canvas.delete(self.id3)
                    self.id=canvas.create_rectangle(100, 0, 250, 250, fill=random_colour)

                    if random_colour=='red':
                        random_colour='lightgreen'

                    elif random_colour=='lightgreen':
                        random_colour='red'

                    L1[0]=random_colour
                    self.id2=canvas.create_rectangle(250, 0, 400, 250, fill=random_colour)
                    self.id3=canvas.create_text(320, 540, text=L3[0], font=('Times', 30), fill='red')

            def main_command(self, evt):
                pos=self.canvas.coords(self.id)

                if self.variable==0:

                    if L[0]=='red':
                        root.destroy()
                        root1=Tk()
                        root1.geometry('500x500+700+300')
                        canvas1=Canvas(root1, width=500, height=500)
                        canvas1.pack()
                        canvas1.create_text(245,100,text='Game Over', font=('Times', 30))
                        canvas1.create_text(245,150,text='Your Score is:', font=('Times', 30))
                        Score=canvas1.create_text(400,150,text=L3[0], font=('Times', 30))

                        def restart():
                            root1.destroy()
                            os.startfile(r'C:\Users\elcan\Desktop/custom game.py')

                        btn=Button(root1, text='restart',font=('Times', 15), bg='#ffcc00', fg='#000000', width=30, height=3, state='normal', command=restart)
                        btn.place(x=80, y=240)
                        root1.mainloop()

                    elif L3[0]==240:
                        root.destroy()
                        root1=Tk()
                        root1.geometry('500x500+700+300')
                        canvas1=Canvas(root1, width=500, height=500)
                        canvas1.pack()
                        canvas1.create_text(245,100,text='Success', font=('Times', 30))
                        canvas1.create_text(245,150,text='Your Score is:', font=('Times', 30))                        
                        Score=canvas1.create_text(400,150,text=L3[0]+10, font=('Times', 30))

                        def restart():
                            root1.destroy()
                            os.startfile(r'C:\Users\elcan\Desktop/custom game.py')

                        btn=Button(root1, text='Menu',font=('Times', 15), bg='#ffcc00', fg='#000000', width=30, height=3, state='normal', command=restart)
                        btn.place(x=80, y=240)
                        root1.mainloop()

                    elif L[0]!='red':
                        canvas.delete(self.id)
                        self.id=canvas.create_rectangle(pos, fill='white')
                        L2[0]+=10
                        L3[0]+=10

                        if pos[3]>=500:
                            canvas.delete(self.id)

                    self.variable+=1         

            def main_command2(self, evt):
                pos2=self.canvas.coords(self.id2)

                if self.variable==0:

                    if L1[0]=='red':
                        root.destroy()
                        root1=Tk()
                        root1.geometry('500x500+700+300')
                        canvas1=Canvas(root1, width=500, height=500)
                        canvas1.pack()
                        canvas1.create_text(245,100,text='Game Over', font=('Times', 30))
                        canvas1.create_text(245,150,text='Your Score is:', font=('Times', 30))                        
                        Score=canvas1.create_text(400,150,text=L3[0], font=('Times', 30))

                        def restart():
                            root1.destroy()
                            os.startfile(r'C:\Users\elcan\Desktop/custom game.py')

                        btn=Button(root1, text='Menu',font=('Times', 15), bg='#ffcc00', fg='#000000', width=30, height=3, state='normal', command=restart)
                        btn.place(x=80, y=240)
                        root1.mainloop()

                    elif L3[0]==240:
                        root.destroy()
                        root1=Tk()
                        root1.geometry('500x500+700+300')
                        canvas1=Canvas(root1, width=500, height=500)
                        canvas1.pack()
                        canvas1.create_text(245,100,text='Success', font=('Times', 30))
                        canvas1.create_text(245,150,text='Your Score is:', font=('Times', 30))                        
                        Score=canvas1.create_text(400,150,text=L3[0]+10, font=('Times', 30))

                        def restart():
                            root1.destroy()
                            os.startfile(r'C:\Users\elcan\Desktop/custom game.py')

                        btn=Button(root1, text='Menu',font=('Times', 15), bg='#ffcc00', fg='#000000', width=30, height=3, state='normal', command=restart)
                        btn.place(x=80, y=240)
                        root1.mainloop()

                    elif L1[0]!='red':
                        
                        canvas.delete(self.id2)
                        self.id2=canvas.create_rectangle(pos2, fill='white')
                        
                        L2[0]+=10
                        L3[0]+=10
                        if pos2[3]>=500:
                            canvas.delete(self.id2)
                    self.variable+=1
                    
        notes=Notes(canvas, variable)
        z=2  
        variable=1
        
        while 1:
            notes.draw()
            notes.eternal_loop()
            t=time.perf_counter()

            if variable==1:
                z=t+1
                variable+=1

            if t>=z-0.5 and t<=z:
                canvas.tag_raise(margin6)
                canvas.tag_raise(margin7)
                               
            if t>=z and t<=z+0.5:
                canvas.tag_lower(margin6)
                canvas.tag_lower(margin7)                
                z+=1

            root.update()
            root.update_idletasks()
            time.sleep(0.01)
            
            
        root.mainloop()
    def Hard():
        gamemode.destroy()
        root=Tk()
        root.title('Custom Game')
        root.geometry('500x600+700+300')
        root.wm_attributes('-topmost', 1)
        canvas=Canvas(root,width=500, height=600, bg='#000000')
        canvas.pack()
        
        canvas.create_text(245, 540, text='Score:', font=('Times', 30), fill='red') 
        canvas.create_rectangle(0,501,500,600,outline='white')
        margin6=canvas.create_rectangle(0,0,100,500, fill='yellow')
        margin7=canvas.create_rectangle(400,0,500,500, fill='yellow')

        L2=[0]
        L3=[0]
        margin1=canvas.create_rectangle(0,0,100,500, fill='blue')
        margin2=canvas.create_rectangle(400,0,500,500, fill='blue')

        

        variable=0


        canvas.tag_lower(margin6)
        canvas.tag_lower(margin7)
        

        COLOURS_LIST=['red', 'lightgreen']
        L=[]
        L1=[]

        class Notes:

            def __init__(self, canvas, variable):
                self.canvas=canvas
                self.variable=variable                
                random_colour=random.choice(COLOURS_LIST)
                L.append(random_colour)
                self.id=canvas.create_rectangle(100, 0, 250, 250, fill=random_colour)

                if random_colour=='red':
                    random_colour='lightgreen'

                elif random_colour=='lightgreen':
                    random_colour='red'

                L1.append(random_colour)
                self.id2=canvas.create_rectangle(250, 0, 400, 250, fill=random_colour)
                self.canvas.bind_all('<KeyPress-Left>', self.main_command)
                self.canvas.bind_all('<KeyPress-Right>', self.main_command2)
                self.id3=canvas.create_text(320, 540, text=L3[0], font=('Times', 30), fill='red')

            def draw(self):
                self.canvas.move(self.id, 0, 5)
                self.canvas.move(self.id2, 0, 5)

            def eternal_loop(self):
                pos=self.canvas.coords(self.id)
                self.canvas=canvas
                random_colour=random.choice(COLOURS_LIST)
                    
                if pos[3]>=500:
                    if self.variable==0:
                        L3[0]-=10
                        if L3[0]==-100:
                            root.destroy()
                            root1=Tk()
                            root1.geometry('500x500+700+300')
                            canvas1=Canvas(root1, width=500, height=500)
                            canvas1.pack()
                            canvas1.create_text(245,100,text='Game Over', font=('Times', 30))
                            canvas1.create_text(245,150,text='Your Score is:', font=('Times', 30))
                            Score=canvas1.create_text(400,150,text=L3[0], font=('Times', 30))

                            def restart():
                                root1.destroy()
                                os.startfile(r'C:\Users\elcan\Desktop/custom game.py')

                            btn=Button(root1, text='restart',font=('Times', 15), bg='#ffcc00', fg='#000000', width=30, height=3, state='normal', command=restart)
                            btn.place(x=80, y=240)
                            root1.mainloop()
                    self.variable=0
                    L[0]=random_colour
                    canvas.delete(self.id)
                    canvas.delete(self.id2)
                    canvas.delete(self.id3)
                    self.id=canvas.create_rectangle(100, 0, 250, 250, fill=random_colour)

                    if random_colour=='red':
                        random_colour='lightgreen'

                    elif random_colour=='lightgreen':
                        random_colour='red'

                    L1[0]=random_colour
                    self.id2=canvas.create_rectangle(250, 0, 400, 250, fill=random_colour)
                    self.id3=canvas.create_text(320, 540, text=L3[0], font=('Times', 30), fill='red')

            def main_command(self, evt):
                pos=self.canvas.coords(self.id)

                if self.variable==0:

                    if L[0]=='red':
                        root.destroy()
                        root1=Tk()
                        root1.geometry('500x500+700+300')
                        canvas1=Canvas(root1, width=500, height=500)
                        canvas1.pack()
                        canvas1.create_text(245,100,text='Game Over', font=('Times', 30))
                        canvas1.create_text(245,150,text='Your Score is:', font=('Times', 30))
                        Score=canvas1.create_text(400,150,text=L3[0], font=('Times', 30))

                        def restart():
                            root1.destroy()
                            os.startfile(r'C:\Users\elcan\Desktop/custom game.py')

                        btn=Button(root1, text='restart',font=('Times', 15), bg='#ffcc00', fg='#000000', width=30, height=3, state='normal', command=restart)
                        btn.place(x=80, y=240)
                        root1.mainloop()

                    elif L3[0]==290:
                        root.destroy()
                        root1=Tk()
                        root1.geometry('500x500+700+300')
                        canvas1=Canvas(root1, width=500, height=500)
                        canvas1.pack()
                        canvas1.create_text(245,100,text='Success', font=('Times', 30))
                        canvas1.create_text(245,150,text='Your Score is:', font=('Times', 30))
                        Score=canvas1.create_text(400,150,text=L3[0]+10, font=('Times', 30))

                        def restart():
                            root1.destroy()
                            os.startfile(r'C:\Users\elcan\Desktop/custom game.py')

                        btn=Button(root1, text='Menu',font=('Times', 15), bg='#ffcc00', fg='#000000', width=30, height=3, state='normal', command=restart)
                        btn.place(x=80, y=240)
                        root1.mainloop()
                    

                    elif L[0]!='red':
                        
                        canvas.delete(self.id)
                        self.id=canvas.create_rectangle(pos, fill='white')
                        L2[0]+=10
                        L3[0]+=10

                        if pos[3]>=500:
                            canvas.delete(self.id)

                    self.variable+=1        

            def main_command2(self, evt):
                pos2=self.canvas.coords(self.id2)

                if self.variable==0:

                    if L1[0]=='red':
                        root.destroy()
                        root1=Tk()
                        root1.geometry('500x500+700+300')
                        canvas1=Canvas(root1, width=500, height=500)
                        canvas1.pack()
                        canvas1.create_text(245,100,text='Game Over', font=('Times', 30))
                        canvas1.create_text(245,150,text='Your Score is:', font=('Times', 30))
                        Score=canvas1.create_text(400,150,text=L3[0], font=('Times', 30))

                        def restart():
                            root1.destroy()
                            os.startfile(r'C:\Users\elcan\Desktop/custom game.py')

                        btn=Button(root1, text='Menu',font=('Times', 15), bg='#ffcc00', fg='#000000', width=30, height=3, state='normal', command=restart)
                        btn.place(x=80, y=240)
                        root1.mainloop()

                    elif L3[0]==290:
                        root.destroy()
                        root1=Tk()
                        root1.geometry('500x500+700+300')
                        canvas1=Canvas(root1, width=500, height=500)
                        canvas1.pack()
                        canvas1.create_text(245,100,text='Success', font=('Times', 30))
                        canvas1.create_text(245,150,text='Your Score is:', font=('Times', 30))
                        
                        Score=canvas1.create_text(400,150,text=L3[0]+10, font=('Times', 30))
                        def restart():
                            root1.destroy()
                            os.startfile(r'C:\Users\elcan\Desktop/custom game.py')
                        btn=Button(root1, text='Menu',font=('Times', 15), bg='#ffcc00', fg='#000000', width=30, height=3, state='normal', command=restart)
                        btn.place(x=80, y=240)
                        root1.mainloop()
                    
                    if L1[0]!='red':                        
                        canvas.delete(self.id2)
                        self.id2=canvas.create_rectangle(pos2, fill='white')
                        L2[0]+=10
                        L3[0]+=10

                        if pos2[3]>=500:
                            canvas.delete(self.id2)

                    self.variable+=1      
        notes=Notes(canvas, variable)
        variable=1
        
        while 1:
            notes.draw()
            notes.eternal_loop()
            t=time.perf_counter()

            if variable==1:
                z=t+1
                variable+=1
            if t>=z-0.5 and t<=z:
                canvas.tag_raise(margin6)
                canvas.tag_raise(margin7)
                
                
            if t>=z and t<=z+0.5:
                canvas.tag_lower(margin6)
                canvas.tag_lower(margin7)                
                z+=1

            root.update()
            root.update_idletasks()
            time.sleep(0.01)
        root.mainloop()
       
    btn10=Button(gamemode, text='Easy', font=('Times', 15), bg='#ffcc00', fg='#000000', width=30, height=3, state='normal', command=Easy)
    btn10.place(x=80, y=100)
    btn20=Button(gamemode, text='Medium', font=('Times', 15), bg='#ffcc00', fg='#000000', width=30, height=3, state='normal', command=Medium)
    btn20.place(x=80, y=240)
    btn30=Button(gamemode, text='Hard', font=('Times', 15), bg='#ffcc00', fg='#000000', width=30, height=3, state='normal', command=Hard)
    btn30.place(x=80, y=380)

def onclick1():
    menu.destroy()
    tutorial=Tk()
    tutorial.title('Tutorial')
    tutorial.geometry('500x500+700+300')
    canvas4=Canvas(tutorial, width=500, height=500, bg='#000000')
    canvas4.pack()
    canvas4.create_text(245, 40,text='Tutorial', font=('Times', 40), fill='blue')
    canvas4.create_text(245,140,text='←  button to hit the left rectangle', font=('Times', 25), fill='white')
    canvas4.create_text(245,240,text='→  button to hit the right rectangle', font=('Times', 25), fill='white')

    def onclick2():
        tutorial.destroy()
        os.startfile(r'C:\Users\elcan\Desktop/custom game.py')

    btn5=Button(tutorial, text='Back', font=('Times', 15), bg='#ffcc00', fg='#000000', width=30, height=3, state='normal', command=onclick2)
    btn5.place(x=70, y=270)
    tutorial.mainloop()

def onclick30():
    menu.destroy()

btn1=Button(menu, text='Play', font=('Times', 15), bg='#ffcc00', fg='#000000', width=30, height=3, state='normal', command=onclick)
btn1.place(x=80, y=100)
btn2=Button(menu, text='Tutorial', font=('Times', 15), bg='#ffcc00', fg='#000000', width=30, height=3, state='normal', command=onclick1)
btn2.place(x=80, y=240)
btn2=Button(menu, text='Quit', font=('Times', 15), bg='#ffcc00', fg='#000000', width=30, height=3, state='normal', command=onclick30)
btn2.place(x=80, y=380)
menu.update()
time.sleep(0.01)
menu.mainloop()
