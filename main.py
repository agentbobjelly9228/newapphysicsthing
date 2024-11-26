import cv2

cap = cv2.VideoCapture("onepiece.mp4")
ret, frame = cap.read()
zoom_factor = 1.5
while True:
    ret, frame = cap.read()

    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
    height, width, _ = frame.shape

    # Calculate the cropping box based on the zoom factor
    center_x, center_y = width // 2, height // 2
    new_width, new_height = int(width / zoom_factor), int(height / zoom_factor)

    # Crop the frame to the zoomed-in area
    x1 = max(0, center_x - new_width // 2)
    y1 = max(0, center_y - new_height // 2)
    x2 = min(width, center_x + new_width // 2)
    y2 = min(height, center_y + new_height // 2)

    cropped_frame = frame[y1:y2, x1:x2]

    # Resize the cropped frame to the original size
    frame = cv2.resize(cropped_frame, (width, height))
    cv2.imshow('frame', frame)
