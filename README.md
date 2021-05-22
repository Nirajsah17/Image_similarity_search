# Image_similarity_search
#### Table of content 
1. Workflow
2. Installation
3. Results

### models file link is below (beacause github not allow for big size )

[Latent Sapce Model file](https://drive.google.com/file/d/1f0861aY4C-Nb10XpXDbsu7re19dRBGyd/view?usp=sharing)

<br><br>
##### 1. Workflow
![](https://github.com/Nirajsah17/Image_similarity_search/blob/main/imagesearch.png)
<br>

##### a. Datasets overviews :
   This is Flipkart product Image Datasets available on kaggle you can download from ![here] (https://www.kaggle.com/PromptCloudHQ/flipkart-products) .
   it contain a lots of table but we only care about the image table where the link of all the available images are given , through we downloads all the images in a folder for images datasets.
##### b. Models training :  
   We are training an <u>Autoencoder</u> Model that will generate lower dimesional representaion of image as models . then we extract lower dimesion representation of all  images and saved it.
##### 2. Installation ( To run this model on your PC ):
Note : This model trained on google colab with tensorflow==2.4.x version <br>
To run this model on your own PC , First of all clone the repository on your PC and put in your project folder . <br>
create a Python Virtual Environment and Install all dependencies that are mentioned in the <u>requirement.txt file<u/> <br>
Now in the virtual environment trace your project directory and Run the Following coommand  > python <u>yourappname.py</u><br>
HUrrraY ,You all set to go goto browser paste running server and port . 
   
### Results :
![Index page](https://github.com/Nirajsah17/Image_similarity_search/blob/main/Screenshot%20(715).png)
<br>
UI for image uploads 
<br><br>
![](https://github.com/Nirajsah17/Image_similarity_search/blob/main/Screenshot%20(714).png)

<br><br>

![](https://github.com/Nirajsah17/Image_similarity_search/blob/main/Screenshot%20(716).png)


###### reference :
   1. https://github.com/luchonaveiro/image-search-engine


