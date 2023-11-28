from tkinter import*

root = Tk()
root.title("Fibonnacci")
root.geometry("600x300")
comm = Label(root,text="enter no. times to execute the program")
enter_no = Entry(root,text="enter no.")
series = Label(root,text="Fibonaci series: ")
flower = Label(root)
spiral = Label(root)

def fibo():
    num1=0
    num2=1
    sum=0
    val=int(enter_no.get())
    counter=1
    while(counter<=val):
        series["text"] += str(sum)+""
        counter = counter+1
        num1=num2
        num2=sum
        sum = num1+num2
    flower["text"]="flower is fully bloomed "
    spiral["text"] = "spiral in right diresction are "+str(num1)+" spirals in left direction are "+str(num2)+" \n total spirals are "+str(sum)
    
btn = Button(root,text="click to see the fibonacci series",command=fibo)
comm.pack()
enter_no.pack()
btn.pack()
series.pack()
flower.pack()
spiral.pack()

root.mainloop()
