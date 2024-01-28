import face_recognition
import os
from django.conf import settings as s
import cv2


i = 0


def handle_uploaded_file(f):
    global i
    with open(f'{s.BASE_DIR}\\facedetect\\upload\\{f.name}.jpg',
              'wb+') as destination:
        # rest of your code

        for chunk in f.chunks():
            destination.write(chunk)

class Util:
    @staticmethod
    def imagetoBinary(image):
            with open(image, 'rb') as image_file:
            # Read the binary data from the image file
                binary_data = image_file.read()

            return binary_data


    @staticmethod
    def handle_uploaded_file(f):
        global i
        with open(f'{s.BASE_DIR}\\facedetect\\upload\\{f.name}', 'wb+') as destination:

            for chunk in f.chunks():
                destination.write(chunk)
        
        return f.name
    
    @staticmethod
    def handle_media_file(f,file="ved"):
        global i
        with open(f'{s.BASE_DIR}\\facedetect\\media\\{f.name}', 'wb+') as destination:

            for chunk in f.chunks():
                destination.write(chunk)
        
        return f.name
    @staticmethod
    def compare_faces_with_uploaded_image(image_search, media_dir=f"{s.BASE_DIR}\\facedetect"):
        try:
            # Initialize the face detector
            face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

            # Load the uploaded image
            image_path = os.path.join(media_dir, 'upload', image_search)
            image = cv2.imread(image_path)
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Detect faces in the uploaded image
            faces = face_detector.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            if len(faces) == 0:
                return "No faces detected in the uploaded image."

            # Load the uploaded image for face recognition
            mask_image = face_recognition.load_image_file(image_path)
            mask_face_locations = face_recognition.face_locations(mask_image)

            if len(mask_face_locations) == 0:
                return "No faces found in the masked image for face recognition."

            mask_face_encoding = face_recognition.face_encodings(mask_image)[0]

            # Initialize results list
            results = []

            # Compare faces from the uploaded image to faces in the media directory
            for file_name in os.listdir(f"{s.BASE_DIR}\\facedetect\\media"):
                if file_name.endswith(".jpg"):
                    print(file_name)
                    unknown_picture = face_recognition.load_image_file(os.path.join(media_dir, 'media', file_name))
                    unknown_face_encodings = face_recognition.face_encodings(unknown_picture)

                    for unknown_face_encoding in unknown_face_encodings:
                        match = face_recognition.compare_faces([mask_face_encoding], unknown_face_encoding)[0]
                        if match:
                            results.append(file_name)
                            return [True,file_name]

            return results if results else "No matching faces found in the media directory."

        except Exception as e:
            return f"An error occurred: {e}"


    # def match(imageSearch):
    #     print("this is to image ",imageSearch)
    #     items = os.listdir(f"{s.BASE_DIR}\\facedetect\\upload")
    #     total_items = len(items)
    #     print(f"Total items are {total_items}")
    #     picture_of_me = face_recognition.load_image_file(f"{s.BASE_DIR}\\facedetect\\upload\\{imageSearch}")
    #     my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
    #     unknown_picture = face_recognition.load_image_file(f"{s.BASE_DIR}\\facedetect\\media\\{i}.jpg")
    #     unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
    #     results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
        
    #     return results
        
    # @staticmethod
    # def match(fromImag, toimage):
    #     try:
    #         # Load the images
    #         picture_of_me = face_recognition.load_image_file(f"{s.BASE_DIR}\\facedetect\\upload\\{fromImag}")
    #         unknown_picture = face_recognition.load_image_file(f"{s.BASE_DIR}\\facedetect\\media\\{toimage}")

    #         # Get face encodings if faces are detected in both images
    #         my_face_encodings = face_recognition.face_encodings(picture_of_me)
    #         unknown_face_encodings = face_recognition.face_encodings(unknown_picture)

    #         if len(my_face_encodings) > 0 and len(unknown_face_encodings) > 0:
    #             my_face_encoding = my_face_encodings[0]
    #             unknown_face_encoding = unknown_face_encodings[0]

    #             # Compare face encodings
    #             results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
    #             return results
    #         else:
    #             # Handle case where no face is detected in one or both images
    #             return [False]

    #     except Exception as e:
    #         print(f"An error occurred: {e}")
    #         return [False]




    @staticmethod
    def count_items_in_folder(folder_path):
        try:
            # List all items (files and folders) in the specified folder
            items = os.listdir(folder_path)

            # Count the total number of items
            total_items = len(items)
            print(f"Total items are {total_items}")
            return total_items

        except FileNotFoundError:
            print(f"The folder at {folder_path} does not exist.")
            return None



