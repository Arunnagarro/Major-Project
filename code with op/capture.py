import cv2
import face_recognition
import datetime as dt
import log
import os




def capturephoto(user):
	global original_frame
	parent="images/"
	dir=user
	filename=user+".jpg"
	path=os.path.join(parent,dir)
	cam = cv2.VideoCapture(0)
	captured=False
	exit=False

	while True:
		ret, frame = cam.read()
		frame=cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

		if not ret:
			break

		face_locations = face_recognition.face_locations(frame)
		original_frame=frame
		for a,b,c,d in face_locations:
			
			#cv2.rectangle(frame,(d,a),(b,c),(255,0,255),3)
			#cv2.putText(frame,f'{User}',(b-100,c+50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)
			face_encodings = face_recognition.face_encodings(frame,face_locations)
			

		frame=cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
		original_frame=cv2.cvtColor(original_frame, cv2.COLOR_RGB2BGR)
		
		
		
		cv2.imshow("Capturing Image",frame)
		face_loc_length=0	
		k = cv2.waitKey(1)
		if k%256 == 27:
			#log_data="escape hit image not captured closing file . \n"
			#log_data+="---------------------------------------------------------------------------------------------------------------\n\n\n\n"
			#log.write_file(File,log_data)
			#log.close_file(File)
			print("Escape hit, closing...")
			cam.release()
			cv2.destroyAllWindows()
			exit=True
			break
		elif k%256 == 32:
			t=dt.datetime.now()
			face_loc_length=len(face_locations)
			exit=False	
			print("Image Captured at ",f'{t}')
			#log_data="Image captured at "+ f'{dt.datetime.now().time()}' + ".\n "
			#log.write_file(file,log_data)
			#if not file.closed():
			#	log.close(file)
			
			if not os.path.exists(path):
				os.mkdir(path)
			os.chdir(path)

			cv2.imwrite(filename,original_frame)
			os.chdir("..")
			cam.release()
			cv2.destroyAllWindows()
			break
	cam.release()
	cv2.destroyAllWindows()

	if face_loc_length==1:
		return face_encodings
	elif exit==True :
		print("closing .........")
	else:
		print("face not identified try in bright place..... or sit properly .")
		cam.release()
		cv2.destroyAllWindows()
		if exit==False:
			capturephoto(user)



	



