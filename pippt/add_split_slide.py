from tkinter import *
from PIL import ImageTk, Image

# default font style and color
DEFAULT_FONT = "Ubuntu"
TITLE_FONT_COLOR = "steel blue"
CONTENT_FONT_COLOR = "grey25"
# default align and justify
ALIGN = "left"
JUSTIFY = "center"
# default image size 
IMAGE_SIZE = (400, 400)

class add_split_slide(Frame):
    """ add_split_slide: Slide with two content space
    
    - title()
    - content()
    - image()
    """
    def __init__(self):
        """ Inherit the LabelFrames class in Tkinter module
        """
        LabelFrame.__init__(self, bg='white')
        self.width = self.winfo_screenwidth()
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=1)
        self.col = 0
        self.left, self.right = 1, 1
        
        self.label = Label(self, height=4, bg='white')
        self.label.grid(row=0, column=0,
                        padx=25, pady=(25,0))
        self.line = Canvas(self, height=5, bg=TITLE_FONT_COLOR)
        self.line.grid(row=1, column=0, columnspan=3,
                       padx=10, pady=(5,10), sticky=W+E)

    def title(self, string, font = DEFAULT_FONT,
              font_color = TITLE_FONT_COLOR, align = ALIGN):
        """ Title for the slide
        
        string    : Title string
        font      : Title font style
        font_color: Title font color
        align     : Title placement side
        """
        ht, side = 0, W
        # Stripping the line char
        string = string.lstrip('\n')
        string = string.rstrip('\n')
        # Adding height according to lines of string
        if '\n' in string:
            ht=string.count('\n')
            
        # Alignment changes for the grid
        if   align == 'left':
            self.col, span, side = 0, 1, W
        elif align == 'right':
            self.col, span, side = 2, 1, E
        elif align == 'center':
            self.col, span, side = 0, 3, W+E

        # config the title line according to input
        self.label.config(text=string, height=ht+1, font=font+' 45 bold',
                          fg=font_color, justify=align, padx=20,
                          wraplength=self.width-100)
        self.label.grid(row=0, column=self.col, columnspan=span,
                        padx=10, pady=(25,0), sticky=side)
        # config the color of line according to title color
        self.line.config(bg=font_color)
        self.line.grid(row=1, column=0, columnspan=3,
                       padx=20, pady=(5,10), sticky=W+E)

    def content(self, string, align, font = DEFAULT_FONT,
                font_color = CONTENT_FONT_COLOR, justify = JUSTIFY):
        """ Content for the slide 
        
        string    : Content string 
        align     : Content placement side
        font      : Content font style
        font_color: Content font color
        justify   : Justify content
        """
        # Stripping the line char
        string = string.lstrip('\n')
        string = string.rstrip('\n')
        # Alignment of the content
        if align == 'left':
            self.left += 1
            row, self.col = self.left, 0
        elif align == 'right':
            self.right += 1
            row, self.col = self.right, 2

        label = Label(self, text=string, font=font+' 24 ',fg=font_color,
                      bg='white', justify=justify,
                      wraplength=self.width/2)
        label.grid(row=row, column=self.col, columnspan=1,
                   padx=10, pady=10)

    def image(self, path, align, size = IMAGE_SIZE):
        """ Image for the slide
        
        path  : The path of the image
        align : align the image in direction
        size  : size of the image resolution
        """
        # Alignment of the content
        if align == 'left':
            self.left += 1
            row, self.col = self.left, 0
        elif align == 'right':
            self.right += 1
            row, self.col = self.right, 2
            
        # Opening image file
        load = Image.open(path)
        # Resizing it to fit inside screen
        resize = load.resize(size, Image.ANTIALIAS)
        # Loading the image
        img = ImageTk.PhotoImage(resize)
        label = Label(self, image=img, bg='white')
        label.image = img
        label.grid(row=row, column=self.col, columnspan=1,
                   padx=10, pady=10)
