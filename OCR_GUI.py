# importing required libraries 
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import os, sys, time
from rekognition import Rekog


class OCRWindow(QMainWindow):
    def __init__(self): 
        super().__init__() 

        self.setGeometry(100, 100, 800, 600) 
        self.setStyleSheet("background : lightgrey;") 

        self.available_cameras = QCameraInfo.availableCameras() 

        if not self.available_cameras: 
            sys.exit() 

        self.status = QStatusBar() 
        self.setStatusBar(self.status) 

        self.save_path = "" 

        self.viewfinder = QCameraViewfinder()
        self.viewfinder.show()
        self.setCentralWidget(self.viewfinder) 

        self.select_camera(0) 

        toolbar = QToolBar("Camera Tool Bar")
        self.addToolBar(toolbar) 

        click_action = QAction("Click photo", self)
        click_action.setStatusTip("This will capture picture")
        click_action.setToolTip("Capture picture")
        click_action.triggered.connect(self.click_photo)
        toolbar.addAction(click_action) 

        change_folder_action = QAction("Change save location", self) 
        change_folder_action.setStatusTip("Change folder where picture will be saved saved.")
        change_folder_action.setToolTip("Change save location")
        change_folder_action.triggered.connect(self.change_folder)
        toolbar.addAction(change_folder_action) 

        toolbar.setStyleSheet("background : white;") 

        self.setWindowTitle("Slip OCR") 

        self.show() 

    # method to select camera 
    def select_camera(self, i): 
        self.camera = QCamera(self.available_cameras[i]) 
        self.camera.setViewfinder(self.viewfinder) 
        self.camera.setCaptureMode(QCamera.CaptureStillImage) 
        self.camera.error.connect(lambda: self.alert(self.camera.errorString()))
        self.camera.start()
        self.capture = QCameraImageCapture(self.camera)
        self.capture.error.connect(lambda error_msg, error, msg: self.alert(msg))
        self.capture.imageSaved.connect(self.get_text)
        self.current_camera_name = self.available_cameras[i].description()
        self.save_seq = 0       

    def click_photo(self):
        self.save_seq += 1
        self.capture.capture(os.path.join(self.save_path, str(self.save_seq)))

    def get_text(self):
        r = Rekog()
        if r.upload_file(str(self.save_seq) + ".jpg" ,"rekog-bucket"):
            print(r.detect_text(str(self.save_seq) + ".jpg" ,"rekog-bucket"))
        else:
            print("fail")

    # change folder method 
    def change_folder(self): 
        path = QFileDialog.getExistingDirectory(self, "Picture Location", "") 
        if path: 
            self.save_path = path 
        self.save_seq = 0

    # method for alerts 
    def alert(self, msg): 
        error = QErrorMessage(self) 
        error.showMessage(msg)


# Driver code 
if __name__ == "__main__" :
    App = QApplication(sys.argv) 
    window = OCRWindow() 
    sys.exit(App.exec()) 
