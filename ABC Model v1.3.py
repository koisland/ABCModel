import copy
import os
import tkinter as tk
import webbrowser
from PIL import Image, ImageTk


def disable(item):
    app.wt_image.destroy()
    app.whorls = ['1. Sepals', '2. Petals', '3. Stamen', '4. Carpels']
    app.genes = [1, 2, 3]  # A, B, and C, respectively.

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
            on_off(app.whorl_1, 'raised', '#7fa905', 1, 0)
        elif item == '2. Petals':
            on_off(app.whorl_2, 'raised', '#f9dc00', 1, 0)
        elif item == '3. Stamen':
            on_off(app.whorl_3, 'raised', '#66c3e7', 1, 0)
        elif item == '4. Carpels':
            on_off(app.whorl_4, 'raised', '#f2a064', 1, 0)
        grid_draw()
        return

    if item in ABCWindow.target_gene:  # Remove gene if the same as previously pressed gene.
        ABCWindow.target_gene.remove(item)
        print(ABCWindow.target_whorl, ABCWindow.target_gene)
        if item == 1:  # A
            on_off(app.cls_a, 'raised', '#8080ff', 2, 0)
        elif item == 2:  # B
            on_off(app.cls_b, 'raised', '#ffff80', 2, 0)
        elif item == 3:  # C
            on_off(app.cls_c, 'raised', '#ff8080', 2, 0)
        grid_draw()
        return

    if item in app.whorls:
        ABCWindow.target_whorl.append(item)
        if item == '1. Sepals':
            on_off(app.whorl_1, 'sunken', '#FFFFFF', 1, 1)
        elif item == '2. Petals':
            on_off(app.whorl_2, 'sunken', '#FFFFFF', 1, 1)
        elif item == '3. Stamen':
            on_off(app.whorl_3, 'sunken', '#FFFFFF', 1, 1)
        elif item == '4. Carpels':
            on_off(app.whorl_4, 'sunken', '#FFFFFF', 1, 1)

    if item in app.genes:
        ABCWindow.target_gene.append(item)
        if item == 1:
            on_off(app.cls_a, 'sunken', '#FFFFFF', 2, 1)
        elif item == 2:
            on_off(app.cls_b, 'sunken', '#FFFFFF', 2, 1)
        elif item == 3:
            on_off(app.cls_c, 'sunken', '#FFFFFF', 2, 1)


def grid_draw():
    # Takes inputs (genes disabled and in what whorl/all gene expression in a whorl.) and outputs gene expression.
    # Order of each condition is important. Once elif statement fulfilled, that iteration of the loop stops.
    # Conditions with greater requirements added first followed by more easily fulfilled ones.
    def column_filler(new_value, *args):
        for original_key in args:
            column[original_key] = new_value

    # In W1 -> Row 3: (-) and Row 4: (A, C or -)
    # In W2 -> Row 3: (B or -) and Row 4: (A, C or -)
    # In W3 -> Row 3: (B or -) and Row 4: (A, C or -)
    # In W1 -> Row 3: (-) and Row 4: (A, C or -)

    for row, column in app.grid.items():
        if row == 3:
            for x in column:
                # Same Level
                if x == 2 or x == 3:
                    if (app.whorls[x - 1] in ABCWindow.target_whorl) and not ABCWindow.target_gene:  # Only whorls
                        column_filler('-', x)
                    elif not ABCWindow.target_whorl and (2 in ABCWindow.target_gene):  # Only B gene
                        column_filler('-', x)
                    elif (app.whorls[x - 1] in ABCWindow.target_whorl) and (
                            2 in ABCWindow.target_gene):  # Specific whorl and B gene
                        column_filler('-', x)
                    elif 2 in ABCWindow.target_gene:
                        pass
        elif row == 4:
            for x in column:
                if app.whorls[x - 1] in ABCWindow.target_whorl and not ABCWindow.target_gene:
                    column_filler('-', x)
                elif not ABCWindow.target_whorl and (
                        1 in ABCWindow.target_gene and 3 in ABCWindow.target_gene):  # Only A or C
                    column_filler('-', x)
                elif not ABCWindow.target_whorl and (1 in ABCWindow.target_gene):  # Only A
                    column_filler('C', x)
                elif not ABCWindow.target_whorl and (3 in ABCWindow.target_gene):  # Only C
                    column_filler('A', x)
                elif app.whorls[x - 1] in ABCWindow.target_whorl and (
                        1 in ABCWindow.target_gene and 3 in ABCWindow.target_gene):  # Specific whorl and A and C
                    column_filler('-', x)
                elif app.whorls[x - 1] in ABCWindow.target_whorl and (
                        1 in ABCWindow.target_gene):  # Specific whorl and A
                    if x == 1 or x == 2:
                        column_filler('C', x)
                elif app.whorls[x - 1] in ABCWindow.target_whorl and (
                        3 in ABCWindow.target_gene):  # Specific whorl and C
                    if x == 3 or x == 4:
                        column_filler('A', x)

            # This ^^^ algorithm does the same thing as 300 lines of code...
            # So much wasted time :(((

    print('', '\n', app.grid[3], '\n', app.grid[4])
    print(ABCWindow.target_gene, ABCWindow.target_whorl)


def imager(file, init_widget, master_widget):  # Insert image.
    try:
        img_path = os.getcwd() + '\\Images\\' + file
        # img_path = '/home/runner/ABC-Model-v13/' + file
        file = Image.open(img_path)
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
        self.cls_a = tk.Button(self.gene_frame, text='Class A', font='Roboto 11', bg='#8080ff', width=26,
                               command=lambda: [disable(1), grid_draw(), self.updating_abc()])
        self.cls_b = tk.Button(self.gene_frame, text='Class B', font='Roboto 11', bg='#ffff80', width=26,
                               command=lambda: [disable(2), grid_draw(), self.updating_abc()])
        self.cls_c = tk.Button(self.gene_frame, text='Class C', font='Roboto 11', bg='#ff8080', width=26,
                               command=lambda: [disable(3), grid_draw(), self.updating_abc()])

        self.cls_a.grid(row=2, column=1, columnspan=2)
        self.cls_b.grid(row=1, column=2, columnspan=2)
        self.cls_c.grid(row=2, column=3, columnspan=2)

        # Results Label
        self.update_frame = tk.Frame()
        self.update_frame.grid(row=3, pady=(0, 10))
        tk.Label(self, text=' - Results - ', font='Roboto 13 bold').grid(row=3)

        # WT Picture Frame & Grid.
        self.pic_frame = tk.Frame()
        self.pic_frame.grid(row=4, pady=(0, 8))

        self.r1_1, self.r1_2, self.r1_3, self.r1_4, self.r1_5 = \
            tk.Label(self.pic_frame, relief='ridge', image=''), tk.Label(self.pic_frame, relief='ridge', image=''), \
            tk.Label(self.pic_frame, relief='ridge', image=''), tk.Label(self.pic_frame, relief='ridge', image=''), \
            tk.Label(self.pic_frame, relief='ridge', image='')
        self.r1_1.grid(row=1, column=1), self.r1_2.grid(row=1, column=2), self.r1_3.grid(row=1, column=3), \
        self.r1_4.grid(row=1, column=4), self.r1_5.grid(row=1, column=5)

        self.r2_1, self.r2_2, self.r2_3, self.r2_4, self.r2_5 = \
            tk.Label(self.pic_frame, relief='ridge', image=''), tk.Label(self.pic_frame, relief='ridge', image=''), \
            tk.Label(self.pic_frame, relief='ridge', image=''), tk.Label(self.pic_frame, relief='ridge', image=''), \
            tk.Label(self.pic_frame, relief='ridge', image='')
        self.r2_1.grid(row=2, column=1), self.r2_2.grid(row=2, column=2), self.r2_3.grid(row=2, column=3), \
        self.r2_4.grid(row=2, column=4), self.r2_5.grid(row=2, column=5)

        self.r3_1, self.r3_2, self.r3_3, self.r3_4, self.r3_5 = \
            tk.Label(self.pic_frame, relief='ridge', image=''), tk.Label(self.pic_frame, relief='ridge', image=''), \
            tk.Label(self.pic_frame, relief='ridge', image=''), tk.Label(self.pic_frame, relief='ridge', image=''), \
            tk.Label(self.pic_frame, relief='ridge', image='')
        self.r3_1.grid(row=3, column=1), self.r3_2.grid(row=3, column=2), self.r3_3.grid(row=3, column=3), \
        self.r3_4.grid(row=3, column=4), self.r3_5.grid(row=3, column=5)

        self.r4_1, self.r4_2, self.r4_3, self.r4_4, self.r4_5 = \
            tk.Label(self.pic_frame, relief='ridge', image=''), tk.Label(self.pic_frame, relief='ridge', image=''), \
            tk.Label(self.pic_frame, relief='ridge', image=''), tk.Label(self.pic_frame, relief='ridge', image=''), \
            tk.Label(self.pic_frame, relief='ridge', image='')
        self.r4_1.grid(row=4, column=1), self.r4_2.grid(row=4, column=2), self.r4_3.grid(row=4, column=3), \
        self.r4_4.grid(row=4, column=4), self.r4_5.grid(row=4, column=5)

        self.r5_1, self.r5_2, self.r5_3, self.r5_4, self.r5_5 = \
            tk.Label(self.pic_frame, relief='ridge', image=''), tk.Label(self.pic_frame, relief='ridge', image=''), \
            tk.Label(self.pic_frame, relief='ridge', image=''), tk.Label(self.pic_frame, relief='ridge', image=''), \
            tk.Label(self.pic_frame, relief='ridge', image='')
        self.r5_1.grid(row=5, column=1), self.r5_2.grid(row=5, column=2), self.r5_3.grid(row=5, column=3), \
        self.r5_4.grid(row=5, column=4), self.r5_5.grid(row=5, column=5)

        self.grid_pic = {'r1_1': self.r1_1, 'r1_2': self.r1_2, 'r1_3': self.r1_3, 'r1_4': self.r1_4, 'r1_5': self.r1_5,
                         'r2_1': self.r2_1, 'r2_2': self.r2_2, 'r2_3': self.r2_3, 'r2_4': self.r2_4, 'r2_5': self.r2_5,
                         'r3_1': self.r3_1, 'r3_2': self.r3_2, 'r3_3': self.r3_3, 'r3_4': self.r3_4, 'r3_5': self.r3_5,
                         'r4_1': self.r4_1, 'r4_2': self.r4_2, 'r4_3': self.r4_3, 'r4_4': self.r4_4, 'r4_5': self.r4_5,
                         'r5_1': self.r5_1, 'r5_2': self.r5_2, 'r5_3': self.r5_3, 'r5_4': self.r5_4, 'r5_5': self.r5_5}

        # Template Wild-Type Image
        open_file = Image.open(os.getcwd() + '\\Images\\wt.png')
        # open_file = Image.open('/home/runner/ABC-Model-v13/wt.png')
        open_file = open_file.resize((300, 290), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(open_file, master=self)
        self.wt_image = tk.Label(self.pic_frame, image=render)
        self.wt_image.image = render
        self.wt_image.grid(row=1, column=1, rowspan=5, columnspan=5)

        # Class ABC Gene Labels & Grid Dictionary (To access later)
        self.product_frame = tk.Frame()
        self.product_frame.grid(row=5, pady=(0, 10))

        g3_1 = tk.Label(self.product_frame, font='Roboto, 9', width=13, bg='#FFFFFF', relief='ridge')
        g3_2 = tk.Label(self.product_frame, text='B', font='Roboto, 9', bg='#ffff80', width=13, relief='ridge')
        g3_3 = tk.Label(self.product_frame, text='B', font='Roboto, 9', bg='#ffff80', width=13, relief='ridge')
        g3_4 = tk.Label(self.product_frame, font='Roboto, 9', width=13, bg='#FFFFFF', relief='ridge')

        g4_1 = tk.Label(self.product_frame, text='A', font='Roboto, 9', bg='#8080ff', width=13, relief='ridge')
        g4_2 = tk.Label(self.product_frame, text='A', font='Roboto, 9', bg='#8080ff', width=13, relief='ridge')
        g4_3 = tk.Label(self.product_frame, text='C', font='Roboto, 9', bg='#ff8080', width=13, relief='ridge')
        g4_4 = tk.Label(self.product_frame, text='C', font='Roboto, 9', bg='#ff8080', width=13, relief='ridge')

        self.grid_genes = {'g3_1': g3_1, 'g3_2': g3_2, 'g3_3': g3_3, 'g3_4': g3_4,
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

    def updating_abc(self):
        for row in range(3, 5):
            for key, value in self.grid[row].items():
                if value == 'A':
                    self.grid_genes['g' + str(row) + '_' + str(key)].config(text='A', bg='#8080ff')
                elif value == 'B':
                    self.grid_genes['g' + str(row) + '_' + str(key)].config(text='B', bg='#ffff80')
                elif value == 'C':
                    self.grid_genes['g' + str(row) + '_' + str(key)].config(text='C', bg='#ff8080')
                elif value == '-':
                    self.grid_genes['g' + str(row) + '_' + str(key)].config(text='-', bg='#FFFFFF')

        def grid_placer(organ):
            # W1 - r1_3, r3_1, r3_5, r5_3
            # W2 - r2_2, r2_4, r4_2, r4_4
            # W3 - r3_2, r3_4, r2_3, r4_3
            # W4 - r3_3
            if starting_whorl == 2:  # Diagonal
                imager(organ + 'NW.png', self.r2_2, self)
                imager(organ + 'SW.png', self.r4_2, self)  # Too lazy to fix images. Swapped V
                imager(organ + 'NE.png', self.r2_4, self)  # ^
                imager(organ + 'SE.png', self.r4_4, self)

            elif starting_whorl == 3:
                imager(organ + 'N.png', self.r2_3, self)
                imager(organ + 'W.png', self.r3_2, self)
                imager(organ + 'E.png', self.r3_4, self)
                imager(organ + 'S.png', self.r4_3, self)
            elif starting_whorl == 4:
                imager(organ + '.png', self.r3_3, self)
            else:
                if organ == 'Carpel':  # Carpel should be single not double.
                    imager(organ + 'N1.png', self.r1_3, self)
                    imager(organ + 'W.png', self.r3_1, self)
                    imager(organ + 'E.png', self.r3_5, self)
                    imager(organ + 'S1.png', self.r5_3, self)
                elif organ == 'Leaf':  # Correctly sized leaf.
                    imager(organ + 'N1.png', self.r1_3, self)
                    imager(organ + 'W1.png', self.r3_1, self)
                    imager(organ + 'E1.png', self.r3_5, self)
                    imager(organ + 'S1.png', self.r5_3, self)
                else:
                    imager(organ + 'N.png', self.r1_3, self)
                    imager(organ + 'W.png', self.r3_1, self)
                    imager(organ + 'E.png', self.r3_5, self)
                    imager(organ + 'S.png', self.r5_3, self)

        # possible_combinations = {'-A': 'sepal', '-C': 'carpel',
        #                          'BA': 'petal', 'BC': 'stamen', 'B-': 'hybrid',
        #                          '--': 'leaf'}

        # Loops through grid row 3 and 4, combines entries into a key which corresponds to a specific floral organ/leaf.
        # Starting whorl indicates which whorl that the organ needs to go in grid_placer.
        starting_whorl = 1
        for r1c, r2c in zip(self.grid[3].values(), self.grid[4].values()):
            if r1c + r2c == '-A':  # W1 or 4
                grid_placer('Sepal')
            elif r1c + r2c == '-C':  # W1 or 4
                grid_placer('Carpel')
            elif r1c + r2c == 'BA':  # W2 or 3
                grid_placer('Petal')
            elif r1c + r2c == 'BC':  # W2 or 3
                grid_placer('Stamen')
            elif r1c + r2c == 'B-':  # W2 or 3
                grid_placer('Hybrid')
            elif r1c + r2c == '--':  # W1, 2, 3 , or 4
                grid_placer('Leaf')
            starting_whorl += 1

        self.grid = copy.deepcopy(self.original_grid)


# No need for if __name__ == '__main__':
# Not planning on importing.
app = ABCWindow()
app.title('ABC Model')
app.resizable(0, 0)
app.mainloop()

# Built in PyCharm using Python 3.8
# Keisuke K. Oshima (5/30/20)
