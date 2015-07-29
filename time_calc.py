def time(lightyears):
    speed_of_light = 670616629#MPH
    craft_speed = 36373
    speed_ratio = speed_of_light/craft_speed
    hl = (str(speed_ratio * lightyears) * 8765)
    return hl
    
