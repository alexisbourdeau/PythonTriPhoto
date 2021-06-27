import os, time
import shutil
from datetime import datetime, timezone


def file_creation_date(path_to_file):
	return os.path.getctime(path_to_file)


def move_file(photo_path):
	chunk = ['D:/PHOTOS']+datetime.fromtimestamp(os.stat(photo_path).st_mtime).strftime("%Y/%m").split("/")+[os.path.basename(photo_path)]
	chunk = list(map(str, chunk))
	separator = '/'
	print(separator.join(chunk))
	if not os.path.exists(os.path.dirname(separator.join(chunk))):
		os.makedirs(os.path.dirname(separator.join(chunk)))
	shutil.move(photo_path, separator.join(chunk))
	return 0


def move_files(photo_list):
	# cas unitaire : plus de photos à ranger
	if len(photo_list) == 0:

	# cas standard, il y  au moins un fichier à ranger
	else:
		# ranger le premier fichier de la liste
		move_file(photo_list.pop(0))
		# appeler la fonction avec un item de mois
		move_files(photo_list)


# Liste des photos dans le répertoire
move_files(list(map(
	lambda x: 'D:/PHOTOS/ATRIER/'+x,
	os.listdir('D:\\PHOTOS\\ATRIER'
))))
