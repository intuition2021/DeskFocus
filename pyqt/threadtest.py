from tkinter import *

class TimerTest():
    def __init__(self, root):
        self.root=root

        self.is_running=False
        self.count=IntVar()
        self.max_seconds=60  ## quit after this amount of time
        Label(root, textvariable=self.count,
              font=('DejaVuSansMono', 12, "bold"),
              bg="lightyellow").grid(row=1, column=0,
              columnspan=2, sticky="ew")

        Button(root, text="Start", fg="blue", width=15,
                            command=self.startit).grid(row=10,
                            column=0, sticky="nsew")
        Button(root, text="Stop", fg="red", width=15,
                            command=self.stopit).grid(row=10,
                            column=1, sticky="nsew")
        Button(self.root, text="Quit", bg="orange",
                            command=self.root.quit).grid(row=11,
                            column=0, columnspan=2, sticky="nsew")

    def startit(self):
        if not self.is_running:  ## avoid 2 button pushes
            self.is_running=True
            self.increment_counter()

    def increment_counter(self):
        if self.is_running:  ## stopit not called
             c=self.count.get() +1
             self.count.set(c)
             if c < self.max_seconds:
                 self.root.after(1000, self.increment_counter)  ## every second
             else:
                 self.is_running=False
                 Label(root, text="Time Is Up",
                       font=('DejaVuSansMono', 14, "bold"),
                       bg="red").grid(row=5, column=0,
                       columnspan=2, sticky="ew")

    def stopit(self):
        self.is_running = False

root = Tk()
TT=TimerTest(root)
root.mainloop()