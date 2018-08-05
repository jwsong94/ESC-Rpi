import tkinter as tk

window = tk.Tk();

sensors = ['Oscil', 'Flame', 'Smoke'];

oscil = tk.Label(window, text='Oscil', width=10);
flame = tk.Label(window, text='Frame', width=10);
smoke = tk.Label(window, text='Smoke', width=10);

oscil_status = tk.Label(window, text='', width=2, bg='green');
flame_status = tk.Label(window, text='', width=2, bg='green');
smoke_status = tk.Label(window, text='', width=2, bg='green');

oscil.grid(row=0, column=0);
oscil_status.grid(row=0, column=1);
flame.grid(row=0, column=2);
flame_status.grid(row=0, column=3);
smoke.grid(row=0, column=4);
smoke_status.grid(row=0, column=5);

window.mainloop();
