from PIL import Image

def hide_message(image_path, message):
    img = Image.open(image_path)

    binary_message = ''.join(format(ord(i), '08b') for i in message)

    width, height = img.size

    max_message_length = (width * height) // 8

    if len(binary_message) > max_message_length:
        raise ValueError('Message too long to be hidden in the given image')

    new_img = Image.new(img.mode, img.size)

    message_index = 0

    # Loop through each pixel in the image - use nested loop where x represents width & y represents height
            # Get the RGB values of the current pixel, using img.getpixel()
            # unpack the result tuple to red, green & blue


    for x in range(width):
      for y in range(height):
            pixel = img.getpixel((x,y))
            red,green,blue = pixel
            # print(pixel)

            # Check if the message has been fully hidden
            if message_index == len(binary_message):
                new_img.putpixel((x, y), pixel)
                continue

            # Modify the least significant bit of each RGB value with the message bits
            red_binary = format(red, '08b')
            green_binary = format(green, '08b')
            blue_binary = format(blue, '08b')

            #update last value of red_binary and increment message_index (done for you)
            red_binary = red_binary[:-1] + binary_message[message_index]
            message_index += 1

            if message_index == len(binary_message):
                green_binary = green_binary[:-1] + '0'
                blue_binary = blue_binary[:-1] + '0'
            else:
                green_binary = green_binary[:-1] + binary_message[message_index]
                message_index += 1

                if message_index == len(binary_message):
                    blue_binary = blue_binary[:-1] + '0'
                else:
                    blue_binary = blue_binary[:-1] + binary_message[message_index]
                    message_index += 1
            #check if message_index reached it's limit
            #if yes, set '0' as the last value of green and blue binary
            #else, update last value of green_binary and increment message_index

            #check again if message_index reached it's limit
            #if yes, set '0' as the last value of blue binary
            #else, update the last value of blue_binary and increment message_index

            #converting back to binary
            red = int(red_binary, 2)
            green = int(green_binary, 2)
            blue = int(blue_binary, 2)

            # Create a new pixel with the modified RGB values and add it to the new image
            new_pixel = (red, green, blue)
            new_img.putpixel((x, y), new_pixel)
    new_img.save('hidden.png')

def extract_message(image_path):
    # Open the image
    img = Image.open(image_path)

    # Get the size of the image
    width, height = img.size

    binary_message = ''
    # Loop through each pixel in the image
    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            red, green, blue = pixel

            red_binary = format(red, '08b')
            green_binary = format(green, '08b')
            blue_binary = format(blue, '08b')

            # Concatenate the last bit of every red_binary, green_binary & blue_binary to binary_message
            binary_message += red_binary[-1]
            binary_message += green_binary[-1]
            binary_message += blue_binary[-1]

    # Convert the binary message to text
    message = ''
    for i in range(0, len(binary_message), 8):
        message += chr(int(binary_message[i:i+8], 2))

    return message
