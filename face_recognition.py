#change file name or it will give you error like :"AttributeError: module 'face_recognition' has no attribute 'load_image_file'"
import face_recognition
from PIL import Image, ImageDraw


image_obama = face_recognition.load_image_file("E:\py\known\obama.jpg")
obama_encoding= face_recognition.face_encodings(image_obama)[0]


image_modi = face_recognition.load_image_file("E:\py\known\modi.jpg")
modi_encoding= face_recognition.face_encodings(image_modi)[0]


known_face_encoding=[obama_encoding,modi_encoding]
known_face_name=["obama","modi"]

t_img=face_recognition.load_image_file("index.jpeg")

face_loc=face_recognition.face_locations(t_img)
face_encodings=face_recognition.face_encodings(t_img,face_loc)

pil_img=Image.fromarray(t_img)

draw=ImageDraw.Draw(pil_img)

for(top, right, bottom ,left), face_encoding in zip(face_loc,face_encodings):
    matches=face_recognition.compare_faces(known_face_encoding,face_encoding)
    name="unknown"

    if True in matches:
        first_match=matches.index(True)
        name=known_face_name[first_match]


    draw.rectangle(((left,top),(right,bottom)),outline=(0,0,0))

    text_width,text_height=draw.textsize(name)
    draw.rectangle(((left,bottom - text_height - 10),(right,bottom)),fill=(0,0,0),outline=(0,0,0))
    draw.text((left+6,bottom - text_height - 5), name,fill=(255,255,255,255))

pil_img.show()
