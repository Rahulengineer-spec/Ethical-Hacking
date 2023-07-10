import tkinter as tk

class CarGUI:
    def __init__(self, window):
        self.window = window
        self.canvas = tk.Canvas(self.window, width=400, height=300)
        self.canvas.pack()
        self.car_image = tk.PhotoImage(file="car.png")  # Replace "car.png" with your car image file path
        self.car = self.canvas.create_image(50, 150, image=self.car_image)
        
    def move_car(self):
        self.canvas.move(self.car, 5, 0)  # Adjust the values to change the car's movement speed and direction
        self.window.after(100, self.move_car)
        
    def start(self):
        self.move_car()
        self.window.mainloop()

window = tk.Tk()
car_gui = CarGUI(window)
car_gui.start()
