def calculate_image_memory(num_images, width, height, color_depth):
    bits_per_image = width * height * color_depth

    bytes_per_image = bits_per_image / 8

    total_bytes = bytes_per_image * num_images

    total_mib = total_bytes / (1024 * 1024)

    return total_mib