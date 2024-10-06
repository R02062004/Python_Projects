#!/usr/bin/env python
# coding: utf-8

# In[54]:


from PIL import Image
import matplotlib.pyplot as plt

img = Image.open(r"C:\Users\moham\Desktop\meme_1.PNG")

plt.imshow(img)


# In[55]:


# Initialize ImageDraw
DRAW = ImageDraw.Draw(img)

# Preparing the Text Element
TEXT_1 = """Data Analyst with
  12Lakhs offerletter """

# Choose a font and size
font = ImageFont.truetype('arial.ttf', 50)

# Add text to the image
DRAW.text((800, 500), text=TEXT_1, fill=(255,255,255), font=font, align="center")

plt.imshow(img)


# In[56]:


# Initialize ImageDraw
DRAW = ImageDraw.Draw(img)

# Preparing the Text Element
TEXT_2 = """**Hiring for Data Analyst 
   salary 12.05 lakhs ** """

# Choose a font and size
font = ImageFont.truetype('arial.ttf', 70)

# Add text to the image
DRAW.text((0, 600), text=TEXT_2, fill=(0, 0,255), font=font, align="center")

plt.imshow(img)


# In[ ]:




