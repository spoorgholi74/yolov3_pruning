import glob, os
from pathlib import Path

for filename in Path('src').glob('**/*.c'):
    print(filename)

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Directory where the data will reside, relative to 'darknet.exe'
path_data = '/data/custom/'
path_image = 'data/custom/images/'
# Percentage of images to be used for the test set
percentage_test = 10

# Create and/or truncate train.txt and test.txt
file_train = open(current_dir  + path_data + 'train.txt', 'w')
file_test = open(current_dir + path_data + 'test.txt', 'w')

# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
for pathAndFilename in Path(current_dir + '/' + path_image).glob('*.jpg'):
    print(pathAndFilename)
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    print(title, ' + ', ext)
    #file = open(title + '.txt', 'w')
    #file.write('0 0.5 0.5 1 1')
    #file.close()

    if counter == index_test:
        counter = 1
        file_test.write(path_image + title + '.jpg' + "\n")
    else:
        file_train.write(path_image + title + '.jpg' + "\n")
        counter = counter + 1
