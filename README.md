
## Bulk Update EXIF Data in Image Files

This Python script allows you to update the EXIF (Exchangeable Image File Format) data in a batch of image files. It uses the piexif library to modify the date and time information in the EXIF metadata of the specified image files. In this script, the date and time are set to November 6, 2021, at midnight (00:00:00).


## Installation


```bash
  pip install -r requirements.txt
```

## Usage/Examples

- Ensure that your image files are in the same directory as this script or specify the correct file path in the filename variable.

- Run the script, and it will loop through a range of image files (from 93 to 99 in this case) and update the EXIF data in each image file to the specified date and time.

- The updated image files will have their EXIF data modified, and the script will print the file names as they are processed.

**Note:** Make sure to change the date and time values in the new_date variable to match your desired date and time.


## Caution

Modifying EXIF data can impact how your images are organized and sorted. Be sure to back up your image files before running this script, especially if you plan to modify a large number of images.
