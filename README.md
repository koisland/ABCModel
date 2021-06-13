## ABC Model
I built this script for fun after noticing that that the class genes in the ABC Model 
slides in *EEMB 157CL* look really similar to the buttons used in Python's Tkinter module. It seemed like an easy fit 
and an interactive way to learn the ABC Model. I also figured that it wouldn't be too difficult to figure out an 
algorithm to predict what a perfect flower would look like if one disabled a given set of genes.

![](Images/Whole%20Images/No%20C%20in%20W4,%20B+C%20in%20W1+4.png)

### About
1. A grid that that prints ABC gene expression as a list in the python console.
	* This is used to generate the tkinter grid in (4).

2. An set of conditions that divides the top (B) and bottom (A and C) of the ABC model.
	* It goes through possible item combinations from (3) and updates the console grid.
	* Why divide them? Each level has different rules. 
  		* Top genes can only be B or - while bottom genes can be A, C, or -. 

3. A simple GUI with 4 whorl buttons and 3 gene buttons. These inputs disable gene expression.
	* Genes are given priority before whorls.
		* This means that pressing A and whorl 1 will disable A only in W1.
	* Inputs are placed in a list and used in (2).

4. A tkinter grid of empty labels that are later filled with a specific floral organ image.
	* Why a grid and not a single image?
		* **7 buttons == A lot of permutations/combinations...**
			* With v1.0 and v1.1, I did not sort so I would have to check for each permutation.
			* `- 7 * 6 * 5 * 4 * 3 * 2 * 1 = ~5040`
		* Even with the v1.2 where I sorted inputs, there are a lot of combinations to find.   
			* `(7 choose 1) + (7 choose 2 + (7 choose 3) + (7 choose 4) + (7 choose 5) + (7 choose 6) + (7 choose 7) = ~127`
		* A grid that auto-generates an image removes the need to check for a combination and
		add a specific image. 
		* It does come at the cost of neatness.
			* *Check the "Whole Images" folder* **( ; _ ;)**

### In-Progress

-[ ] *Image Upgrade*
	- Resize and rescale images to be equal size to prevent janky window changes.
-[ ] *Game Potential*
	- Generate random combination of console grid and have player guess what combination of gene/whorl disabling produces image.
-[ ] *ABCE Model*
	- Convert ABC model to ABCE model. This is the most difficult and would take the longest.
