import colorgram

color_pallet = []
colors = colorgram.extract("image.jpg", 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_pallet = (r,g,b)
    color_pallet.append(new_pallet)
