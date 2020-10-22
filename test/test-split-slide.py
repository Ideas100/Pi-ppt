from pippt import *

# Testing slide
app = Pippt(title='Test split slide')

# Test-1: add_split_slide
# default settings
frame1 = add_split_slide()
frame1.title('Testing Title method')
left_string="""
Difference between
* align left
* align_in left
"""
frame1.content(left_string, align='left', outline=True)
right_string="""
Difference between
* align right
* align_in center
"""
frame1.content(right_string, align='right', align_in='center', outline=True)

# Test-2: add_split_slide
# title: color and align
# content: adding content
# image : adding image
frame2 = add_split_slide()
frame2.title('Testing title align center', font_color= 'grey15', align='center')

frame2.content('Adding line 1 content', align='left', align_in='center')
frame2.content('Adding line 2 content', align='left', align_in='center')
frame2.content('Adding line 3 content', align='left', align_in='center')
frame2.image('image/image_1.png', align='right', size=(400,300))

# Test-3: add_split_slide
# title: test without title
# content: adding content on right
# image: align left
frame3 = add_split_slide()
string="""
* Content with align_in and justify to be center
"""
frame3.title('Testing title align right', align='right')
frame3.content(string, align='right', align_in='center', justify='center')
frame3.image('image/image_1.png', align='left', size=(400,300))


# Bundle the frames
app.bundle(frame1, frame2, frame3)
# Keeps the application open 
app.mainloop()
