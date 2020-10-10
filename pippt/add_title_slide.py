from tkinter import *

# default font style and color
DEFAULT_FONT = 'Ubuntu'
TITLE_FONT_COLOR = 'steel blue'
CONTENT_FONT_COLOR = 'grey25'
# default align and justify 
ALIGN = 'left'
JUSTIFY = 'center'

class add_title_slide(Frame):
    """ add_title_slide: For title and subtitle only
    
    - title()
    - subtitle()
    """    
    def __init__(self):
        """ Inherit the LabelFrame class in Tkinter module
        """
        LabelFrame.__init__(self, bg='white')
        self.width = self.winfo_screenwidth()
        
    def title(self, string, font = DEFAULT_FONT,
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
                      fg=font_color, bg='white', justify=justify,
                      wraplength=self.width-100)
        label.pack(side='top', padx=25, pady=(75,25))
        
    def subtitle(self, string, font = DEFAULT_FONT,
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
                      fg=font_color, bg='white', justify=justify,
                      wraplength=self.width-100)
        label.pack(side=side, padx=25, pady=(25,75))
