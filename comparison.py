from PIL import Image, ImageChops, ImageStat

def compare_images(path_a, path_b):
    a = Image.open(path_a).convert("RGB").resize((256, 256))
    b = Image.open(path_b).convert("RGB").resize((256, 256))
    diff = ImageChops.difference(a, b)
    score = sum(ImageStat.Stat(diff).mean) / 3
    return (f"Average pixel difference: {score:.1f}/255. This is sensitive to lighting, framing, "
            "and camera changes; it is not a measure of skin improvement or worsening.")
