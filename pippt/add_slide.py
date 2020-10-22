from tkinter import *
from PIL import ImageTk, Image

# default font style and color
DEFAULT_FONT = "Ubuntu"
TITLE_FONT_COLOR = "steel blue"
CONTENT_FONT_COLOR = "grey25"
# default align and justify
ALIGN = "left"
JUSTIFY = "left"
# default image and codeblock size
IMAGE_SIZE = (400, 400)
CODE_SIZE  = (1000, 300)
# Additional size constant codeblock
CODE_ONLY  = (1000, 450)

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
        self.rely = 0.2
        
        self.line = Canvas(self, height=5, bg=TITLE_FONT_COLOR)
        self.line.place(relx=0.5, rely=0.185, relwidth=0.975, anchor=CENTER)
        
    def title(self, string, font = DEFAULT_FONT,
              font_color = TITLE_FONT_COLOR, align = ALIGN):
        """ Title for the slide
        
        string    : Title string
        font      : Title font style
        font_color: Title font color
        align     : Title placement side
        """
        # Stripping the line char 
        string = string.lstrip('\n')
        string = string.rstrip('\n')
        # auto size adjustment for text size [default size is 45]
        size = 45
        rely = 0.03
        if len(string) > 40:
            size = round(size - (len(string)%40)/2)
            rely = 0.005

        # alignment fot the title
        if align == 'left':
            side, just = 'w', 'left' 
        elif align == 'center':
            side, just = align, 'center'
        elif align == 'right':
            side, just = 'e', 'right'
            
        label = Label(self, text=string, bg='white',
                      font=font+' '+str(size)+' '+ 'bold', fg=font_color,
                      anchor=side, justify=just, wraplength=self.width-50)
        self.line.config(bg=font_color)
        label.place(relx=0.05, rely=rely, relwidth=0.9)
        
    def content(self, string, font = DEFAULT_FONT,
                font_color = CONTENT_FONT_COLOR, align = ALIGN,
                justify = JUSTIFY, outline = False):
        """ Content for the slide
        
        string    : Content string
        font      : Content font style
        font_color: Content font color
        align     : Content alignment 
        justify   : Content justify side
        outline   : Show the outline of text box
        """
        # Stripping the line char 
        string = string.lstrip('\n')
        string = string.rstrip('\n')

        count = string.count('\n')
        # Alignment of text
        if align == 'left':
            anchor = 'w'
        elif align == 'center':
            anchor = align
        elif align == 'right':
            anchor = 'e'

        # show the outline
        if outline == True:
            relief = 'solid'
        else:
            relief = 'flat'
            
        label = Label(self, text=string, bg='white', font=font+' 24',
                      fg=font_color, anchor=anchor, justify=justify,
                      wraplength=self.width-100, relief=relief)
        label.place(relx=0.050, rely=self.rely, relwidth=0.9)
        # Calculation made for invoking new lines
        self.rely = self.rely + 0.075 + count*0.05

    def image(self, path, align = ALIGN, size = IMAGE_SIZE,
              outline = False):
        """ Image for the slide
        
        path    : The path of the image
        size    : size of the image resolution
        align   : align the image in direction
        outline : shows the outline of the Fixed Image size
        """
         # Alignment of the content
        if align == 'left':
            anchor = 'w'
        elif align == 'center':
            anchor = align
        elif align == 'right':
            anchor= 'e'

        # Shows the outline 
        if outline == True:
            relief = 'solid'
        else:
            relief = 'flat'
            
        # Opening image file
        load = Image.open(path)
        # Resizing it to fit inside screen
        resize = load.resize(size, Image.ANTIALIAS)
        # Loading the image
        img = ImageTk.PhotoImage(resize)
        label = Label(self, image=img, bg='white', anchor=anchor,
                      relief=relief)
        label.image = img
        label.place(relx=0.05, rely=self.rely, relwidth=0.90, relheight=0.70)

    def codeblock(self, code = None, path = None, size = CODE_SIZE):
        """ Code for the slide 
        
        code  : Adding the code blocks
        path  : Path of the code
        size  : Size set to default or use CODE_ONLY to maximize
        """
        wd, ht = size
        
        if path != None:
            file_ = open(path, 'r')
            code = file_.read()

        # Creating sub frame and inserting a canvas 
        sub_frame=Frame(self, width=wd, height=ht,
                        bd=4, relief=RAISED)
        sub_frame.place(relx=0.05, rely=self.rely)
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
