from Functions import * 

model = load_model('action.h5')


cap = cv2.VideoCapture(0)
# Set mediapipe model 
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    prev_gesture = None
    while cap.isOpened():

        # Read feed
        ret, frame = cap.read()

        # Make detections
        image, results = mediapipe_detection(frame, holistic)
        
        # Draw landmarks
        draw_landmarks(image, results)
        
        # 2. Prediction logic
        keypoints = extract_keypoints(results)
        sequence.append(keypoints)
        sequence = sequence[-30:]
        
        if len(sequence) == 30:
            res = model.predict(np.expand_dims(sequence, axis=0))[0]
            # print(actions[np.argmax(res)])
            # speak(actions[np.argmax(res)])
            current_gesture = actions[np.argmax(res)]

            if current_gesture != prev_gesture:  # Check if the current gesture is different from the previous one
                if prev_gesture is not None:  # Check if this is not the first gesture detected
                    speak(current_gesture)  # Speak the current gesture
                    # print(current_gesture)  # Print the current gesture
                prev_gesture = current_gesture  # Update the previous gesture

            cv2.rectangle(image, (0,0), (640, 40), (245, 117, 16), -1)
            cv2.putText(image, current_gesture, (3,30), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    
# ... (rest of the code remains unchanged)

        # Show to screen
        cv2.imshow('I can Speak', image)

        # Break gracefully
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()