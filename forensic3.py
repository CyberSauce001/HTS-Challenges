with open("/root/Desktop/flashdrive/shh.jpg", "rb") as f:
    r = f.read()

# Global variables
file_list = ["rar", "jpg"]
header_array = []
trailer_array = []
start = 0
file_number = 0

# Iterate through the jpg and rar files
for fi in range(start, len(file_list)):

    if file_list[fi] == "jpg":
        header_array = [255, 216, 255, 224]
        trailer_array = [255, 217]
    else:
        header_array = [82, 97, 114, 33]
        trailer_array = [0, 64, 7, 0]

    # Search and save the header bytes from the indexes above
    key_list = []
    for i in range(start, len(r)):
        try:
            if (r[i + 1] == header_array[1] and 
                r[i + 2] == header_array[2] and 
                r[i + 3] == header_array[3]):
                key_list.append(i)
        except IndexError:
            pass

    # Now search and save the trailer bytes
    for j in range(start, len(key_list)):
        byte_list = []
        for i in range(key_list[j], len(r)):
            byte_list.append(r[i])
            try:
                if i > 0:
                    if file_list[fi] == "jpg":
                        if (r[i - 1] == trailer_array[0] and 
                            r[i] == trailer_array[1]):
                            break
                    else:
                        if (r[i - 3] == trailer_array[0] and 
                            r[i - 2] == trailer_array[1] and 
                            r[i - 1] == trailer_array[2] and 
                            r[i] == trailer_array[3]):
                            break
            except IndexError:
                pass

        # Error correction for the first byte
        byte_list[0] = header_array[0]

       # save the result
        output_path = f"/root/Desktop/out/{file_number}.{file_list[fi]}"
        with open(output_path, "wb") as file:
            file.write(bytearray(byte_list))
        
        file_number += 1
