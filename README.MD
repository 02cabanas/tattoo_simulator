###### License: GNU Affero General Public License v3.0
# **Tattoo sumlator**
### GPT prompt Title is called "Python blender image rendering"

## Pre-production considerations:
- I am currently git-ignoring the __init__.so files of the bpy python extension that I'm using to interact with the Blender file using Python


## todo:
- YES
    - create overlay boundry with acurate dimensions, cut-outs and partitions according to sketched diagram in notes for day 6/26/2024
        - first get proportions in blender then probably finalise in photoshop
        - cut out knee cut out
    - render the three background images for the Front, Side, and Back of thigh
    - set up UI according to sketched diagram in notes for day 6/26/2024
    - add functionality to move uploaded image within overlay boundry
    - pass the uploaded image from the flask app to the simulate_tattoo.py file so that it can be added as a plane to the file model.blend in the 'blend.files' folder withing the 'flaskapp' folder.
- Optional
    - Make whole body symetric (for better uv unwrapping)
        - the face is symetric but other parts of the body are not; like the legs





## last sesh notes:
7/5/2024
<br/>
- THINKING OF SCRAPPING THE WHOLE PRJECTING TATTOO IDEA; thinking of doing UV mapping instead for the the tattoo overlay
- I was working on UV unwrapping; and how make seams to see whats possible to properly unwrap
    - trying to decide how big of body parts I want to work with basically
        - like thigh at a time or leg at a time, or lower body in general at a time, or whole body
- am having new thoughts for the UI maybe it goes like this
    - top of UI
        - a bunch of drop-down and the drop-down for example the first drop-down is upper body and then the next drop-down is lower body and then the lower body one is expanded and it shows left leg and shows right leg and then the right leg one is expanded and it shows thigh and lower leg and then the is checked so they all have checkboxes next to them and the only one that's checked is the thigh
    - middle UI
        - background UV unwrapp shape with color coded FRONT, BACK, INNER, OUTER with tatoo's overlayed on top and able to be moved (up,down,left,right)
    - bottom UI
        - key to match the colors on the above color coded UI shape to FRONT, BACK, INNER, OUTER
        - maybe a 3d model below that that is color coded with FRONT, BACK, INNER, OUTER colors and you can pan around to see where your tattoos would land basically in referance to how you located them in the middle UI Part

7/4/2024
<br/>
- I left of at trying to flatten my cutout though I should remember that Im not going to really use the flattened cutout to apply the tattoo. I need to apply via operations so this reallt is jsut a rough estimate.
- i need to cut out the knee hole

6/26/2024
<br/>
<br/>
<img src="images_extra/diagram_1.png" alt="UI diagram 1" width="300" style="margin-left: 50px;">
- so the steps after the user adjust the placement of the image inside the boundary plane would be to project the uploaded image onto that abnormally shaped plane and then deformed that plane around the already set up Bézier curve
- Thigh tattoo:
    - Also, for the thigh tattoo, we could do the same thing where they drop their image into an overlay box and then we split the image up inside the overlay box, for example, into three pieces, and then one piece will more or less land on the front of the thigh. The other piece will land more or less on the side of the thigh and the other piece were land, more or less on the back of the thigh, and we can give previews to those so they can kind of see where the pieces are gonna land before they select or render
- Back tattoo
    - For the blender tattoo program, we could actually set up an overly box and then the person places their tattoo in that box and then we split their tattoo into multiple pieces so they’ll be one piece that’ll go for example for example it’ll go on the bottom half of the back and then the other piece will go on the upper half of the back and then we’ll join those two pieces on maybe like two or three edges, but not the whole edges all across the middle so that the pieces can deform correctly so the lower piece can deform correctly around the lower back instead of snapping onto the arms
- Completed
    - set up git-lsf to track all *.blend and *.so files 
    - added and pushed whole repo to github (finally backed up my local directory to GitHub)


6/22/2024
- have to log of (>_<) .... but basically I think the most up to date blend file is /Users/fredo/Documents/Blender/Blender projects/Simulate_Tattoo/flaskapp/blend_files/model.blend   
- also check the renders folder to see how the adding image as plane execution went
- I was basically testing how to pass the uploaded image from the flask app to the simulate_tattoo.py file so that it can be added to the .blend file as a plane
<br><br>

6/20/2024

- Thigh tattoo: (NEW PROJECT DIRECTION)
    - I think I actually picked the most difficult body part to do so maybe I should look into doing thigh body part instead
    - We could make it so they drop their image into an overlay box and then we split the image up inside the overlay box, for example, into three pieces, and then one piece will more or less land on the front of the thigh. The other piece will land more or less on the side of the thigh and the other piece were land, more or less on the back of the thigh, and we can give previews to those so they can kind of see where the pieces are gonna land before they select or render

- Back tattoo Solutions
    - I could have an already existing Bézier curve That the image plain deform to In the Z axis; Vertical, Following the spine of the model.
    - ~~I should probably limit the movement in the X and Y Search that the edges of the image don't cross an overlaid box boundary(so that The bottom edges of the plane don't snap to the arm since they should be snapping to the torso)~~
    - ~~^^^^ So I should add an overlay box to contain the X and Y movement of the image~~
    - This one's DIFFICULT, I could add a bottom, Bézier curve to wrap Any parts of the image below certain point around the torso (again again to avoid the bottom edges of the plane snapping to the arm)~~
    - we could actually set up an overly box and then the person places their tattoo in that box and then we split their tattoo into multiple pieces so they’ll be one piece that’ll go for example for example it’ll go on the bottom half of the back and then the other piece will go on the upper half of the back and then we’ll join those two pieces on maybe like two or three edges, but not the whole edges all across the middle so that the pieces can deform correctly so the lower piece can deform correctly around the lower back instead of snapping onto the arms


## Description
- A website to easily generate realistic renders of how specific tattoos would look on a model body.



<br><br><br><br><br><br><br><br><br>
# Markdown Cheat Sheet

## Headers
# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6

## Emphasis
*italic* or _italic_

**bold** or __bold__

~~strikethrough~~

## Lists
- Unordered list item 1
- Unordered list item 2
  - Subitem 1
  - Subitem 2

1. Ordered list item 1
2. Ordered list item 2
   1. Subitem 1
   2. Subitem 2

## Links
[OpenAI](https://www.openai.com)

## Images
![OpenAI Logo](https://www.openai.com/logo.png)

## Blockquotes
> This is a blockquote.

## Code
Inline code: `inline code`

Code block: ??????

## Horizontal Rule
---
or
***
or
___

## Tables
| Header 1 | Header 2 |
|----------|----------|
| Row 1 Col 1 | Row 1 Col 2 |
| Row 2 Col 1 | Row 2 Col 2 |

## Task Lists
- [ ] Task 1
- [x] Task 2