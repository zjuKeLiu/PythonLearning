import tkinter
import tkinter.messagebox

def main():
    flag = True

    #change the words on label
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello, world!')\
            if flag else ('blue', 'Goodbye, world')
        label.conflg(text = msg, fg = color)

    #quit
    def confirm_to_quit():
        if tkinter.massageboc.askokcancel('notice', 'are you sure to quit?'):
            top.quit()

    #create the top window
    top = tkinter.Tk()
    #set the size of window
    top.geometry('240*160')
    #set the title of window
    top.title('Game')
    #create the label and add it to the top window
    label = tkinter.Label(top, text = 'Hello, world!', font = 'Arial -32', fg = 'red')
    label.pack(expand=1)
    #create a container to contain the button
    panel = tkinter.Frame(top)
    #create a button , attach it to the container, use the parameter of command to attach it to the function
    button1 = tkinter.Button(panel, text='change', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.button(panel, text='quit', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    #start the main loop of issue
    tkinter.mainloop()

if __name__ == '__main__':
    main()
