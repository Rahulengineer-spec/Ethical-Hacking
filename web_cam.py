import cv2

def main():
    # Open the default webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Read the current frame from the webcam
        ret, frame = cap.read()

        # Display the frame in a window called "Webcam"
        cv2.imshow('Webcam', frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
