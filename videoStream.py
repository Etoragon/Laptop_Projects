import cv2

# Replace '<raspberry_pi_ip_address>' with the actual IP address of your Raspberry Pi
stream_url = 'dummy url'

# Open the video stream
cap = cv2.VideoCapture(stream_url)

# Check if the video stream is opened successfully
if not cap.isOpened():
    print('Failed to open video stream')
    exit(1)

# Read and display the video frames until the user presses 'q'
while True:
    ret, frame = cap.read()
    if not ret:
        print('Failed to read frame from video stream')
        break

    # Display the frame in a window called 'Live Stream'
    cv2.imshow('Live Stream', frame)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video stream and close the window
cap.release()
cv2.destroyAllWindows()
