import os

i = 0
j = 0
def rn_input(folder, model_name, input_folder=None):
	global i
	folder = folder.encode('string-escape')
    if input_folder is None:
	   input_folder = os.path.join(folder, r"INPUT")
	for f_ in os.listdir(input_folder):
		file_type = r"." + f_.split(".")[-1]
		print f_, model_name+file_type
		try:
			os.rename(os.path.join(input_folder, f_), os.path.join(input_folder, model_name+file_type))
		except WindowsError:
			i += 1
			os.rename(os.path.join(input_folder, f_), os.path.join(input_folder, model_name+str(i)+file_type))

def rn_output(folder, model_name, output_folder=None):
	global j
	folder = folder.encode('string-escape')
    if output_folder is None:
	   output_folder = os.path.join(folder, r"OUTPUT")
	for f_ in os.listdir(output_folder):
		file_type = r"." + f_.split(".")[-1]
		print f_, model_name+file_type
		try:
			os.rename(os.path.join(output_folder, f_), os.path.join(output_folder, model_name+file_type))
		except:
			j += 1
			os.rename(os.path.join(output_folder, f_), os.path.join(output_folder, model_name+str(j)+file_type))

def rn_io(folder, model_name):
	rn_input(folder, model_name)
	rn_output(folder, model_name)
	return 2

def rn_all(folder):
	folder = folder.encode('string-escape')
	for sub in os.listdir(folder):
		rn_io(os.path.join(folder, sub), sub)

def is_img(file_):
	if file_.split('.')[-1] == "img":
		return True
	return False
