from flask import Flask,render_template,request
from PIL import Image
from tensorflow.keras.preprocessing.image import load_img,img_to_array,array_to_img
from tensorflow.keras.models import load_model,Model,load_model
import numpy as np
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity,cosine_distances
app = Flask(__name__)




image_vector = pickle.load(open(r'C:/Users/Lenovo/Desktop/imagesearch/app_Building/metadata.pkl','rb'))
#model = load_model(r'E:/Medium/image_autoencoder_2.h5')
latent_model = load_model(r'C:/Users/Lenovo/Desktop/imagesearch/app_Building/latent_model.h5')

def image_vector_generator(img):
	img2 = np.expand_dims(img,axis=0)
	img2 = img2/255.0
	latent_vector = latent_model(img2)
	return latent_vector




@app.route('/',methods=['POST','GET'])
def home():

	if request.method == 'POST':
		#img_vector = image_vector_generator(image)
		u_img = request.files['image']
		img = Image.open(u_img.stream)
		img = img.resize((224,224))
		img.save('./uploads/'+u_img.filename)
		vector= image_vector_generator(img)
		print(vector)

		v = []
		for i in range(len(image_vector['image_vector'])):
		  sim = cosine_similarity(X=image_vector['image_vector'][i],Y=vector)
		  v.append(sim)
		arr = np.array(v)
		arr2 = np.reshape(arr,-1)
		arr2 = arr2[50:]
		DataFrame = pd.DataFrame(image_vector['img_url'])
		DataFrame['similarity'] = arr2
		df = DataFrame.sort_values(by='similarity',ascending=False)
		df = df.head(10)
		index = df.index
		l = index[0]
		print(df['image_url'][l])
		img_name = []
		score = []
		for i in index :
			img1 = df['image_url'][i]
			img_name.append(img1)
			sc = df['similarity'][i]
			score.append(sc)
		data = {'image_name':img_name,'scores':score}
		print(data['scores'])
		return render_template('index.html',data=data)
	else:

		return render_template('index.html')



if __name__ == '__main__':
	app.run(debug=True)