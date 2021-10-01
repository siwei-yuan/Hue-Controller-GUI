from phue import Bridge
import tkinter as tk


def connect():
    bridge = Bridge('192.168.31.132')
    bridge.connect()
    lights = bridge.lights
    for light in lights:
        print(light.name)


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.bridge = Bridge('192.168.31.132')
        self.master = master
        self.pack()
        self.create_widgets()

    def switch(self, name):
        status = self.bridge.get_light(name)
        self.bridge.set_light(name, 'on', not status.get('state').get('on'))

    def slide(self, data, name):
        self.bridge.set_light(name, {'bri': int(data), 'transitiontime': 1})

    def create_widgets(self):
        lights = Bridge('192.168.31.132').lights
        for light in lights:
            self.button = tk.Button(self, text=light.name, command=lambda: self.switch(light.name))
            self.button.grid(row=0, column=1, padx=10, pady=10)
            self.scale = tk.Scale(self, from_=0, to=254, command=lambda data: self.slide(data, light.name), length=200,
                                  orient="horizontal")
            self.scale.grid(row=1, column=1, padx=5)

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.grid(row=2, column=1, padx=10, pady=20)


root = tk.Tk()
app = Application(master=root)
app.mainloop()
