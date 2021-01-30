# VaccTracc

To setup and test for yourself (on Windows)

1. Install AWS CLI v2 from here: https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-windows.html
2. Navigate to the .aws folder, found in the user directory ("C:/Users/Aadit O" in my case)
3. Sign in here for your credentials: https://www.awseducate.com/student/s/launch-starter
4. Click "Account Details" and copy everything in the text box titled "AWS CLI"
5. Open the credentials text file in the .aws folder and paste everything (if this doesn't show up, run "aws configure" in your command prompt)
6. Open the config text file and enter the following:
[default]
region = us-east-1
output = json
7. In a command prompt, put in the following:
pip install pyqt5
pip install boto3

8. Once that's done, just run the OCR_GUI.py file
