from tkinter import *
from PIL import ImageTk, Image

# default font style and color
DEFAULT_FONT = "Ubuntu"
TITLE_FONT_COLOR = "steel blue"
CONTENT_FONT_COLOR = "grey25"
# default align and justify
ALIGN = "left"
JUSTIFY = "left"
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
        self.right_rely = 0.2
        self.left_rely = 0.2
        
        self.line = Canvas(self, height=5, bg=TITLE_FONT_COLOR)
        self.line.place(relx=0.5, rely=0.185, relwidth=0.975,
                        anchor=CENTER)

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
     
    def content(self, string, align, font = DEFAULT_FONT, align_in = ALIGN,
                font_color = CONTENT_FONT_COLOR, justify = JUSTIFY,
                outline = False):
        """ Content for the slide 
        
        string    : Content string 
        align     : Content placement side
        font      : Content font style
        font_color: Content font color
        justify   : Justify content
        outline   : Show the outline of the text box
        """
        # Stripping the line char
        string = string.lstrip('\n')
        string = string.rstrip('\n')

        count = string.count('\n')
        # Main Alignment of the content
        if align == 'left':
            relx = 0.025
            rely = self.left_rely
            self.left_rely = self.left_rely + 0.075 + count*0.05
        elif align == 'right':
            relx = 0.525
            rely = self.right_rely
            self.right_rely = self.right_rely + 0.075 + count*0.05

        # Alignment inside of text box
        if align_in == 'left':
            anchor = 'w'
        elif align_in == 'center':
            anchor = align_in
        elif align_in == 'right':
            anchor = 'e'

        # Show the outline
        if outline == True:
            relief = 'solid'
        else:
            relief = 'flat'

        label = Label(self, text=string, bg='white', font=font+' 24',
                      fg=font_color, anchor=anchor, justify=justify,
                      wraplength=self.width/2-100, relief=relief)
        label.place(relx=relx, rely=rely, relwidth=0.45)
        
    def image(self, path, align, size = IMAGE_SIZE,
              outline = False):
        """ Image for the slide
        
        path  : The path of the image
        align : align the image in direction
        size  : size of the image resolution
        outline : shows the outline of the Fixed Image size
        """
        # Alignment of the content
        if align == 'left':
            relx=0.025
        elif align == 'right':
            relx=0.525

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
        label = Label(self, image=img, bg='white', anchor='center',
                      relief=relief)
        label.image = img
        label.place(relx=relx, rely=0.2, relwidth=0.45, relheight=0.75)
