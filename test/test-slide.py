from pippt import *

# Testing slide
app = Pippt(title='Test slide')

# Test-1: add_slide
# default settings
frame1 = add_slide()
frame1.title('Test Title method')
frame1.content('Default settings:', font_color='black')
string="""
* align is left
* justify is left
"""
frame1.content(string)

# Test-2: add_slide
# title: color and align
# content: no of line and align
frame2 = add_slide()
frame2.title('Test title align left', align='left', font_color= 'grey10')
string="""
Adding more text to test the single line wrapping feature with default align and justify to be center.
"""
frame2.content(string, justify = 'center')

# Test-3: add_slide
# title: justify right
# image: image with default settings
frame3 = add_slide()
frame3.title('Test title align right', align='right')
frame3.content('Default Image size 400, 400')
frame3.image('image/image_1.png')

# Test-4: add_slide
# title: adding long title
# image: adjust size and align
frame4 = add_slide()
title="""Test title with a long title"""
frame4.title(title)
frame4.image('image/image_1.png', size=(400, 300))


# Test-5: add_slide
# title: adding title with split lines.
# codeblock: invoking a code file
frame5 = add_slide()
title = """
Testing title method with a long title
spliting into two lines
"""
frame5.title(title)
frame5.content('Swapping program!')
frame5.codeblock(path='code/code.c')


# Test-6: add_slide:
# title: adding title
# codeblock: increase the size with default value(CODE_ONLY)
frame6 = add_slide()
frame6.title('Testing title', align='center')
frame6.codeblock(path='code/code.c', size=CODE_ONLY)

# Test-7: add_slide:
# title: adding title
# codeblock: adding a code as a string type
frame7 = add_slide()
frame7.title('Testing Title')
frame7.content('Hello world program!')
string="""
#include <stdio.h>

int main()
{
        printf("Hello world!");

        return 0;
}
"""
frame7.codeblock(code=string)


# Bundle the frames
app.bundle(frame1, frame2, frame3, frame4, frame5, frame6, frame7)
# Keeps the application open 
app.mainloop()
