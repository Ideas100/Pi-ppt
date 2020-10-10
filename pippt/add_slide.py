from tkinter import *
from PIL import ImageTk, Image

# default font style and color
DEFAULT_FONT = "Ubuntu"
TITLE_FONT_COLOR = "steel blue"
CONTENT_FONT_COLOR = "grey25"
# default align and justify
ALIGN = "left"
JUSTIFY = "center"
# default image and codeblock size
IMAGE_SIZE = (350, 350)
CODE_SIZE  = (1000, 300)
# Additional size constant for image and codeblock
IMAGE_ONLY = (500, 500)
CODE_ONLY  = (900, 480)

class add_slide(Frame):
    """ add_slide: Normal slide
    
    - title()
    - content()
    - image()
    - codeblock()
    """
    
    def __init__(self):
        """ Inherit the LabelFrames class in Tkinter module
        """
        LabelFrame.__init__(self, bg='white')
        self.width = self.winfo_screenwidth()
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=1)
        self.row, self.col = 2, 0
        
        self.label = Label(self, height=4, bg='white')
        self.label.grid(row=0, column=self.col,
                        padx=25, pady=(25,0))
        self.line = Canvas(self, height=5, bg=TITLE_FONT_COLOR)
        self.line.grid(row=1, column=self.col, columnspan=3,
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
        # Stripping the line char before and after in string
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
                          wraplength= self.width-100)
        self.label.grid(row=0, column=self.col, columnspan=span,
                        padx=10, pady=(25,0), sticky=side)
        # config the color of line according to title color
        self.line.config(bg=font_color)
        self.line.grid(row=1, column=0, columnspan=3,
                       padx=10, pady=(5,10), sticky=W+E)

    def content(self, string, font = DEFAULT_FONT,
                font_color = CONTENT_FONT_COLOR, align = ALIGN,
                justify = JUSTIFY):
        """ Content for the slide
        
        string    : Content string
        font      : Content font style
        font_color: Content font color
        align     : Content alignment 
        just      : Content justify side 
        """
        self.row += 1
        # Stripping line char 
        string = string.lstrip('\n')
        string = string.rstrip('\n')
        
        if   align == 'left':
            self.col, span, side = 0, 1, W
        elif align == 'right':
            self.col, span, side = 2, 1, E
        elif align == 'center':
            self.col, span, side = 0, 3, W+E

        # Content line
        label = Label(self, text=string, font=font+' 24 ', fg=font_color,
                      bg='white', justify=justify, padx=50,
                      wraplength=self.width-100)
        label.grid(row=self.row, column=self.col, columnspan=span,
                   padx=10, pady=5, sticky=side)

    def image(self, path, size = IMAGE_SIZE, align = ALIGN):
        """ Image for the slide
        
        path  : The path of the image
        size  : size of the image resolution
        align : align the image in direction
        """
        self.row += 1
        
        if   align == 'left':
            self.col, span, side = 0, 1, W
        elif align == 'right':
            self.col, span, side = 2, 1, E
        elif align == 'center':
            self.col, span, side = 0, 3, W+E
            
        # Opening image file
        load = Image.open(path)
        # Resizing it to fit inside screen
        resize = load.resize(size, Image.ANTIALIAS)
        # Loading the image
        img = ImageTk.PhotoImage(resize)
        label = Label(self, image=img, bg='white', padx=50)
        label.image = img
        label.grid(row=self.row, column=self.col, columnspan=span,
                   padx=10, pady=5, sticky=side)

    def codeblock(self, code = None, path = None, size = CODE_SIZE):
        """ Code for the slide 
        
        code  : Adding the code blocks
        path  : Path of the code
        size  : Size set to default or use CODE_ONLY to maximize
        """
        self.row += 1
        wd, ht = size

        if path != None:
            file_ = open(path, 'r')
            code = file_.read()
            
        # Creating sub frame and inserting a canvas 
        sub_frame=Frame(self, width=wd, height=ht,
                        bd=4, relief=RAISED)
        sub_frame.grid(row=self.row, column=0, columnspan=3,
                     padx=50, sticky=W)
        # canvas with sub_frame as root
        canvas=Canvas(sub_frame)
        # code_frame inside canvas 
        self.code_frame=Frame(canvas)
        # scroll x and y axis for horizontal and vertical scrolling
        scrollx=Scrollbar(sub_frame, orient="horizontal", bg='snow', width=17,
                          elementborderwidth=3, command=canvas.xview)
        canvas.configure(xscrollcommand=scrollx.set)
        scrolly=Scrollbar(sub_frame, orient="vertical", bg='snow', width=17,
                          elementborderwidth=3, command=canvas.yview)
        canvas.configure(yscrollcommand=scrolly.set)
        # packing the scrollbar
        scrollx.pack(side="bottom",fill=X)
        scrolly.pack(side="right",fill=Y)   
        canvas.pack(side="left")
        # creating window for code frame 
        canvas.create_window((0,0),window=self.code_frame,anchor='nw')
        self.code_frame.bind("<Configure>",
                   lambda e: canvas.configure(scrollregion=canvas.bbox("all"),
                                              width=wd, height=ht, bg='grey25'))
        # Adding up and down key for scrolling
        self.code_frame.focus_set()
        self.code_frame.bind("<Up>", lambda event: canvas.yview_scroll(-1, "units"))
        self.code_frame.bind("<Down>", lambda event: canvas.yview_scroll( 1, "units"))
        
        # Label the code into the code_frame
        Label(self.code_frame, text=code, font='Courier 16 bold', fg='snow',
              bg='grey25', justify='left', padx=50, pady=50).pack()
