import os, time
import shutil
from datetime import datetime, timezone


def file_creation_date(path_to_file):
	return os.path.getctime(path_to_file)


def move_file(photo_path):
	# chunk = ['D:/PHOTOS']+list(time.localtime(file_creation_date(photo_path))[:-7])+[os.path.basename(photo_path)]
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
		return 0

	# cas standard, il y  au moins un fichier à ranger
	else:
		# ranger le premier fichier de la liste
		move_file(photo_list.pop(0))
		# appeler la fonction avec un item de mois
		move_files(photo_list)
	return 0


# Liste des photos dans le répertoire
move_files(list(map(
	lambda x: 'D:/PHOTOS/ATRIER/'+x,
	os.listdir('D:\\PHOTOS\\ATRIER'
))))

#print(datetime.fromtimestamp(os.stat("D:/PHOTOS/ATRIER/2020/_31A5679.JPG").st_mtime).strftime("%Y/%m").split("/"))
#print(time.localtime(file_creation_date("D:/PHOTOS/ATRIER/2020/_31A5679.JPG"))[:-7])
#datetime.fromtimestamp(stat_result.st_mtime, tz=timezone.utc)

# move_file('C:/Users/Alexis BOURDEAU/Pictures/iCloud Photos/Downloads/_talkv_wmHDzcf4pz_KBxTDva2J4uxtdvJ2OSttK_talkv_high.mp4')

