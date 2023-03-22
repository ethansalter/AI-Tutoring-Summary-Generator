# Tutoring Summary Generator
This program generates a tutoring summary for a student based on the input provided by the tutor. The program runs a GUI that has input boxes for the student’s name, the length of the session, their mastery of the content, and the tutor’s recommendations for the student. The program automatically generates a prompt from the responses and inputs the prompt into chat GPT to automatically generate a tutoring summary. This prompt can be manually edited in a text box within the GPT. It then automatically sends this summary to the specified email address on file once the user presses the "upload" button.

![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](/GUI_screenshot.png)

## Getting Started
To get started with this program, you will need to have Python 3 installed on your computer. You can download Python 3 from the official website: https://www.python.org/downloads/

You will also need to install the following Python packages:

tkinter
openai
smtplib
You can install these packages using pip:

pip install tkinter openai smtplib
Usage
To use this program, simply run the tutoring_summary_generator.py file. This will open the GUI, where you can enter the student’s name, the length of the session, their mastery of the content, and the tutor’s recommendations for the student.

Once you have entered all the information, click the “Generate Summary” button. The program will automatically generate a tutoring summary using chat GPT and present it into the textbox on the bottom of the GUI. The user can then press the "Upload" button to send it to the specified email address on file.

## Chat GPT
Chat GPT is an artificial intelligence language model developed by OpenAI. It is used in this program to generate the tutoring summary based on the input provided by the tutor. You will need to have an OpenAI API key to use this feature. You can sign up for an API key on the OpenAI website: https://beta.openai.com/signup/

## Specifying the Email Address
To specify the email address that the tutoring summary should be sent to, you will need to edit the students.json file. Look for the following line of code:

"email": "example@example.com",
Replace example@example.com with the email address that you want to send the tutoring summary to.

## Compatibility
This program should work on any operating system that supports Python 3. It has been tested on Windows, macOS, and Linux.

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request. You can also open an issue if you find any bugs or have any suggestions for improvement.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
