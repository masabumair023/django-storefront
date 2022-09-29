from django.core.exceptions import ValidationError

def validate_image_size(image):
    max_image_size_kb = 1000

    if image.size > max_image_size_kb *1024:
        raise ValidationError(f'Images cannot be larger than {max_image_size_kb} KBs')