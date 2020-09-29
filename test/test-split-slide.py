from pippt import *

# Testing slide
app = Pippt(title='Test split slide')

# Test-1: add_split_slide
# default settings
frame1 = add_split_slide()
frame1.title('Testing Title method')
left_string="""
* Adding line 1 of the contents in left
* Adding line 2 of the contents in left
* Adding line 3 of the contents in left
"""
frame1.content(left_string, align='left')
right_string="""
* Adding line 1 of the contents in right
* Adding line 2 of the contents in right
* Adding line 3 of the contents in right
"""
frame1.content(right_string, align='right')

# Test-2: add_split_slide
# title: color and align
# content: adding content
# image : adding image
frame2 = add_split_slide()
frame2.title('Testing title align left', font_color= 'grey10', align='left')
string="""
* adding line 1 content 
* adding line 2 content 
* adding line 3 content
"""
frame2.content(string, align='left')
frame2.image('image/image_1.png', align='right', size=(400,300))

# Test-3: add_split_slide
# title: test without title
# content: adding content on right
# image: align left
frame3 = add_split_slide()
string="""
* adding line 1 content 
* adding line 2 content 
* adding line 3 content
"""
frame3.content(string, align='right')
frame3.image('image/image_1.png', align='left', size=(400,300))


# Bundle the frames
app.bundle(frame1, frame2, frame3)
# Keeps the application open 
app.mainloop()
