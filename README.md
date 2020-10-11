# Pi-ppt

Pi-ppt is a simple presentation module based on Tkinter. The goal is to provide
a new experience of creating a presentation by programming.

## Build

### Dependencies:
Requires a Tkinter module.

`$ apt-get install python3-tk`

`$ apt-get install python3-pil python3-pil.imagetk`

### Installation:
Install using pip.

**direct install**

`$ pip3 install pippt`

or

**clone and install**

`$ cd Pi-ppt`

`$ pip3 install .`

### Command Usage:
Generates a sample format of code under given slide name

`pi-ppt --init <slide_name>`

## Design
The Pi-ppt module is based tkinter. This module contains four classes
  * `Pippt`          
  * `add_title_slide`
  * `add_slide`      
  * `add_split_slide`

### Main window: [ `Pippt` ]
This class maintains the root window showing slides in the form of frames.
This class has a `bundle` method which uses to bundle all the slides(frames)
into the root window.
`app = Pippt()`
`app.bundle(frame_1, frame_2,...)`

### Frames: [ `add_title_slide`, `add_slide`, `add_split_slide` ]
These class maintains the each frame(slides) with their method. Methods
available in different class as metioned below.,

  * **title**    - `add_title_slide`, `add_slide`, `add_split_slide`
  * **subtitle** - `add_title_slide`
  * **content**  - `add_slide`, `add_split_slide`
  * **image**    - `add_slide`, `add_split_slide`
  * **codeblock**- `add_slide`

### Features:
Each frame has arguments like **font style, color, align and justify** which
is set to the default that can be customizable too.

Image and codeblock **size** can be changed accordingly.

Auto line wrapping

## Sample run:

`$ pi-ppt --init new_slide`

`$ cd new_slide/`

`$ python3 new_slide.py`

### Output:

![image](docs/screen_shot.png)
