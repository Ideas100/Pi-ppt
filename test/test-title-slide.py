from pippt import *

# Testing title slide
app = Pippt(title='Test title slide')

# Test-1: add_title_slide
# default settings
frame1 = add_title_slide()
title ="""
Testing Title method
"""
frame1.title(title)
frame1.subtitle('Subtitle method')

# Test-2: add_title_slide
# title: font Times roman & justify left
# subtitle: font Courier & side right
frame2 = add_title_slide()
title ="""
Testing title method
justify left
"""
frame2.title(title, font='Times', justify='left')
frame2.subtitle('Subtitle: right', font='Courier', side='right')

# Test-3: add_title_slide
# title: color red4 &justify right
# subtitle: color grey35 &side left 
frame3 = add_title_slide()
title ="""
Testing title method
justify right
"""
frame3.title(title, font_color='red4', justify='right')
frame3.subtitle('Subtitle: left', font_color='grey35', side='left')

# Test-4: add_title_slide
# title: adding long title
# subtitle: adding long subtitle
frame4 = add_title_slide()
title="""
Testing title method with a long title
"""
frame4.title(title)
frame4.subtitle('Testing subtitle with a long text')


# Test-5: add_title_slide
# title: spliting a long text into two lines
frame5 = add_title_slide()
title = """
Testing title method with a long title
splitting into two lines
"""
subtitle="""
Testing subtitle method with long text
splitting and justifying it 
"""
frame5.title(title)
frame5.subtitle(subtitle, side='right', justify='right')

# Bundle the frames
app.bundle(frame1, frame2, frame3, frame4, frame5)
# Keeps the application open 
app.mainloop()
