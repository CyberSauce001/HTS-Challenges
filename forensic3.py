# Open and read the binary data of the image file
#replace file_path with the path to your shh.jpg
file_path = ""
with open(file_path, "rb") as file:
    data = file.read()

# Global variables
file_types = {
    "jpg": {
        "header": bytearray([255, 216, 255, 224]),
        "trailer": bytearray([255, 217])
    },
    "rar": {
        "header": bytearray([82, 97, 114, 33]),
        "trailer": bytearray([0, 64, 7, 0])
    }
}
file_number = 0

# Iterate through rar and jpg
for file_type in file_types:
    header = file_types[file_type]["header"]
    trailer = file_types[file_type]["trailer"]

    key_positions = []
    i = 0

    # Search for headers
    while i < len(data) - len(header) + 1:
        if data[i:i+len(header)] == header:
            key_positions.append(i)
            i += len(header)  # Move past the header
        else:
            i += 1

    # Extract files based on found headers
    for start_pos in key_positions:
        end_pos = start_pos + len(header)
        j = end_pos

        # Search for trailers
        while j < len(data) - len(trailer) + 1:
            if data[j:j+len(trailer)] == trailer:
                byte_list = data[start_pos:j+len(trailer)]
                break
            j += 1

        # Write extracted file
      #replace output_file_path to where you want it
        output_file_path = f"/root/Desktop/temp/{file_number}.{file_type}"
        with open(output_file_path, "wb") as output_file:
            output_file.write(byte_list)

        file_number += 1
