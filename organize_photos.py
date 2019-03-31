import os, time
import shutil


def file_creation_date(path_to_file):
	return os.path.getctime(path_to_file)


def move_file(photo_path):
	chunk = ['D:/PHOTOS']+list(time.localtime(file_creation_date(photo_path))[:-7])+[os.path.basename(photo_path)]
	chunk = list(map(str, chunk))
	separator = '/'
	print(separator.join(chunk))
	os.makedirs(os.path.dirname(separator.join(chunk)))
	shutil.move(photo_path, separator.join(chunk))
	return 0


def move_files(photo_list):
	# cas unitaire : plus de photos à ranger
	if len(photo_list) == 0:
		return 0

	# cas standard, il y  au moins un fichier à ranger
	else:
		# ranger le premier fichier de la liste
		move_file(photo_list.pop(0))
		# appeler la fonction avec un item de mois
		move_files(photo_list)


	return 0


# Liste des photos dans le répertoire
# move_file(os.listdir('C:\\Users\\Alexis BOURDEAU\\Pictures\\iCloud Photos\\Downloads'))


move_file('C:/Users/Alexis BOURDEAU/Pictures/iCloud Photos/Downloads/_talkv_wmHDzcf4pz_KBxTDva2J4uxtdvJ2OSttK_talkv_high.mp4')
