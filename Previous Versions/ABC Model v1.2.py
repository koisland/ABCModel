import copy
import os
import tkinter as tk
import webbrowser
from tkinter import messagebox
from PIL import Image, ImageTk


def disable(item):
    whorls = ['1. Sepals', '2. Petals', '3. Stamen', '4. Carpels']
    genes = [1, 2, 3]  # A, B, and C, respectively.

    def on_off(button, state, color, grid_row, boolean):
        if not color:
            button.config(relief=state)
        else:
            button.config(bg=color, relief=state)
        app.grid[grid_row][item] = boolean

    if item in ABCWindow.target_whorl:  # Remove whorl if the same as previously pressed whorl.
        ABCWindow.target_whorl.remove(item)
        print(ABCWindow.target_whorl, ABCWindow.target_gene)
        if item == '1. Sepals':
            on_off(app.whorl_1, 'raised', '', 1, 0)
        elif item == '2. Petals':
            on_off(app.whorl_2, 'raised', '', 1, 0)
        elif item == '3. Stamen':
            on_off(app.whorl_3, 'raised', '', 1, 0)
        elif item == '4. Carpels':
            on_off(app.whorl_4, 'raised', '', 1, 0)
        grid_draw()
        return

    if item in ABCWindow.target_gene:  # Remove gene if the same as previously pressed gene.
        ABCWindow.target_gene.remove(item)
        print(ABCWindow.target_whorl, ABCWindow.target_gene)
        if item == 1:  # A
            on_off(app.cls_a, 'raised', 'blue', 2, 0)
        elif item == 2:  # B
            on_off(app.cls_b, 'raised', 'yellow', 2, 0)
        elif item == 3:  # C
            on_off(app.cls_c, 'raised', 'red', 2, 0)
        grid_draw()
        return

    if item in whorls:
        ABCWindow.target_whorl.append(item)
        if item == '1. Sepals':
            on_off(app.whorl_1, 'sunken', '', 1, 1)
        elif item == '2. Petals':
            on_off(app.whorl_2, 'sunken', '', 1, 1)
        elif item == '3. Stamen':
            on_off(app.whorl_3, 'sunken', '', 1, 1)
        elif item == '4. Carpels':
            on_off(app.whorl_4, 'sunken', '', 1, 1)

    if item in genes:
        ABCWindow.target_gene.append(item)
        if item == 1:
            on_off(app.cls_a, 'sunken', '#8080ff', 2, 1)
        elif item == 2:
            on_off(app.cls_b, 'sunken', '#ffff80', 2, 1)
        elif item == 3:
            on_off(app.cls_c, 'sunken', '#ff8080', 2, 1)


def grid_draw():
    def column_filler(new_value, *args):
        for original_key in args:
            column[original_key] = new_value

    # Needs to be sorted after every button press. Otherwise more conditions to check below.
    ABCWindow.target_whorl = sorted(ABCWindow.target_whorl)
    ABCWindow.target_gene = sorted(ABCWindow.target_gene)

    for row, column in app.grid.items():
        if row == 3 or row == 4:
            # Nothing disabled.
            if (not ABCWindow.target_whorl and not ABCWindow.target_gene) or \
                    (ABCWindow.target_gene == [1] and ABCWindow.target_whorl == ['3. Stamen']) or \
                    (ABCWindow.target_gene == [1] and ABCWindow.target_whorl == ['4. Carpels']) or \
                    (ABCWindow.target_gene == [2] and ABCWindow.target_whorl == ['1. Sepals']) or \
                    (ABCWindow.target_gene == [2] and ABCWindow.target_whorl == ['4. Carpels']) or \
                    (ABCWindow.target_gene == [3] and ABCWindow.target_whorl == ['1. Sepals']) or \
                    (ABCWindow.target_gene == [3] and ABCWindow.target_whorl == ['2. Petals']) or \
                    (ABCWindow.target_gene == [1, 2] and ABCWindow.target_whorl == ['4. Carpels']) or \
                    (ABCWindow.target_gene == [2, 3] and ABCWindow.target_whorl == ['1. Sepals']):
                imager('wt.png', app.image_box, app)

            # Whorls disabled
            elif (not ABCWindow.target_gene and ABCWindow.target_whorl == ['1. Sepals']) or \
                    (ABCWindow.target_gene == [1, 3] and ABCWindow.target_whorl == ['1. Sepals']):
                column_filler('-', 1)
                imager('No W1, A+C in W1.png', app.image_box, app)
            elif not ABCWindow.target_gene and ABCWindow.target_whorl == ['2. Petals']:
                column_filler('-', 2)
                imager('No W2.png', app.image_box, app)
            elif (not ABCWindow.target_gene and ABCWindow.target_whorl == ['3. Stamen']) or \
                    (ABCWindow.target_gene == [2, 3] and ABCWindow.target_whorl == ['3. Stamen']):
                column_filler('-', 3)
                imager('No W3, B+C in W3.png', app.image_box, app)
            elif (not ABCWindow.target_gene and ABCWindow.target_whorl == ['4. Carpels']) or \
                    (ABCWindow.target_gene == [1, 3] and ABCWindow.target_whorl == ['4. Carpels']) or \
                    (ABCWindow.target_gene == [2, 3] and ABCWindow.target_whorl == ['4. Carpels']):
                column_filler('-', 4)
                imager('No W4, A+C in W4, B+C in W4.png', app.image_box, app)
            elif not ABCWindow.target_gene and ABCWindow.target_whorl == ['1. Sepals', '2. Petals']:
                column_filler('-', 1, 2)
                imager('No W1+2.png', app.image_box, app)
            elif not ABCWindow.target_gene and ABCWindow.target_whorl == ['1. Sepals', '3. Stamen']:
                column_filler('-', 1, 3)
                imager('No W1+3.png', app.image_box, app)
            elif not ABCWindow.target_gene and ABCWindow.target_whorl == ['1. Sepals', '4. Carpels']:
                column_filler('-', 1, 4)
                imager('No W1+4.png', app.image_box, app)
            elif not ABCWindow.target_gene and ABCWindow.target_whorl == ['2. Petals', '3. Stamen']:
                column_filler('-', 2, 3)
                imager('No W2+3.png', app.image_box, app)
            elif not ABCWindow.target_gene and ABCWindow.target_whorl == ['2. Petals', '4. Carpels']:
                column_filler('-', 2, 4)
                imager('No W2+4.png', app.image_box, app)
            elif not ABCWindow.target_gene and ABCWindow.target_whorl == ['3. Stamen', '4. Carpels']:
                column_filler('-', 3, 4)
                imager('No W3+4.png', app.image_box, app)
            elif not ABCWindow.target_gene and ABCWindow.target_whorl == ['1. Sepals', '2. Petals', '3. Stamen']:
                column_filler('-', 1, 2, 3)
                imager('No W1+2+3.png', app.image_box, app)
            elif not ABCWindow.target_gene and ABCWindow.target_whorl == ['1. Sepals', '2. Petals', '4. Carpels']:
                column_filler('-', 1, 2, 4)
                imager('No W1+2+4.png', app.image_box, app)
            elif not ABCWindow.target_gene and ABCWindow.target_whorl == ['1. Sepals', '3. Stamen', '4. Carpels']:
                column_filler('-', 1, 3, 4)
                imager('No W1+3+4.png', app.image_box, app)
            elif not ABCWindow.target_gene and ABCWindow.target_whorl == ['2. Petals', '3. Stamen', '4. Carpels']:
                column_filler('-', 2, 3, 4)
                imager('No W2+3+4.png', app.image_box, app)

            # Genes and whorls disabled
            elif (not ABCWindow.target_whorl and ABCWindow.target_gene == [2]) or \
                    (ABCWindow.target_whorl == ['2. Petals', '3. Stamen'] and ABCWindow.target_gene == [2]):
                if row == 3:
                    column_filler('-', 2, 3)
                    imager('No B, B in W2+3.png', app.image_box, app)
            elif (not ABCWindow.target_whorl and ABCWindow.target_gene == [1]) or \
                    (ABCWindow.target_whorl == ['1. Sepals', '2. Petals'] and ABCWindow.target_gene == [1]) or \
                    (ABCWindow.target_whorl == ['1. Sepals'] and ABCWindow.target_gene == [1, 2]):
                if row == 4:
                    column_filler('C', 1, 2)
                    imager('No A, A in W1+2, A+B in W1.png', app.image_box, app)
            elif (not ABCWindow.target_whorl and ABCWindow.target_gene == [3]) or \
                    (ABCWindow.target_whorl == ['3. Stamen', '4. Carpels'] and ABCWindow.target_gene == [1]):
                if row == 4:
                    column_filler('A', 3, 4)
                    imager('No C, C in W3+4.png', app.image_box, app)
            elif not ABCWindow.target_whorl and ABCWindow.target_gene == [1, 3]:
                if row == 4:
                    column_filler('-', 1, 2, 3, 4)
                    imager('No A+C.png', app.image_box, app)
            elif ABCWindow.target_whorl == ['2. Petals'] and ABCWindow.target_gene == [1, 3]:
                if row == 4:
                    column_filler('-', 2)
                    imager('No A+C in W2.png', app.image_box, app)
            elif ABCWindow.target_whorl == ['3. Stamen'] and ABCWindow.target_gene == [1, 3]:
                if row == 4:
                    column_filler('-', 3)
                    imager('No A+C in W3.png', app.image_box, app)
            elif (not ABCWindow.target_whorl and ABCWindow.target_gene == [1, 2]) or \
                    (ABCWindow.target_whorl == ['1. Sepals', '2. Petals', '3. Stamen'] and ABCWindow.target_gene == [1, 2]):
                if row == 3:
                    column_filler('-', 2, 3)
                elif row == 4:
                    column_filler('C', 1, 2)
                imager('No A+B, A+B in W1+2+3.png', app.image_box, app)
            elif (ABCWindow.target_whorl == ['2. Petals'] and ABCWindow.target_gene == [1, 2]) or \
                    (ABCWindow.target_whorl == ['2. Petals', '4. Carpels'] and ABCWindow.target_gene == [1, 2]):
                if row == 3:
                    column_filler('-', 2)
                elif row == 4:
                    column_filler('C', 2)
                imager('No A+B in W2, A+B in W2+4.png', app.image_box, app)

            # NEED PICTURES

            elif (ABCWindow.target_whorl == ['1. Sepals', '2. Petals'] and ABCWindow.target_gene == [1, 2]) or \
                    (ABCWindow.target_whorl == ['1. Sepals', '2. Petals', '4. Carpels'] and ABCWindow.target_gene == [1, 2]):
                if row == 3:
                    column_filler('-', 2)
                elif row == 4:
                    column_filler('C', 1, 2)
                imager('No A+B in W1+2, A+B in W1+2+4.png', app.image_box, app)
            elif ABCWindow.target_whorl == ['1. Sepals', '3. Stamen'] and ABCWindow.target_gene == [1, 2]:
                if row == 3:
                    column_filler('-', 3)
                elif row == 4:
                    column_filler('C', 1)
                    column_filler('A', 3)
                imager('No A+B in W1+3.png', app.image_box, app)
            elif (ABCWindow.target_whorl == ['2. Petals', '3. Stamen'] and ABCWindow.target_gene == [1, 2]) or \
                    (ABCWindow.target_whorl == ['2. Petals', '3. Stamen', '4. Carpels'] and ABCWindow.target_gene == [1, 2]):
                if row == 3:
                    column_filler('-', 2, 3)
                elif row == 4:
                    column_filler('C', 2)
                imager('No A+B in W2+3, A+B in W2+3+4.png', app.image_box, app)
            elif ABCWindow.target_whorl == ['1. Sepals', '3. Stamen', '4. Carpels'] and ABCWindow.target_gene == [1, 2]:
                if row == 3:
                    column_filler('-', 3)
                elif row == 4:
                    column_filler('C', 1)
                imager('No A+B in W1+3+4.png', app.image_box, app)
            elif not ABCWindow.target_whorl and ABCWindow.target_gene == [2, 3]:
                if row == 3:
                    column_filler('-', 2, 3)
                elif row == 4:
                    column_filler('A', 3, 4)
                imager('No B+C.png', app.image_box, app)
            elif ABCWindow.target_whorl == ['1. Sepals', '3. Stamen'] and ABCWindow.target_gene == [2, 3]:
                if row == 3:
                    column_filler('-', 3)
                elif row == 4:
                    column_filler('A', 3)
                imager('No B+C in W1+3.png', app.image_box, app)
            elif ABCWindow.target_whorl == ['2. Petals', '3. Stamen'] and ABCWindow.target_gene == [2, 3]:
                if row == 3:
                    column_filler('-', 2, 3)
                elif row == 4:
                    column_filler('A', 3)
                imager('No B+C in W2+3.png', app.image_box, app)
            elif ABCWindow.target_whorl == ['2. Petals', '4. Carpels'] and ABCWindow.target_gene == [2, 3]:
                if row == 3:
                    column_filler('-', 2)
                elif row == 4:
                    column_filler('A', 4)
                imager('No B+C in W2+4.png', app.image_box, app)
            elif ABCWindow.target_whorl == ['3. Stamen', '4. Carpels'] and ABCWindow.target_gene == [2, 3]:
                if row == 3:
                    column_filler('-', 3)
                elif row == 4:
                    column_filler('A', 3, 4)
                imager('No B+C in W3+4.png', app.image_box, app)

            # NOT DONE

            elif ABCWindow.target_whorl == ['1. Sepals', '2. Petals', '3. Stamen'] and ABCWindow.target_gene == [2, 3]:
                if row == 3:
                    column_filler('-', 2, 3)
                elif row == 4:
                    column_filler('C', 2)
                imager('No B+C in W1+2+3.png', app.image_box, app)

            elif ABCWindow.target_whorl == ['1. Sepals', '2. Petals', '4. Carpels'] and ABCWindow.target_gene == [2, 3]:
                if row == 3:
                    column_filler('-', 2, 3)
                elif row == 4:
                    column_filler('C', 2)
                imager('No B+C in W1+2+4.png', app.image_box, app)

            elif ABCWindow.target_whorl == ['1. Sepals', '3. Stamen', '4. Carpels'] and ABCWindow.target_gene == [2, 3]:
                if row == 3:
                    column_filler('-', 2, 3)
                elif row == 4:
                    column_filler('C', 2)
                imager('No B+C in W1+3+4.png', app.image_box, app)

            elif ABCWindow.target_whorl == ['2. Petals', '3. Stamen', '4. Carpels'] and ABCWindow.target_gene == [2, 3]:
                if row == 3:
                    column_filler('-', 2, 3)
                elif row == 4:
                    column_filler('C', 2)
                imager('No B+C in W2+3+4.png', app.image_box, app)

            elif ABCWindow.target_whorl == ['1. Sepals', '2. Petals'] and ABCWindow.target_gene == [1, 3]:
                if row == 3:
                    column_filler('-', 2, 3)
                elif row == 4:
                    column_filler('A', 3, 4)
                imager('No A+C in W1+2.png', app.image_box, app)

            elif ABCWindow.target_whorl == ['1. Sepals', '3. Stamen'] and ABCWindow.target_gene == [1, 3]:
                if row == 3:
                    column_filler('-', 2, 3)
                elif row == 4:
                    column_filler('A', 3, 4)
                imager('No A+C in W1+3.png', app.image_box, app)

            elif ABCWindow.target_whorl == ['1. Sepals', '4. Carpels'] and ABCWindow.target_gene == [1, 3]:
                if row == 3:
                    column_filler('-', 2, 3)
                elif row == 4:
                    column_filler('A', 3, 4)
                imager('No A+C in W1+4.png', app.image_box, app)

            elif ABCWindow.target_whorl == ['2. Petals', '3. Stamen'] and ABCWindow.target_gene == [1, 3]:
                if row == 3:
                    column_filler('-', 2, 3)
                elif row == 4:
                    column_filler('A', 3, 4)
                imager('No A+C in W2+3.png', app.image_box, app)

            elif ABCWindow.target_whorl == ['2. Petals', '4. Carpels'] and ABCWindow.target_gene == [1, 3]:
                if row == 3:
                    column_filler('-', 2, 3)
                elif row == 4:
                    column_filler('A', 3, 4)
                imager('No A+C in W2+4.png', app.image_box, app)

            elif ABCWindow.target_whorl == ['3. Stamen', '4. Carpels'] and ABCWindow.target_gene == [1, 3]:
                if row == 3:
                    column_filler('-', 2, 3)
                elif row == 4:
                    column_filler('A', 3, 4)
                imager('No A+C in W3+4.png', app.image_box, app)

            elif ABCWindow.target_whorl == ['1. Sepals', '2. Petals', '3. Stamen'] and ABCWindow.target_gene == [1, 3]:
                if row == 3:
                    column_filler('-', 2, 3)
                elif row == 4:
                    column_filler('C', 2)
                imager('No A+C in W1+2+3.png', app.image_box, app)

            elif ABCWindow.target_whorl == ['1. Sepals', '2. Petals', '4. Carpels'] and ABCWindow.target_gene == [1, 3]:
                if row == 3:
                    column_filler('-', 2, 3)
                elif row == 4:
                    column_filler('C', 2)
                imager('No A+C in W1+2+4.png', app.image_box, app)

            elif ABCWindow.target_whorl == ['1. Sepals', '3. Stamen', '4. Carpels'] and ABCWindow.target_gene == [1, 3]:
                if row == 3:
                    column_filler('-', 2, 3)
                elif row == 4:
                    column_filler('C', 2)
                imager('No A+C in W1+3+4.png', app.image_box, app)

            elif ABCWindow.target_whorl == ['2. Petals', '3. Stamen', '4. Carpels'] and ABCWindow.target_gene == [1, 3]:
                if row == 3:
                    column_filler('-', 2, 3)
                elif row == 4:
                    column_filler('C', 2)
                imager('No A+C in W2+3+4.png', app.image_box, app)

            # DONE

            elif (ABCWindow.target_gene == [1, 2, 3]) or \
                    (ABCWindow.target_whorl == ['1. Sepals', '2. Petals', '3. Stamen', '4. Carpels']):
                column_filler('-', 1, 2, 3, 4)
                imager('No A+B+C.png', app.image_box, app)
            elif (ABCWindow.target_gene == [1] and ABCWindow.target_whorl == ['1. Sepals']) or \
                    (ABCWindow.target_whorl == ['1. Sepals', '4. Carpels'] and ABCWindow.target_gene == [1, 2]):
                if row == 4:
                    column_filler('C', 1)
                imager('No A in W1, A+B in W1+4.png', app.image_box, app)
            elif (ABCWindow.target_gene == [1] and ABCWindow.target_whorl == ['2. Petals']) or \
                    (ABCWindow.target_gene == [1] and ABCWindow.target_whorl == ['2. Petals', '3. Stamen']):
                if row == 4:
                    column_filler('C', 2)
                imager('No A in W2, A in W2+3.png', app.image_box, app)
            elif (ABCWindow.target_gene == [2] and ABCWindow.target_whorl == ['2. Petals']) or \
                    (ABCWindow.target_gene == [2, 3] and ABCWindow.target_whorl == ['2. Petals']) or \
                    (ABCWindow.target_whorl == ['1. Sepals', '2. Petals'] and ABCWindow.target_gene == [2, 3]):
                if row == 3:
                    column_filler('-', 2)
                imager('No B in W2, B+C in W2, B+C in W1+2.png', app.image_box, app)
            elif ABCWindow.target_gene == [2] and ABCWindow.target_whorl == ['3. Stamen'] or \
                    (ABCWindow.target_gene == [1, 2] and ABCWindow.target_whorl == ['3. Stamen']) or \
                    (ABCWindow.target_gene == [1, 2] and ABCWindow.target_whorl == ['3. Stamen', '4. Carpels']):
                if row == 3:
                    column_filler('-', 3)
                imager('No B in W3, A+B in W3, A+B in W3+4.png', app.image_box, app)
            elif ABCWindow.target_gene == [3] and ABCWindow.target_whorl == ['3. Stamen']:
                if row == 4:
                    column_filler('A', 3)
                imager('No C in W3.png', app.image_box, app)
            elif (ABCWindow.target_gene == [3] and ABCWindow.target_whorl == ['4. Carpels']) or \
                    (ABCWindow.target_whorl == ['1. Sepals', '4. Carpels'] and ABCWindow.target_gene == [2, 3]):
                if row == 4:
                    column_filler('A', 4)
                imager('No C in W4, B+C in W1+4.png', app.image_box, app)

    print('', '\n', app.grid[3], '\n', app.grid[4])
    print(ABCWindow.target_gene, ABCWindow.target_whorl)


def imager(file, init_widget, master_widget):  # Insert image.
    try:
        img_path = os.path.expanduser('~\\Desktop\\ABC Model\\Images\\') + file
        file = Image.open(img_path)
        file = file.resize((300, 290), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(file, master=master_widget)
        init_widget.configure(image=render)
        init_widget.image = render
    except FileNotFoundError:
        init_widget.config(image='', text="'" + file + "' was not found")


class ABCWindow(tk.Tk):
    # Button Response
    target_whorl = []
    target_gene = []

    def __init__(self):
        super().__init__()
        self.original_grid = {1: {'1. Sepals': 0, '2. Petals': 0, '3. Stamen': 0, '4. Carpels': 0},
                              2: {1: 0, 2: 0, 3: 0},  # A, B, C
                              3: {1: '-', 2: 'B', 3: 'B', 4: '-'},
                              4: {1: 'A', 2: 'A', 3: 'C', 4: 'C'}}
        self.grid = copy.deepcopy(self.original_grid)

        self.whorl_frame = tk.Frame()
        self.whorl_frame.grid(row=1, pady=(10, 0))
        self.whorl_1 = tk.Button(self.whorl_frame, text='Sepals', font='Roboto 11', bg='#7fa905', width=12,
                                 command=lambda: [disable('1. Sepals'), grid_draw(), self.updating_abc()])
        self.whorl_2 = tk.Button(self.whorl_frame, text='Petals', font='Roboto 11', bg='#f9dc00', width=12,
                                 command=lambda: [disable('2. Petals'), grid_draw(), self.updating_abc()])
        self.whorl_3 = tk.Button(self.whorl_frame, text='Stamen', font='Roboto 11', bg='#66c3e7', width=12,
                                 command=lambda: [disable('3. Stamen'), grid_draw(), self.updating_abc()])
        self.whorl_4 = tk.Button(self.whorl_frame, text='Carpels', font='Roboto 11', bg='#f2a064', width=12,
                                 command=lambda: [disable('4. Carpels'), grid_draw(), self.updating_abc()])

        self.whorl_1.grid(row=1, column=1)
        self.whorl_2.grid(row=1, column=2)
        self.whorl_3.grid(row=1, column=3)
        self.whorl_4.grid(row=1, column=4)

        # Class gene frame
        self.gene_frame = tk.Frame()
        self.gene_frame.grid(row=2, padx=10, pady=10)
        self.cls_a = tk.Button(self.gene_frame, text='Class A', font='Roboto 11', bg='blue', width=26,
                               command=lambda: [disable(1), grid_draw(), self.updating_abc()])
        self.cls_b = tk.Button(self.gene_frame, text='Class B', font='Roboto 11', bg='yellow', width=26,
                               command=lambda: [disable(2), grid_draw(), self.updating_abc()])
        self.cls_c = tk.Button(self.gene_frame, text='Class C', font='Roboto 11', bg='red', width=26,
                               command=lambda: [disable(3), grid_draw(), self.updating_abc()])

        self.cls_a.grid(row=2, column=1, columnspan=2)
        self.cls_b.grid(row=1, column=2, columnspan=2)
        self.cls_c.grid(row=2, column=3, columnspan=2)

        # Results Label
        self.update_frame = tk.Frame()
        self.update_frame.grid(row=3, pady=(0, 10))
        tk.Label(self, text=' - Results - ', font='Roboto 13 bold').grid(row=3)

        # WT Picture Frame
        self.old_img = 0
        self.pic_frame = tk.Frame()
        self.pic_frame.grid(row=4)
        self.image_box = tk.Label(self.pic_frame, relief='ridge', image='')
        imager('wt.png', self.image_box, self)
        self.image_box.grid(pady=(0, 10))

        # Class ABC Gene Labels & Grid Dictionary (To access later)
        self.product_frame = tk.Frame()
        self.product_frame.grid(row=5, pady=(0, 10))

        g3_1 = tk.Label(self.product_frame, font='Roboto, 9', width=13, bg='#FFFFFF', relief='ridge')
        g3_2 = tk.Label(self.product_frame, text='B', font='Roboto, 9', bg='yellow', width=13, relief='ridge')
        g3_3 = tk.Label(self.product_frame, text='B', font='Roboto, 9', bg='yellow', width=13, relief='ridge')
        g3_4 = tk.Label(self.product_frame, font='Roboto, 9', width=13, bg='#FFFFFF', relief='ridge')

        g4_1 = tk.Label(self.product_frame, text='A', font='Roboto, 9', bg='blue', width=13, relief='ridge')
        g4_2 = tk.Label(self.product_frame, text='A', font='Roboto, 9', bg='blue', width=13, relief='ridge')
        g4_3 = tk.Label(self.product_frame, text='C', font='Roboto, 9', bg='red', width=13, relief='ridge')
        g4_4 = tk.Label(self.product_frame, text='C', font='Roboto, 9', bg='red', width=13, relief='ridge')

        self.grid_dict = {'g3_1': g3_1, 'g3_2': g3_2, 'g3_3': g3_3, 'g3_4': g3_4,
                          'g4_1': g4_1, 'g4_2': g4_2, 'g4_3': g4_3, 'g4_4': g4_4}

        g3_1.grid(row=1, column=1)
        g3_2.grid(row=1, column=2)
        g3_3.grid(row=1, column=3)
        g3_4.grid(row=1, column=4)

        g4_1.grid(row=2, column=1)
        g4_2.grid(row=2, column=2)
        g4_3.grid(row=2, column=3)
        g4_4.grid(row=2, column=4)

        # References
        self.references = tk.Frame()
        self.references.grid(row=6)
        title = tk.Label(self.references, text=" - References - ", font='Roboto 13 bold')
        ppr = tk.Button(self.references,
                        text="Robles, Pedro & Pelaz, Soraya. (2005). Flower and fruit development in Arabidopsis thaliana.\n"
                             "The International journal of developmental biology. 49. 633-43. 10.1387/ijdb.052020pr.",
                        font='Roboto 9', relief='ridge', width=75,
                        command=lambda: webbrowser.open("https://www.researchgate.net/publication/7663453_"
                                                        "Flower_and_fruit_development_in_Arabidopsis_thaliana"))
        book = tk.Label(self.references,
                        text="Taiz L, Zeiger E. 2010. Plant Physiology and Development. 5th ed. \n"
                             "Sinauer Associates. Chapter 24, The Control of Flowering; pg. 561-565",
                        font='Roboto 9', relief='ridge', width=75)
        title.grid(padx=10)
        ppr.grid(padx=10)
        book.grid(pady=(0, 10))

        # tk.messagebox.showinfo(title="ABC Model (WIP!!!)",
        #                        message="This is a work-in-progress and is missing combinations!"
        #                                "\n\nIf you run into any errors or find something "
        #                                "that is incorrect, please let me know! "
        #                                "\n\n-Keith")

    def updating_abc(self):
        for row in range(3, 5):
            for key, value in self.grid[row].items():
                if value == 'A':
                    self.grid_dict['g' + str(row) + '_' + str(key)].config(text='A', bg='blue')
                elif value == 'B':
                    self.grid_dict['g' + str(row) + '_' + str(key)].config(text='B', bg='yellow')
                elif value == 'C':
                    self.grid_dict['g' + str(row) + '_' + str(key)].config(text='C', bg='red')
                elif value == '-':
                    self.grid_dict['g' + str(row) + '_' + str(key)].config(text='-', bg='#FFFFFF')

        self.grid = copy.deepcopy(self.original_grid)


# No need for if __name__ == '__main__':
# Not planning on importing.
app = ABCWindow()
app.title('ABC Model')
app.resizable(0, 0)
app.mainloop()

# Built in PyCharm using Python 3.8
# Keisuke K. Oshima (5/30/20)
