
# Table-scan :Noble tool to detect and extract tables from images.

The computer vision community has witnessed the significant success of table detection techniques over the last decade. However, converting the detected tables into digital format is still a challenge. So in this repo, Ashish Aman (M22MA002) and Bhawna Bhoria (M22MA003) have studied the techniques of performing table detection with the help of deep learning concepts. This purpose is implemented using both inbuilt functions and defining models from scratch. Further, comparisons are done in between various techniques. Hence, this idea will have great practical applications in the documentation domain where the artifacts and physical documentation can be transformed into digital format.
Table detection from an image can be achieved using Optical Character Recognition (OCR) techniques combined with image processing techniques. Here is an overview of the steps involved in detecting tables from an image:
Preprocessing the image, detecting contours like horizontal and vertical lines, identifying table regions, extracting text with optical character recognition, and finally post-processing the results to format the data into a table are all necessary phases in the process of table detection from an image. Python offers a number of libraries and tools, including OpenCV, Scikit-Image, and EasyOCR, that can be used to detect tables in images. The level of precision and performance required, as well as the image's complexity and quality, will determine the method and approaches employed. Data input, invoice processing, and document scanning are just a few of the many uses for automated table detection from photos.Next we have trained our custom dataset on different versions of YOLO V5 and V8 to detect the table and done their comparisons. After that our first method is implemented to extract data from the table detected in it. Time is saved and accuracy is increased in data extraction and analysis when images of tables are processed in this way.


DATASET (ANNOTATED TABLES):- https://drive.google.com/file/d/1LkmuDy-QMdginpbi1Y77RArhTU-pW5aR/view?usp=share_link

    For Table extractions:
    Open the Table_Detection.ipynb file in google colab
    install the requirements mentioned in the code
    Upload the sample image or input image attached in the input.
    give the no. of columns as in the figure in the output.
    Run the cell one by one.
    Required datframe and the evaluation metrics of jaccard similarity will be obtained of your desired image.


2.Yolov5

    Move into the file of Yolov5 of github.
    Clone the git file as mentioned in it.
    install the dependencies and requirement.
    Set the directories of the folder as per the instruction-images\train\IMAGE OF TABLES
    images\val\IMAGE OF TABLES
    label\train\txt files of corresponding images
    label\val\txt file of corresponding images
    update the custom_coco.yaml file in the given folders same as the above directories .Look into readme of the YOLOV5 folder.
    Next run the model by using the dataset link provided into it.
    Predict the output of any images by using best.pt in runs\detect\weights\pred and look the training result by file runs\detect\weights\exp
3.YoloV8n

    Open cv_table_yolov8.ipynb file in colab
    install ultralytics and other requirements
    Next train the model by the Train_data.yaml as data file 
    update the Train_data.yaml file in the given folders same as the above directories .Look into readme of the YOLOV5 folder.
    Next run the model by using the dataset link provided into it.
    Predict the output of any images by using best.pt in runs\detect\weights\pred and look the training result by file runs\detect\weights\exp




## Authors

- [@Ashish-aman](https://www.github.com/Ashish-aman)

- [@97shanu](https://www.github.com/@97shanu)


## 🔗 Links

- [@Ashish-aman](https://www.github.com/Ashish-aman)

- [@97shanu](https://www.github.com/@97shanu)
## License

[MIT](https://github.com/ColfaxResearch/YOLO-Object-Detection/blob/master/LICENSE)

MIT License

Copyright (c) 2018 Colfax Research

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
## Documentation

[YOLO](https://docs.ultralytics.com/)

[YOLO](https://learnopencv.com/ultralytics-yolov8/)

[CNN](https://www.analyticsvidhya.com/blog/2019/10/building-image-classification-models-cnn-pytorch/)

[ANNOTATIONS](https://www.makesense.ai/)