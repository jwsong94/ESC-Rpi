import tkinter as tk

window = tk.Tk();
frame = tk.Frame(window);
frame.pack();

button1 = tk.Button(frame,
                    text="BLE1",);
button1.pack(side=tk.LEFT)
button2 = tk.Button(frame,
                    text="BLE2");
button2.pack(side=tk.LEFT)

window.mainloop();
