from tkinter import *
from pippt.add_title_slide import *
from pippt.add_slide import *
from pippt.add_split_slide import *

# default title of window
_TITLE = "Pippt"
# default number of button's for one page is 16
_BUTTONS_PER_PAGE = 16

class Pippt(Tk):
    """ Pippt class inherits the Tk class from tkinter module
    """
    total_frames = 0
    current_frame = 0
    frames = ()
    
    def __init__(self, title=_TITLE):
        """ Inheriting the tkinter class in tkinter module
        
        title: Title of the main window
        """
        Tk.__init__(self, className='Pippt')
        self.title(title)
        # Get the size of screen dynamically
        width=self.winfo_screenwidth()
        height=self.winfo_screenheight()
        self.geometry(str(width)+'x'+str(height))
        
        # Key binding for moving next or previous slides 
        self.bind('<Right>', self._next_slide)
        self.bind('<Left>', self._back_slide)
        
        # Button frame to holds slide button's for quick access of slides
        self.button_frame = Frame(self)
        self.button = []
        self.prev_button = 0
        self.curr_button = 0
        # Assigning pages to have N number of button's 
        self.page = 0
        self.total_page = 0
        # Left and right button to navigate between the pages.
        self.left_button = Button(self.button_frame, text='<', font='Bold',
                                  bg='ghost white', state=DISABLED)
        self.left_button.pack(side='left', padx=(0,10))
        self.right_button = Button(self.button_frame, text='>', font='Bold',
                                   bg='ghost white', state=DISABLED)
        self.right_button.pack(side='right', padx=(10,0))
        
        # Status label for keep tracking of slides.
        self.status = Label(self)
        
    def bundle(self, *args):
        """ This method will bundle's the frames and create's 
        list of buttons respective to frame's dynamically
        
        args : tuple of frames
        """
        self.frames = args
        self.total_frames = len(self.frames)-1
        # Button for the quick access for the slide's
        for item in range(1, len(self.frames)+1):
            # Adding 0's to the single digit
            if item in (1,2,3,4,5,6,7,8,9):
                string = '0'+ str(item)
            else:
                string = str(item)
            self.button.append(Button(self.button_frame, text=string,
                                      font='Bold', relief='sunken'))
            # Direct switching to the slide using button
            self.button[item-1].config(command=lambda val=item-1: self._switch_to(val))

        self.button[0].config(state=DISABLED)
        self._button_package()
        self.total_page = len(self.button) // _BUTTONS_PER_PAGE
        # Activate left and right button's only more than 16 slides
        if self.total_page > 0 :
            self.right_button.config(state=NORMAL, command=self._move_next_page)
            self.left_button.config(command=self._move_back_page)
        self._show_frame(self.frames[self.current_frame])

    def _button_package(self):
        """ Packing buttons according to size of frames.
        
        page: button accomdation per page is 16
        """
        self._button_unpackage()
        for item in self.button[(self.page)*_BUTTONS_PER_PAGE : (self.page+1)*_BUTTONS_PER_PAGE]:
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
                # Disabling the next page button after reaching the last page
                self.right_button.config(state=DISABLED)         
        self._button_package()

    def _move_back_page(self):
        """ Moving back page for previous set of buttons
        """
        if self.page > 0:
            self.page -= 1
            self.right_button.config(state=NORMAL)
            if self.page == 0:
                # Disabling the back page button when reaching the first page
                self.left_button.config(state=DISABLED)
        self._button_package()

    def _switch_to(self, slide_no):
        """ This method will switch to slide which is being pressed
        
        slide_no : Button which is pressed
        """
        self._remove_frame(self.frames)
        self.current_frame = slide_no
        self._show_frame(self.frames[self.current_frame])
        # storing previously and currently pressed button
        self.prev_button = self.curr_button
        self.curr_button = slide_no
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

        # Switching pages according to the slide number
        if self.current_frame > ((self.page+1) * _BUTTONS_PER_PAGE)-1:
            self._move_next_page()
                
        self.prev_button = self.curr_button
        self.curr_button = self.current_frame
        # Disabling the currently pressed button.
        self.button[self.curr_button].config(state=DISABLED)
        if self.prev_button != self.curr_button:
            # Activating the previously pressed button
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
                
        # Switching pages according the slide number          
        if self.current_frame < ((self.page) * _BUTTONS_PER_PAGE):
            self._move_back_page()
            
        self.prev_button = self.curr_button
        self.curr_button = self.current_frame
        # Disabling the currently pressed button.
        self.button[self.curr_button].config(state=DISABLED)
        if self.prev_button != self.curr_button:
            # Activating the previously pressed button
            self.button[self.prev_button].config(state=NORMAL)
        self._show_frame(self.frames[self.current_frame])
        
    def _show_frame(self, frame):
        """ show_frame will display the slide, buttons and status in the window
        
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
