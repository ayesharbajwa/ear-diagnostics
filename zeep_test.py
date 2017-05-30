import zeep
import base64
import uuid
### zeep documentation at http://docs.python-zeep.org/en/master/index.html ###

# SET UP CONNECTION TO XENPLATE
wsdl = 'https://dev.l2s2.com/XenplateIFWebservice/XenplateIFWebservice.svc?wsdl'
client = zeep.Client(wsdl=wsdl)

### Users (system user/admin), Records (patient), Plate (individual checkups) ###
### https://dev.l2s2.com/XenplateIFWebservice/XenplateIFWebservice.svc ###

# user global var - USER/ADMIN - GET FROM USER INPUT
user = uuid.UUID((input("What is the userID? Enter with single quotes: ")))

# l2s2_file global var - GET FROM USER INPUT
l2s2_name = input("What is the L2S2 database filename? Enter as a string: ")

# random image file for testing
smiley = "l2s2_smiley.jpg"


# service is a ServiceProxy object.  It will check if there
# is an operation with the name `X` defined in the binding
# and if that is the case it will return an OperationProxy


def printUserShowAll(userID):
	""" Function wrapper for API call to UserShowAll """
	print(client.service.UserShowAll(userID))
	return

def printRecordShowAll(userID):
	""" Function wrapper for API call to RecordShowAll """
	print(client.service.RecordShowAll(userID))  # without index
	return

def downloadUserProfileImage(userID):
	""" Function wrapper for API call to download/save user profile photo as .jpg """
	# gives type UserProfileImageDownloadResult, take int64 encoding
	result = client.service.UserProfileImageDownload(userID);
	print result
	img64 = result.File.Data

	img_64_decode = base64.decodestring(img64)
	# create writable image in current directory and write decoding result
	image_result = open(result.File.FileName + '.jpg', 'wb') 
	# write data to image file
	image_result.write(img_64_decode)
	# produces L2S2 profile photo
	return

def uploadFile(filename):
	""" Function wrapper for API call to upload an image file """
	file_data_structure = client.get_element('ns2:XenplateAttachment');
	f = file_data_structure(ContentTransferEncoding= 'base64',
	                     ContentType = 'image/jpeg',
	                     Data= encodeImageAsInt64(filename),
	                     FileName= filename,
	                     OriginalFileName= filename)
	FileUploadResult = client.service.FileUpload(f)
	print(FileUploadResult)
	print(FileUploadResult.FileName)
	return

def downloadFile(l2s2_filename):
	""" Function wrapper for API call to download an image file. """
	FileDownloadResult = client.service.FileDownload(l2s2_filename)
	img64 = FileDownloadResult.File.Data
	img_64_decode = base64.decodestring(img64)
	# create writable image in current directory and write decoding result
	image_result = open(FileDownloadResult.File.FileName + '-1.jpg', 'wb') 
	# write data to image file
	image_result.write(img_64_decode)

def encodeImageAsInt64(local_filename):
	img = open(local_filename, 'rb') #open file in read mode
	img_read = img.read()
	image_64_encode = base64.encodestring(img_read)
	return image_64_encode

def main():
	downloadUserProfileImage(user)
	downloadFile(l2s2_name)


if __name__ == "__main__":
	main()
