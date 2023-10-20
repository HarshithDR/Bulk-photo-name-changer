from datetime import datetime
import piexif



if __name__ == '__main__':
    for x in range(93,100):
        filename = 'path'+str(x)+'.JPG'
        exif_dict = piexif.load(filename)
        new_date = datetime(2021, 11, 6, 00, 00, 00).strftime("%Y:%m:%d %H:%M:%S")
        exif_dict['0th'][piexif.ImageIFD.DateTime] = new_date
        exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_date
        exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = new_date
        exif_bytes = piexif.dump(exif_dict)
        piexif.insert(exif_bytes, filename)
        print(filename)
