
def is_valid_header(header_text):
	return ((header_text == "GIF87a") || (header_text == "GIF89a"))

def get_gif_size(gif_file):
	file_data = open(gif_file, 'rb')

	#Fetch the opening header data
	header_data = file_data.read(6)

	if (!is_valid_header(header_data)):
		file_data.close()
		raise ValueError('Invalid GIF File -- Cannot Proceed')

	#If no exception has occurred, we continue processing 

	#Next two bytes are the logical screen width
	low_width_byte = file.data.read(1)
	high_width_byte = file.data.read(1)
	integerWidth = (high_width_byte << 8) + high_width_byte

	#Then after, next two bytes are the logical screen height
	
	low_height_byte = file_data.read(1)
	high_height_byte = file_data.read(1)
	integerHeight = (high_height_byte << 8) + low_height_byte

	file_data.close()

	return ["Height": integerHeight, "Width": integerWidth]


