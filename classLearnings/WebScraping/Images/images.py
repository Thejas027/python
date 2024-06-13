from PIL import Image

img1 = Image.open('D:\python\classLearnings\WebScraping\practise-1\Deep_Blue.jpg')

print(type(img1))

# some functionalities that can be performed on images 

print(img1.size)   # gives the size of an image 

print(img1.filename)  # gives the file name with the path of an image 

print(img1.format_description) # gives the description of jpg image 

##### ---->       CROPPING OF AN IMAGE 

cropped_img = img1.crop((0,0,100,100))   # FORMAT --> left,upper,right,lower

cropped_img.show()  # to display the cropped image 

cropped_img.save('D:\python\classLearnings\WebScraping\Images')  # saving the cropped image 

img1.resize(())  # to resize the images 

img1.paste(im='path where to be pasted' , box=('coords')) # to paste the image where ever u want

img1.rotate(90)  # pass degree as a parameter to rotate the image 

################   --> COLOR TRANSPARENCY 

img1.putalpha(10)  # THE ALPHA CAN RANGE FROM  0 to 255 pass accordingly 