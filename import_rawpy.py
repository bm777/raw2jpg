import imageio
import os
import rawpy

def load_images_from_folder(folder):
    return os.listdir(folder)

if __name__ == '__main__':

	folder = "/home/bm7/tagus/drone/files"
	print("Listing RC2 image in the folder...", folder)

	l = load_images_from_folder(folder)
	counter = 0
	for i in l:
		try:
			print("Processing {} ... {}/{}".format(i, counter, len(l)))
			with rawpy.imread("files/"+str(i)) as filename:
				rgb = filename.postprocess()
			imageio.imsave("results/image"+str(counter)+".jpg", rgb)
			
			counter += 1
		except Exception as e:
			raise e
		