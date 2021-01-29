import os
import pprint
import webbrowser
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import copy

original_grid = {1: {'Sepals': 1, 'Petals': 0, 'Stamen': 0, 'Carpels': 0},
                 2: {'A': 1, 'B': 1, 'C': 1},
                 3: {1: '-', 2: 'B', 3: 'B', 4: '-'},
                 4: {1: 'A', 2: 'A', 3: 'C', 4: 'C'}}
grid = copy.deepcopy(original_grid)
# Access item with grid[row (1, 2, or 3)][item (whorl or column #]
gene = []
whorl = []

# Needs to be sorted after every button press.
gene = sorted(gene)
whorl = sorted(whorl)


def column_filler(new_value, *args):
    for original_key in args:
        column[original_key] = new_value


for row, column in grid.items():
    for item in column:
        if row == 1 and grid[row][item] == 1:  # Disabled whorl.
            whorl.append(list(column).index(item) + 1)
        if row == 2 and grid[row][item] == 1:  # Disabled gene.
            gene.append(list(column).index(item) + 1)
    # Only whorl disabled.
    if not gene:
        # print(whorl)
        if row == 3 or row == 4:
            for w in whorl:
                column_filler('-', w)
    # Only gene disabled.
    elif not whorl:
        # print(gene)
        if gene == [2] and row == 3:  # B
            column_filler('-', 2, 3)
        elif gene == [1] and row == 4:  # A
            column_filler('C', 1, 2)
        elif gene == [3] and row == 4:  # C
            column_filler('A', 3, 4)
        elif gene == [1, 3] and row == 4:  # A+C
            column_filler('-', 1, 2, 3, 4)
        elif gene == [1, 2]:  # A+B
            if row == 3:
                column_filler('-', 2, 3)
            elif row == 4:
                column_filler('C', 1, 2)
        elif gene == [2, 3]:  # B+C
            if row == 3:
                column_filler('-', 2, 3)
            elif row == 4:
                column_filler('A', 3, 4)
        elif gene == [1, 2, 3]:  # A+B+C
            if row == 3:
                column_filler('-', 2, 3)
            elif row == 4:
                column_filler('-', 1, 2, 3, 4)
    elif gene and whorl:
        print('ok')

    # gene and whorl disabled.

print('', grid[1], '\n', grid[3], '\n', grid[4])

print('\n', original_grid[1], '\n', original_grid[3], '\n', original_grid[4])

print(whorl, gene)

# Pop entry and get key. Insert new entry at key opposite of it (A or C)
# pprint.pprint(grid)


# def disable(item):
#     # Button press removes old picture and product.
#     app.pic_frame.destroy()
#     app.product_frame.destroy()
#
#     whorls = ['Sepals', 'Petals', 'Stamen', 'Carpels']
#     genes = ['A', 'B', 'C']
#     if item in ABCWindow.target_whorl:  # Remove whorl if the same as previously pressed whorl.
#         ABCWindow.target_whorl.remove(item)
#         print(ABCWindow.target_whorl, ABCWindow.target_gene)
#         if item == 'Sepals':
#             app.whorl_1.config(relief='raised')
#         elif item == 'Petals':
#             app.whorl_2.config(relief='raised')
#         elif item == 'Stamen':
#             app.whorl_3.config(relief='raised')
#         elif item == 'Carpels':
#             app.whorl_4.config(relief='raised')
#         return
#     if item in whorls:
#         ABCWindow.target_whorl.append(item)
#         if item == 'Sepals':
#             app.whorl_1.config(relief='sunken')
#         elif item == 'Petals':
#             app.whorl_2.config(relief='sunken')
#         elif item == 'Stamen':
#             app.whorl_3.config(relief='sunken')
#         elif item == 'Carpels':
#             app.whorl_4.config(relief='sunken')
#
#     if item in ABCWindow.target_gene:
#         ABCWindow.target_gene.remove(item)
#         print(ABCWindow.target_whorl, ABCWindow.target_gene)
#         if item == 'A':
#             app.cls_a.config(bg='blue', relief='raised')
#         elif item == 'B':
#             app.cls_b.config(bg='yellow', relief='raised')
#         elif item == 'C':
#             app.cls_c.config(bg='red', relief='raised')
#         return
#     if item in genes:  # Add grid change here to reflect change.
#         ABCWindow.target_gene.append(item)
#         if item == 'A':
#             app.cls_a.config(bg='#8080ff', relief='sunken')
#         elif item == 'B':
#             app.cls_b.config(bg='#ffff80', relief='sunken')
#         elif item == 'C':
#             app.cls_c.config(bg='#ff8080', relief='sunken')
#     print(ABCWindow.target_whorl, ABCWindow.target_gene)
#
#
# def image(file, row, col, frame, main_widg):  # Insert image.
#     try:
#         img_path = os.path.expanduser('~\\Desktop\\ABC Model\\Images\\') + file
#         file = Image.open(img_path)
#         file = file.resize((300, 290), Image.ANTIALIAS)
#         render = ImageTk.PhotoImage(file, master=main_widg)
#         img = tk.Label(frame, relief='ridge', image=render)
#         img.image = render
#         img.grid(row=row, column=col, padx=10, pady=(0, 10))
#     except FileNotFoundError:
#         error_label = tk.Label(frame, text="'" + file + "' " + ' Not Found', font='Roboto 11', relief='ridge')
#         error_label.grid(row=row, column=col, padx=10, pady=(0, 10))
#
#
# class ABCWindow(tk.Tk):
#     # Button Response
#     target_whorl = []
#     target_gene = []
#
#     def __init__(self):
#         super().__init__()
#         self.whorl_frame = tk.Frame()
#         self.whorl_frame.grid(row=1, pady=(10, 0))
#         self.whorl_1 = tk.Button(self.whorl_frame, text='Sepals', font='Roboto 11', bg='#7fa905', width=12,
#                                  command=lambda: [disable('Sepals'), self.updating_abc()])
#         self.whorl_2 = tk.Button(self.whorl_frame, text='Petals', font='Roboto 11', bg='#f9dc00', width=12,
#                                  command=lambda: [disable('Petals'), self.updating_abc()])
#         self.whorl_3 = tk.Button(self.whorl_frame, text='Stamen', font='Roboto 11', bg='#66c3e7', width=12,
#                                  command=lambda: [disable('Stamen'), self.updating_abc()])
#         self.whorl_4 = tk.Button(self.whorl_frame, text='Carpels', font='Roboto 11', bg='#f2a064', width=12,
#                                  command=lambda: [disable('Carpels'), self.updating_abc()])
#
#         self.whorl_1.grid(row=1, column=1)
#         self.whorl_2.grid(row=1, column=2)
#         self.whorl_3.grid(row=1, column=3)
#         self.whorl_4.grid(row=1, column=4)
#
#         # Class gene frame
#         self.gene_frame = tk.Frame()
#         self.gene_frame.grid(row=2, padx=10, pady=10)
#         self.cls_a = tk.Button(self.gene_frame, text='Class A', font='Roboto 11', bg='blue', width=26,
#                                command=lambda: [disable('A'), self.updating_abc()])
#         self.cls_b = tk.Button(self.gene_frame, text='Class B', font='Roboto 11', bg='yellow', width=26,
#                                command=lambda: [disable('B'), self.updating_abc()])
#         self.cls_c = tk.Button(self.gene_frame, text='Class C', font='Roboto 11', bg='red', width=26,
#                                command=lambda: [disable('C'), self.updating_abc()])
#
#         self.cls_a.grid(row=2, column=1, columnspan=2)
#         self.cls_b.grid(row=1, column=2, columnspan=2)
#         self.cls_c.grid(row=2, column=3, columnspan=2)
#
#         # Results Label
#         self.update_frame = tk.Frame()
#         self.update_frame.grid(row=3, pady=(0, 10))
#         tk.Label(self, text=' - Results - ', font='Roboto 13 bold').grid(row=3)
#
#         # WT Picture Frame
#         self.pic_frame = tk.Frame()
#         self.pic_frame.grid(row=4)
#         image('wt.png', 1, 1, self.pic_frame, self)
#
#         # Class ABC Gene Labels
#         self.product_frame = tk.Frame()
#         self.product_frame.grid(row=5, pady=(0, 10))
#         update_cls_a = tk.Label(self.product_frame, text='A', font='Roboto, 9', bg='blue', width=26, relief='ridge')
#         update_cls_b = tk.Label(self.product_frame, text='B', font='Roboto, 9', bg='yellow', width=26, relief='ridge')
#         update_cls_c = tk.Label(self.product_frame, text='C', font='Roboto, 9', bg='red', width=26, relief='ridge')
#
#         update_cls_b.grid(row=1, column=1, columnspan=2)
#         update_cls_a.grid(row=2, column=1)
#         update_cls_c.grid(row=2, column=2)
#
#         # References
#         self.references = tk.Frame()
#         self.references.grid(row=6)
#         title = tk.Label(self.references, text=" - References - ", font='Roboto 13 bold')
#         ppr = tk.Button(self.references,
#                         text="Robles, Pedro & Pelaz, Soraya. (2005). Flower and fruit development in Arabidopsis thaliana.\n"
#                              "The International journal of developmental biology. 49. 633-43. 10.1387/ijdb.052020pr.",
#                         font='Roboto 9', relief='ridge', width=75,
#                         command=lambda: webbrowser.open("https://www.researchgate.net/publication/7663453_"
#                                                         "Flower_and_fruit_development_in_Arabidopsis_thaliana"))
#         book = tk.Label(self.references,
#                         text="Taiz L, Zeiger E. 2010. Plant Physiology and Development. 5th ed. \n"
#                              "Sinauer Associates. Chapter 24, The Control of Flowering; pg. 561-565",
#                         font='Roboto 9', relief='ridge', width=75)
#         title.grid(padx=10)
#         ppr.grid(padx=10)
#         book.grid(pady=(0, 10))
#
#         # tk.messagebox.showinfo(title="ABC Model (WIP!!!)",
#         #                        message="This is a work-in-progress and is missing combinations!"
#         #                                "\n\nIf you run into any errors or find something "
#         #                                "that is incorrect, please let me know! "
#         #                                "\n\n-Keith")
#
#     def updating_abc(self):
#         self.update_frame.destroy()
#         self.update_frame = tk.Frame(self)
#         tk.Label(self, text=' - Results - ', font='Roboto 13 bold').grid(row=3)
#         self.update_frame.grid(row=4, pady=(0, 10))
#
#         # ABC Result Frames
#         update_b_frame = tk.Frame(self.update_frame)
#         update_ac_frame = tk.Frame(self.update_frame)
#         picture_frame = tk.Frame(self.update_frame)
#         picture_frame.grid(row=1)
#         update_b_frame.grid(row=2)
#         update_ac_frame.grid(row=3)
#
#         # Empty Filler Labels
#         empty_label_bl = tk.Label(update_b_frame, width=26, relief='ridge')
#         empty_label_b = tk.Label(update_b_frame, width=13, relief='ridge')
#         empty_label_acl = tk.Label(update_ac_frame, width=26, relief='ridge')
#         empty_label_ac = tk.Label(update_ac_frame, width=13, relief='ridge')
#
#         # Filler AC Labels.
#         fill_a = tk.Label(update_ac_frame, text='A', font='Roboto 9', bg='blue', width=13, relief='ridge')
#         fill_c = tk.Label(update_ac_frame, text='C', font='Roboto 9', bg='red', width=13, relief='ridge')
#
#         # Class ABC Gene Labels
#         update_cls_a = tk.Label(update_ac_frame, text='A', font='Roboto 9', bg='blue', width=26, relief='ridge')
#         update_cls_b = tk.Label(update_b_frame, text='B', font='Roboto 9', bg='yellow', width=26, relief='ridge')
#         update_cls_c = tk.Label(update_ac_frame, text='C', font='Roboto 9', bg='red', width=26, relief='ridge')
#         update_cls_b.grid(row=1, column=2)
#         update_cls_a.grid(row=2, column=1)
#         update_cls_c.grid(row=2, column=2)
#
#         # Mutants
#         # WT or No A+B in whorl 4, B+C in whorl 1, A in whorl 3, A in whorl 4, B in whorl 1, B in whorl 4
#         if (ABCWindow.target_gene == [] and ABCWindow.target_whorl == []) or \
#                 (ABCWindow.target_gene == ['A', 'B'] or ABCWindow.target_gene == ['B', 'A']) \
#                 and ABCWindow.target_whorl == ['Carpels'] \
#                 or \
#                 (ABCWindow.target_gene == ['B', 'C'] or ABCWindow.target_gene == ['C', 'B']) \
#                 and ABCWindow.target_whorl == ['Sepals'] \
#                 or \
#                 ABCWindow.target_gene == ['A'] and ABCWindow.target_whorl == ['Stamen'] or \
#                 ABCWindow.target_gene == ['A'] and ABCWindow.target_whorl == ['Carpels'] or \
#                 ABCWindow.target_gene == ['B'] and ABCWindow.target_whorl == ['Sepals'] or \
#                 ABCWindow.target_gene == ['B'] and ABCWindow.target_whorl == ['Carpels'] or \
#                 ABCWindow.target_gene == ['C'] and ABCWindow.target_whorl == ['Sepals'] or \
#                 ABCWindow.target_gene == ['C'] and ABCWindow.target_whorl == ['Petals']:
#             image('wt.png', 1, 1, picture_frame, self)
#
#         # Whorl 1 disabled.
#         if ABCWindow.target_gene == [] and ABCWindow.target_whorl == ['Sepals'] or \
#                 (ABCWindow.target_gene == ['C', 'A'] or ABCWindow.target_gene == ['A', 'C']) \
#                 and ABCWindow.target_whorl == ['Sepals']:
#             update_cls_a.config(width=13)
#             empty_label_ac.grid(row=2, column=1)
#             update_cls_a.grid(row=2, column=2)
#             update_cls_c.grid(row=2, column=3)
#             image('No W1, A+C in W1.png', 1, 1, picture_frame, self)
#
#         # Whorl 2 disabled.
#         if ABCWindow.target_gene == [] and ABCWindow.target_whorl == ['Petals']:
#             # top adjustments
#             update_cls_b.config(width=12)
#             empty_label_bl.grid(row=1, column=1)
#             empty_label_b.grid(row=1, column=3)
#             # bottom adjustments
#             update_cls_a.config(width=13)
#             empty_label_ac.grid(row=2, column=2, padx=(1, 0))
#             empty_label_ac.config(width=12)
#             update_cls_c.grid(row=2, column=3)
#             image('No W2.png', 1, 1, picture_frame, self)
#
#         # Whorl 3 disabled or B & C disabled in W3
#         if ABCWindow.target_gene == [] and ABCWindow.target_whorl == ['Stamen'] or \
#                 (ABCWindow.target_gene == ['B', 'C'] or ABCWindow.target_gene == ['C', 'B']) \
#                 and ABCWindow.target_whorl == ['Stamen']:
#             # top adjustments
#             update_cls_b.config(width=12)
#             empty_label_bl.grid(row=1, column=3)
#             empty_label_b.grid(row=1, column=1)
#             # bottom adjustments
#             update_cls_a.grid(row=2, column=1)
#             empty_label_ac.grid(row=2, column=2, padx=(1, 0))
#             empty_label_ac.config(width=12)
#             update_cls_c.grid(row=2, column=3)
#             update_cls_c.config(width=13)
#             image('No W3, B+C in W3.png', 1, 1, picture_frame, self)
#
#         # Whorl 4 disabled.
#         if ABCWindow.target_gene == [] and ABCWindow.target_whorl == ['Carpels'] or \
#                 ((ABCWindow.target_gene == ['C', 'A'] or ABCWindow.target_gene == ['A', 'C'])
#                  and ABCWindow.target_whorl == ['Carpels']) \
#                 or \
#                 ((ABCWindow.target_gene == ['B', 'C'] or ABCWindow.target_gene == ['C', 'B'])
#                  and ABCWindow.target_whorl == ['Carpels']):
#             update_cls_c.config(width=13)
#             empty_label_ac.grid(row=2, column=3)
#             update_cls_a.grid(row=2, column=1)
#             update_cls_c.grid(row=2, column=2)
#             image('No W4, A+C in W4, B+C in W4.png', 1, 1, picture_frame, self)
#
#         # Whorl 1 & 2 disabled
#         if ABCWindow.target_gene == [] and \
#                 (ABCWindow.target_whorl == ['Sepals', 'Petals'] or ABCWindow.target_whorl == ['Petals', 'Sepals']):
#             empty_label_bl.grid(row=1, column=1)
#             empty_label_b.grid(row=1, column=3)
#             update_cls_b.config(width=12)
#             update_cls_a.destroy()
#             empty_label_acl.grid(row=2, column=1)
#             image('No W1+2.png', 1, 1, picture_frame, self)
#
#         # Whorl 1 & 3 disabled
#         if ABCWindow.target_gene == [] and \
#                 (ABCWindow.target_whorl == ['Sepals', 'Stamen'] or ABCWindow.target_whorl == ['Stamen', 'Sepals']):
#             # top adjustments
#             empty_label_b.grid(row=1, column=1)
#             update_cls_b.config(width=13)
#             empty_label_bl.grid(row=1, column=3)
#             # bottom adjustments
#             empty_label_ac.grid(row=2, column=1)
#             update_cls_a.config(width=13)
#             update_cls_a.grid(row=2, column=2)
#             tk.Label(update_ac_frame, width=12, relief='ridge').grid(row=2, column=3)
#             update_cls_c.grid(row=2, column=4)
#             update_cls_c.config(width=13)
#             image('No W1+3.png', 1, 1, picture_frame, self)
#
#         # Whorl 1 & 4 disabled
#         if ABCWindow.target_gene == [] and \
#                 (ABCWindow.target_whorl == ['Sepals', 'Carpels'] or ABCWindow.target_whorl == ['Carpels', 'Sepals']):
#             empty_label_ac.grid(row=2, column=1)
#             tk.Label(update_ac_frame, width=13, relief='ridge').grid(row=2, column=4)
#             update_cls_a.grid(row=2, column=2)
#             update_cls_c.grid(row=2, column=3)
#             update_cls_a.config(width=12)
#             update_cls_c.config(width=13)
#             image('No W1+4.png', 1, 1, picture_frame, self)
#
#         # Whorl 2 & 3 disabled
#         if ABCWindow.target_gene == [] and \
#                 (ABCWindow.target_whorl == ['Petals', 'Stamen'] or ABCWindow.target_whorl == ['Stamen', 'Petals']):
#             update_cls_b.destroy()
#             empty_label_bl.grid()
#             empty_label_acl.grid(row=2, column=2)
#             update_cls_c.grid(row=2, column=3)
#             update_cls_a.config(width=13)
#             update_cls_c.config(width=13)
#             image('No W2+3.png', 1, 1, picture_frame, self)
#
#         # Whorl 2 & 4 disabled
#         if ABCWindow.target_gene == [] and \
#                 (ABCWindow.target_whorl == ['Petals', 'Carpels'] or ABCWindow.target_whorl == ['Carpels', 'Petals']):
#             # top adjustments
#             update_cls_b.config(width=13)
#             empty_label_bl.grid(row=1, column=1)
#             empty_label_b.grid(row=1, column=3)
#             # bottom adjustments
#             update_cls_a.config(width=13)
#             empty_label_ac.grid(row=2, column=2, padx=(1, 0))
#             empty_label_ac.config(width=12)
#             update_cls_c.grid(row=2, column=3)
#             update_cls_c.config(width=13)
#             tk.Label(update_ac_frame, width=13, relief='ridge').grid(row=2, column=4)
#             image('No W2+4.png', 1, 1, picture_frame, self)
#
#         # Whorl 3 & 4 disabled
#         if ABCWindow.target_gene == [] and \
#                 (ABCWindow.target_whorl == ['Stamen', 'Carpels'] or ABCWindow.target_whorl == ['Carpels', 'Stamen']):
#             # top adjustments
#             update_cls_b.config(width=12)
#             empty_label_bl.grid(row=1, column=3)
#             empty_label_b.grid(row=1, column=1)
#             # bottom adjustments
#             update_cls_a.grid(row=2, column=1)
#             empty_label_ac.grid(row=2, column=2)
#             empty_label_ac.config(width=26)
#             update_cls_c.destroy()
#             image('No W3+4.png', 1, 1, picture_frame, self)
#
#         # Whorl 1, 2, & 3 disabled
#         if ABCWindow.target_gene == [] and \
#                 (ABCWindow.target_whorl == ['Sepals', 'Petals', 'Stamen'] or
#                  ABCWindow.target_whorl == ['Sepals', 'Stamen', 'Petals'] or
#                  ABCWindow.target_whorl == ['Petals', 'Sepals', 'Stamen'] or
#                  ABCWindow.target_whorl == ['Petals', 'Stamen', 'Sepals'] or
#                  ABCWindow.target_whorl == ['Stamen', 'Sepals', 'Petals'] or
#                  ABCWindow.target_whorl == ['Stamen', 'Petals', 'Sepals']):
#             empty_label_bl.grid(row=1, column=1)
#             update_cls_b.destroy()
#             update_cls_a.destroy()
#             update_cls_c.config(width=12)
#             empty_label_acl.grid(row=2, column=1)
#             empty_label_acl.config(width=39)
#             image('No W1+2+3.png', 1, 1, picture_frame, self)
#
#         # Whorl 1, 2, & 4 disabled
#         if ABCWindow.target_gene == [] and \
#                 (ABCWindow.target_whorl == ['Sepals', 'Petals', 'Carpels'] or
#                  ABCWindow.target_whorl == ['Sepals', 'Carpels', 'Petals'] or
#                  ABCWindow.target_whorl == ['Petals', 'Sepals', 'Carpels'] or
#                  ABCWindow.target_whorl == ['Petals', 'Carpels', 'Sepals'] or
#                  ABCWindow.target_whorl == ['Carpels', 'Sepals', 'Petals'] or
#                  ABCWindow.target_whorl == ['Carpels', 'Petals', 'Sepals']):
#             empty_label_bl.grid(row=1, column=1)
#             empty_label_b.grid(row=1, column=3)
#             update_cls_b.config(width=12)
#             update_cls_a.destroy()
#             update_cls_c.config(width=12)
#             empty_label_ac.grid(row=2, column=3)
#             empty_label_acl.grid(row=2, column=1)
#             image('No W1+2+4.png', 1, 1, picture_frame, self)
#
#         # Whorl 1, 3, & 4 disabled
#         if ABCWindow.target_gene == [] and \
#                 (ABCWindow.target_whorl == ['Sepals', 'Stamen', 'Carpels'] or
#                  ABCWindow.target_whorl == ['Sepals', 'Carpels', 'Stamen'] or
#                  ABCWindow.target_whorl == ['Stamen', 'Sepals', 'Carpels'] or
#                  ABCWindow.target_whorl == ['Stamen', 'Carpels', 'Sepals'] or
#                  ABCWindow.target_whorl == ['Carpels', 'Sepals', 'Stamen'] or
#                  ABCWindow.target_whorl == ['Carpels', 'Stamen', 'Sepals']):
#             # top adjustments
#             empty_label_b.grid(row=1, column=1)
#             update_cls_b.config(width=13)
#             empty_label_bl.grid(row=1, column=3)
#             # bottom adjustments
#             empty_label_ac.grid(row=2, column=1)
#             update_cls_a.config(width=13)
#             update_cls_a.grid(row=2, column=2)
#             tk.Label(update_ac_frame, width=26, relief='ridge').grid(row=2, column=3)
#             update_cls_c.destroy()
#             image('No W1+3+4.png', 1, 1, picture_frame, self)
#
#         # Whorl 2, 3, & 4 disabled
#         if ABCWindow.target_gene == [] and \
#                 (ABCWindow.target_whorl == ['Petals', 'Stamen', 'Carpels'] or
#                  ABCWindow.target_whorl == ['Petals', 'Carpels', 'Stamen'] or
#                  ABCWindow.target_whorl == ['Stamen', 'Petals', 'Carpels'] or
#                  ABCWindow.target_whorl == ['Stamen', 'Carpels', 'Petals'] or
#                  ABCWindow.target_whorl == ['Carpels', 'Petals', 'Stamen'] or
#                  ABCWindow.target_whorl == ['Carpels', 'Stamen', 'Petals']):
#             update_cls_b.destroy()
#             empty_label_bl.grid()
#             empty_label_acl.grid(row=2, column=2)
#             empty_label_acl.config(width=40)
#             update_cls_c.destroy()
#             update_cls_a.config(width=13)
#             image('No W2+3+4.png', 1, 1, picture_frame, self)
#
#         # A disabled, A disabled in whorl 1 & 2, or AB disabled in whorl 1.
#         if (ABCWindow.target_gene == ['A'] and ABCWindow.target_whorl == []) or \
#                 ((ABCWindow.target_whorl == ['Petals', 'Sepals'] or ABCWindow.target_whorl == ['Sepals', 'Petals'])
#                  and ABCWindow.target_gene == ['A']) \
#                 or \
#                 (ABCWindow.target_gene == ['A', 'B'] or ABCWindow.target_gene == ['B', 'A']) \
#                 and ABCWindow.target_whorl == ['Sepals']:
#             update_cls_a.destroy()
#             update_cls_c.config(width=52)
#             image('No A, A in W1+2, A+B in W1.png', 1, 1, picture_frame, self)
#
#         # A disabled in whorl 1
#         if ABCWindow.target_gene == ['A'] and ABCWindow.target_whorl == ['Sepals']:
#             update_cls_a.config(width=13)
#             update_cls_a.grid(row=2, column=2)
#             fill_c.grid(row=2, column=1)
#             update_cls_c.grid(row=2, column=3)
#             image('No A in W1.png', 1, 1, picture_frame, self)
#
#         # A disabled in whorl 2 or A disabled in whorl 2 & 3
#         if ABCWindow.target_gene == ['A'] and ABCWindow.target_whorl == ['Petals'] or \
#                 ((ABCWindow.target_whorl == ['Petals', 'Stamen'] or ABCWindow.target_whorl == ['Stamen', 'Petals'])
#                  and ABCWindow.target_gene == ['A']):
#             update_cls_a.config(width=13)
#             update_cls_c.config(width=39)
#             image('No A in W2, A in W2+3.png', 1, 1, picture_frame, self)
#
#         # B disabled or B disabled in whorl 2 and 3.
#         if (ABCWindow.target_gene == ['B'] and ABCWindow.target_whorl == []) or \
#                 ((ABCWindow.target_whorl == ['Petals', 'Stamen'] or ABCWindow.target_whorl == ['Stamen', 'Petals'])
#                  and ABCWindow.target_gene == ['B']):
#             update_cls_b.destroy()
#             empty_label_bl.grid(row=1)
#             image('No B, B in W2+3.png', 1, 1, picture_frame, self)
#
#         # B disabled in whorl 2 or B & C disabled in whorl 2
#         if ABCWindow.target_gene == ['B'] and ABCWindow.target_whorl == ['Petals'] \
#                 or \
#                 (ABCWindow.target_gene == ['B', 'C'] or ABCWindow.target_gene == ['C', 'B']) \
#                 and ABCWindow.target_whorl == ['Petals']:
#             update_cls_b.config(width=12)
#             empty_label_bl.grid(row=1, column=1)
#             empty_label_b.grid(row=1, column=3)
#             image('No B in W2, B+C in W2.png', 1, 1, picture_frame, self)
#
#         # B disabled in whorl 3 or AB disabled in whorl 3
#         if (ABCWindow.target_gene == ['B'] and ABCWindow.target_whorl == ['Stamen']) \
#                 or \
#                 (ABCWindow.target_gene == ['A', 'B'] or ABCWindow.target_gene == ['B', 'A']) \
#                 and ABCWindow.target_whorl == ['Stamen']:
#             update_cls_b.config(width=12)
#             update_cls_b.grid(row=1, column=2)
#             empty_label_bl.grid(row=1, column=3)
#             empty_label_b.grid(row=1, column=1)
#             image('No B in W3, A+B in W3.png', 1, 1, picture_frame, self)
#
#         # C disabled or C disabled in whorl 3 & 4
#         if (ABCWindow.target_gene == ['C'] and ABCWindow.target_whorl == []) or \
#                 ((ABCWindow.target_whorl == ['Carpels', 'Stamen'] or ABCWindow.target_whorl == ['Stamen', 'Carpels'])
#                  and ABCWindow.target_gene == ['C']):
#             update_cls_c.destroy()
#             update_cls_a.config(width=52)
#             image('No C, C in W3+4.png', 1, 1, picture_frame, self)
#
#         # C disabled in whorl 3.
#         if ABCWindow.target_gene == ['C'] and ABCWindow.target_whorl == ['Stamen']:
#             update_cls_a.config(width=40)
#             update_cls_c.config(width=13)
#             update_cls_c.grid(row=2, column=3)
#             image('No C in W3.png', 1, 1, picture_frame, self)
#
#         # C disabled in whorl 4.
#         if ABCWindow.target_gene == ['C'] and ABCWindow.target_whorl == ['Carpels']:
#             update_cls_c.config(width=13)
#             fill_a.grid(row=2, column=3)
#             image('No C in W4.png', 1, 1, picture_frame, self)
#
#         # A & B disabled
#         if ABCWindow.target_whorl == [] and (
#                 ABCWindow.target_gene == ['A', 'B'] or ABCWindow.target_gene == ['B', 'A']):
#             update_cls_a.destroy()
#             update_cls_b.destroy()
#             empty_label_bl.grid()
#             update_cls_c.config(width=52)
#             image('No A+B.png', 1, 1, picture_frame, self)
#
#         # A & B disabled in whorl 2
#         if ABCWindow.target_whorl == ['Petals'] and (
#                 ABCWindow.target_gene == ['A', 'B'] or ABCWindow.target_gene == ['B', 'A']):
#             # top adjustments
#             update_cls_b.config(width=12)
#             empty_label_bl.grid(row=1, column=1)
#             empty_label_b.grid(row=1, column=3)
#             # bottom adjustments
#             update_cls_a.config(width=13)
#             update_cls_c.grid(row=2, column=3)
#             update_cls_c.config(width=39)
#             image('No A+B in W2.png', 1, 1, picture_frame, self)
#
#         # A & C disabled
#         if (ABCWindow.target_gene == ['C', 'A'] or ABCWindow.target_gene == ['A',
#                                                                              'C']) and ABCWindow.target_whorl == []:
#             update_cls_a.destroy()
#             update_cls_c.destroy()
#             empty_label_acl.grid(row=2, column=1)
#             tk.Label(update_ac_frame, width=26, relief='ridge').grid(row=2, column=2)
#             image('No A+C.png', 1, 1, picture_frame, self)
#
#         # A & C disabled in whorl 2
#         if (ABCWindow.target_gene == ['C', 'A'] or ABCWindow.target_gene == ['A', 'C']) \
#                 and ABCWindow.target_whorl == ['Petals']:
#             # bottom adjustments
#             update_cls_a.config(width=13)
#             empty_label_ac.grid(row=2, column=2, padx=(1, 0))
#             empty_label_ac.config(width=12)
#             update_cls_c.grid(row=2, column=3)
#             image('No A+C in W2.png', 1, 1, picture_frame, self)
#
#         # A & C disabled in whorl 3
#         if (ABCWindow.target_gene == ['C', 'A'] or ABCWindow.target_gene == ['A', 'C']) \
#                 and ABCWindow.target_whorl == ['Stamen']:
#             # bottom adjustments
#             empty_label_ac.grid(row=2, column=2, padx=(1, 0))
#             empty_label_ac.config(width=12)
#             update_cls_c.grid(row=2, column=3)
#             update_cls_c.config(width=12)
#             image('No A+C in W3.png', 1, 1, picture_frame, self)
#
#         # B & C disabled
#         if (ABCWindow.target_gene == ['B', 'C'] or ABCWindow.target_gene == ['C',
#                                                                              'B']) and ABCWindow.target_whorl == []:
#             update_cls_b.destroy()
#             update_cls_c.destroy()
#             empty_label_bl.grid()
#             update_cls_a.config(width=52)
#             image('No B+C.png', 1, 1, picture_frame, self)
#
#         # A, B, & C disabled or any combination of whorls disabled
#         if (('A' in ABCWindow.target_gene and 'B' in ABCWindow.target_gene and 'C' in ABCWindow.target_gene)
#             and ABCWindow.target_whorl == []) \
#                 or \
#                 (('Sepals' in ABCWindow.target_whorl and 'Petals' in ABCWindow.target_whorl
#                   and 'Stamen' in ABCWindow.target_whorl and 'Carpels' in ABCWindow.target_whorl)
#                  and ABCWindow.target_gene == []):
#             update_cls_a.destroy()
#             update_cls_b.destroy()
#             update_cls_c.destroy()
#             empty_label_bl.grid()
#             empty_label_acl.grid(row=2, column=1)
#             tk.Label(update_ac_frame, width=26, relief='ridge').grid(row=2, column=2)
#             image('No A+B+C.png', 1, 1, picture_frame, self)
#
#
# # No need for if __name__ == '__main__':
# # Not planning on importing.
# app = ABCWindow()
# app.title('ABC Model')
# app.resizable(0, 0)
# app.mainloop()
#
# # Built in PyCharm using Python 3.8
# # Keisuke K. Oshima (5/30/20)
