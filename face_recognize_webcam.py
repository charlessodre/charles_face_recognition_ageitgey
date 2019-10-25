import face_recognition
import numpy as np
import helper
import cv2
import os

path_out_images = 'source_img/output/'
path_known_images = 'source_img/known_people/'
path_unknow_images = 'source_img/unknown/'
image_extension = "*.jpeg"


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


list_known_images = helper.get_files_dir(path_known_images, image_extension)

known_face_encodings, known_face_names = get_list_face_encodings_and_names(list_known_images)

# open webcam
video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    print("Could not open webcam!")
    exit()

face_names = []
process_this_frame = True

while True:

    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.55)
            name = "Unknown"

            # use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        text_height = 1
        font = cv2.FONT_HERSHEY_PLAIN
        color_rect = (0, 255, 0)
        color_font = (0, 0, 0)

        if name == "Unknown":
            # color in GBR
            color_rect = (0, 0, 255)
            color_font = (255, 255, 255)

        # draw rectangle over face (color in GBR)
        cv2.rectangle(frame, (left, top), (right, bottom), color_rect, 1)

        # draw rectangle to put name
        cv2.rectangle(frame, (left, int(bottom - text_height - 12)), (right, bottom), color_rect, -1)

        # put recognized image name  over face (color in GBR)
        cv2.putText(frame, name, (left + 5, bottom - 2), font, text_height, color_font)

        # put distance over image (color in  GBR)
        cv2.putText(frame, "distance {:.2}".format(face_distances[best_match_index]), (left + 5, top - 5),
                    font, text_height, (0, 255, 255))

        # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
