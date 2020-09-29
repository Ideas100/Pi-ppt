from tkinter import *
from PIL import ImageTk, Image

# default title of window
TITLE = "Pippt"
# full size of window
FULL_SCREEN = "1300x700"
IMAGE_SIZE = (400, 400)
CODE_ONLY = (900, 480)
# default font style, size for title and content
TITLE_FONT = "Ubuntu"
CONTENT_FONT = "Ubuntu" 
# default font color for title and content, for more color visit
# http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
TITLE_FONT_COLOR = "steel blue"
CONTENT_FONT_COLOR = "grey25"
# default align of title and content
ALIGN = "left"
# default of justify of content
JUSTIFY = "center"


class Pippt(Tk):
    """ Pippt class inherits the Tk class from tkinter module
    """
    total_frames = 0
    current_frame = 0
    frames = ()
    
    def __init__(self, title=TITLE):
        """ Inheriting the tkinter class in tkinter module
        
        title: Title of the main window
        size : Size of the main window
        """
        Tk.__init__(self, className='Pippt')
        self.title(title)
        self.geometry(FULL_SCREEN)
        
        # Key binding for moving with slides, 
        self.bind('<Right>', self._next_slide)
        self.bind('<Left>', self._back_slide)

        # Button frame and button for quick access
        self.button_frame = Frame(self)
        self.button = []
        self.prev_button = 0
        self.curr_button = 0
        # Pages for the buttons to occupy
        self.page = 0
        self.total_page = 0
        # Left and right button to navigate between buttons
        self.left_button = Button(self.button_frame, text='<', font='Bold',
                                  bg='ghost white', state=DISABLED)
        self.left_button.pack(side='left', padx=(0,10))
        self.right_button = Button(self.button_frame, text='>', font='Bold',
                                   bg='ghost white', state=DISABLED)
        self.right_button.pack(side='right', padx=(10,0))
        
        # Status label for keep tracking of slides.
        self.status = Label(self)
        

    def bundle(self, *args):
        """ This method will have bundle's the frames 
        and create's list of buttons dynamically
        
        args : tuple of frames
        """
        self.frames = args
        self.total_frames = len(self.frames)-1
        # Button for the quick access for the slide's
        for item in range(1, len(self.frames)+1):
            if item in (1,2,3,4,5,6,7,8,9):
                string = '0'+ str(item)
            else:
                string = str(item)
            self.button.append(Button(self.button_frame, text=string,
                                      font='Bold', relief='sunken'))
            self.button[item-1].config(command=lambda val=item-1: self._switch_to(val))

        self.button[0].config(state=DISABLED)
        self._button_package()
        self.total_page = len(self.button) // 26
        # Activate left and right button's only more than 30 slides
        if len(self.button) > 26 :
            self.right_button.config(state=NORMAL, command=self._move_next_page)
            self.left_button.config(command=self._move_back_page)
            
        self._show_frame(self.frames[self.current_frame])


    def _button_package(self):
        """ Packing buttons according to size of frames.
        
        page: button accomdation per page is 30
        """
        self._button_unpackage()
        if self.page == 0:
            for item in self.button[:]:
                item.pack(side='left')
        elif self.page == 1:
            for item in self.button[26:]:
                item.pack(side='left')
        elif self.page == 2:
            for item in self.button[52:]:
                item.pack(side='left')
        elif self.page == 3:
            for item in self.button[78:]:
                item.pack(side='left')
                
    def _button_unpackage(self):
        """ Unpacking buttons that are previously present
        """
        for item in self.button:
            item.pack_forget()
        
    def _move_next_page(self):
        """ Moving next page for next set of buttons
        """
        if self.total_page > self.page:
            self.page += 1
            self.left_button.config(state=NORMAL)
            if self.page == self.total_page:
                self.right_button.config(state=DISABLED)         
        self._button_package()

    def _move_back_page(self):
        """ Moving back page for previous set of buttons
        """
        if self.page > 0:
            self.page -= 1
            self.right_button.config(state=NORMAL)
            if self.page == 0:
                self.left_button.config(state=DISABLED)
        self._button_package()

    def _switch_to(self, slide_no):
        """ This method will switch to slide which is being pressed
        
        slide_no : Button which is pressed
        """
        # storing previously and currently pressed button
        self.prev_button = self.curr_button
        self.curr_button = slide_no
        self._remove_frame(self.frames)
        self.current_frame = slide_no
        self._show_frame(self.frames[self.current_frame])
        # Disable the currently pressed button until next button is pressed.
        self.button[self.curr_button].config(state=DISABLED)
        self.button[self.prev_button].config(state=NORMAL)
        
    def _next_slide(self, event):
        """ Event handler for moving next slides
        """
        self._remove_frame(self.frames)
        self.bind('<Left>', self._back_slide)
        if self.current_frame < self.total_frames:
            self.current_frame += 1
            if self.current_frame == self.total_frames:
                self.unbind('<Right>')
            
        self.prev_button = self.curr_button
        self.curr_button = self.current_frame
        # Disable the currently pressed button until next button is pressed.
        self.button[self.curr_button].config(state=DISABLED)
        if self.prev_button != self.curr_button:
            self.button[self.prev_button].config(state=NORMAL)
        self._show_frame(self.frames[self.current_frame])
    
    def _back_slide(self, event):
        """ Event handler for moving back slides
        """
        self._remove_frame(self.frames)
        self.bind('<Right>', self._next_slide)
        if self.current_frame > 0:
            self.current_frame -= 1
            if self.current_frame == 0:
                self.unbind('<Left>')
            
        self.prev_button = self.curr_button
        self.curr_button = self.current_frame
        # Disable the currently pressed button until next button is pressed.
        self.button[self.curr_button].config(state=DISABLED)
        if self.prev_button != self.curr_button:
            self.button[self.prev_button].config(state=NORMAL)
        self._show_frame(self.frames[self.current_frame])
        
    def _show_frame(self, frame):
        """ show_frame will display the current frame in root window
        
        frame : current frame object for displaying the frame
        """            
        string = str(self.current_frame+1)+' of '+str(self.total_frames+1)
        self.status.config(text=string, font='Bold')

        self.button_frame.pack(padx=8, side='top')
        frame.pack(padx=10, pady=5, fill='both', expand='True')
        self.status.pack(side='bottom')       

    def _remove_frame(self, frames):
        """ remove_frame will remove the frame from the root window
        
        frames : tuple of frames 
        """
        for frame in frames:
            frame.pack_forget()



class add_title_slide(Frame):
    """ add_title_slide: For title and subtitle only
    
    - title()
    - subtitle()
    """
    
    def __init__(self):
        """ Inherit the LabelFrame class in Tkinter module
        """
        LabelFrame.__init__(self, bg='white')

        
    def title(self, string, font = TITLE_FONT,
              font_color = TITLE_FONT_COLOR, justify=JUSTIFY):
        """ Main title of the slide

        string    : Main title string 
        font      : Title font style
        font_color: Title font color
        justify   : Justify the Title
        """
        # Stripping the line char
        string = string.lstrip('\n')
        string = string.rstrip('\n')
        
        label = Label(self, text=string, font=font + ' 50 bold',
                      fg=font_color, bg='white', justify=justify)
        label.pack(side='top', padx=25, pady=(75,25))

        
    def subtitle(self, string, font = TITLE_FONT,
                 font_color = CONTENT_FONT_COLOR,
                 side = "top", justify = JUSTIFY):
        """ Subtitle of the slide
        
        string    : Subtitle of the slide
        font      : Subtitle Font style
        font_color: Subtitle Font color
        side      : side to align the subtitle
        justify   : Justify the subtitle
        """
        # Stripping the line char
        string = string.lstrip('\n')
        string = string.rstrip('\n')
        
        label = Label(self, text=string, font=font + ' 28 bold',
                      fg=font_color, bg='white', justify=justify)
        label.pack(side=side, padx=25, pady=(25,75))
    
    
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

        
    def title(self, string, font = TITLE_FONT,
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
                          fg=font_color, justify=align, padx=20)
        self.label.grid(row=0, column=self.col, columnspan=span,
                        padx=10, pady=(25,0), sticky=side)
        # config the color of line according to title color
        self.line.config(bg=font_color)
        self.line.grid(row=1, column=0, columnspan=3,
                       padx=10, pady=(5,10), sticky=W+E)


    def content(self, string, font = CONTENT_FONT,
                font_color = CONTENT_FONT_COLOR, align = ALIGN,
                justify = JUSTIFY, outline = False):
        """ Content for the slide
        
        string    : Content string
        font      : Content font style
        font_color: Content font color
        align     : Content alignment 
        just      : Content justify side 
        outline   : Showinng the outline of the content
        """
        self.row += 1
        value = 'flat'
        # Stripping line char 
        string = string.lstrip('\n')
        string = string.rstrip('\n')
        
        if   align == 'left':
            self.col, span, side = 0, 1, W
        elif align == 'right':
            self.col, span, side = 2, 1, E
        elif align == 'center':
            self.col, span, side = 0, 3, W+E

        if outline == True:
            value = 'solid'
            
        # Content line
        label = Label(self, text=string, font=font+' 24 ', fg=font_color,
                      bg='white', justify=justify, padx=50, relief=value)
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


    def codeblock(self, code=None, path=None, size=(800,300)):
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
        code_frame=Frame(canvas)
        # scroll x and y axis 
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
        
        canvas.create_window((0,0),window=code_frame,anchor='nw')
        code_frame.bind("<Configure>",
                   lambda e: canvas.configure(scrollregion=canvas.bbox("all"),
                                              width=wd, height=ht, bg='grey25'))   

        # Label the code inside.
        Label(code_frame, text=code, font='Courier 16 bold', fg='snow',
              bg='grey25', justify='left', padx=50, pady=50).pack()
  

              
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
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.col = 0
        self.left, self.right = 1, 1
        
        self.label = Label(self, height=4, bg='white')
        self.label.grid(row=0, column=0,
                        padx=25, pady=(25,0))
        self.line = Canvas(self, height=5, bg=TITLE_FONT_COLOR)
        self.line.grid(row=1, column=0, columnspan=3,
                       padx=10, pady=(5,10), sticky=W+E)


    def title(self, string, font = TITLE_FONT,
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
                          fg=font_color, justify=align, padx=20)
        self.label.grid(row=0, column=self.col, columnspan=span,
                        padx=10, pady=(25,0), sticky=side)
        # config the color of line according to title color
        self.line.config(bg=font_color)
        self.line.grid(row=1, column=0, columnspan=3,
                       padx=20, pady=(5,10), sticky=W+E)


    def content(self, string, align, font = CONTENT_FONT,
                font_color = CONTENT_FONT_COLOR, justify = JUSTIFY,
                outline = False):
        """ Content for the slide 
        
        string    : Content string 
        align     : Content placement side
        font      : Content font style
        font_color: Content font color
        justify   : Justify content
        """
        value = 'flat'
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

        # Making outline visible 
        if outline == True:
            value = 'solid'

        label = Label(self, text=string, font=font+' 24 ',
                      fg=font_color, bg='white',
                      justify=justify, relief=value)
        label.grid(row=row, column=self.col, columnspan=1,
                   padx=20, pady=5)


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
                   padx=10, pady=5)
