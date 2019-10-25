import face_recognition
import numpy as np
import helper
import cv2
import os

path_out_images = 'source_img/output/'
path_known_images = 'source_img/known_people/'
path_unknow_images = 'source_img/unknown/'
image_extension = "*.jpeg"
width_max_image = 800


def get_list_face_encodings_and_names(list_known_images, sep="#"):
    '''
    # Get list know images
    :param list_known_images: List of images
    :param sep: Image name separator
    :return: Return Face Encodings and Face names list
    '''

    known_face_encodings = []
    known_face_names = []

    for img_know in list_known_images:
        image_load = face_recognition.load_image_file(img_know)
        if len(face_recognition.face_encodings(image_load)) > 0:
            known_face_encoding = face_recognition.face_encodings(image_load)[0]
            known_face_encodings.append(known_face_encoding)
            known_face_names.append(img_know.split(os.sep)[-1].split(sep)[0].capitalize())

    return known_face_encodings, known_face_names


def resize_images(list_images, width):
    '''
    Resize images
    :param list_images: List of Images
    :param width: width final image resize
    :return:
    '''
    for img in list_images:
        image_resized = helper.resize_image(img, width)
        image_resized.save(img)


list_known_images = helper.get_files_dir(path_known_images, image_extension)
list_images_unknow = helper.get_files_dir(path_unknow_images, image_extension)

resize_images(list_known_images, width_max_image)
resize_images(list_images_unknow, width_max_image)

known_face_encodings, known_face_names = get_list_face_encodings_and_names(list_known_images)

for image_file in list_images_unknow:

    # get image name into current_file
    current_file_name = image_file.split(os.sep)[-1]

    # Load an image with an unknown face
    unknown_image = face_recognition.load_image_file(image_file)

    # Find all the faces and face encodings in the unknown image
    face_locations = face_recognition.face_locations(unknown_image)
    face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

    # Loop through each face found in the unknown image
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.55)

        name = "Unknown"

        # use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        text_height = 1
        font = cv2.FONT_HERSHEY_PLAIN
        color_rect = (0, 255, 0)
        color_font = (0, 0, 0)

        if name == "Unknown":
            # color in GBR
            color_rect = (255, 0, 0)
            color_font = (255, 255, 255)

        # draw rectangle over face (color in GBR)
        cv2.rectangle(unknown_image, (left, top), (right, bottom), color_rect, 1)

        # draw rectangle to put name
        cv2.rectangle(unknown_image, (left, int(bottom - text_height - 12)), (right, bottom), color_rect, -1)

        # put recognized image name  over face (color in GBR)
        cv2.putText(unknown_image, name, (left + 5, bottom - 2), font, text_height, color_font)

        # put distance over image (color in  GBR)
        cv2.putText(unknown_image, "distance {:.2}".format(face_distances[best_match_index]), (left + 5, top - 5),
                    font, text_height, (0, 255, 255))

    # display output (convert RGB to GBR)
    # cv2.imshow("Face Recognized", cv2.cvtColor(unknown_image, cv2.COLOR_RGB2BGR))
    # press any key to close window
    # cv2.waitKey()

    # save image with recognize name
    cv2.imwrite(path_out_images + current_file_name, cv2.cvtColor(unknown_image, cv2.COLOR_RGB2BGR))

# release resources
cv2.destroyAllWindows()
