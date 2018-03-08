# Write a function to find the rectangular intersection of two given love rectangles.

# As with the example above, love rectangles are always "straight" and never "diagonal."
# More rigorously: each side is parallel with either the x-axis or the y-axis.

# They are defined as dictionaries like this:
#   my_rectangle = {

#     # Coordinates of bottom-left corner
#     'left_x'   : 1,
#     'bottom_y' : 1,

#     # Width and height
#     'width'    : 6,
#     'height'   : 3,

# }

def find_line_overlap(x1, x2, y1, y2):
    # find overlapping points in lines defined by endpoints (x1,x2) and (y1,y2)
    # if end points just meet, then it is not considered as overlapping.
    start_point = max(x1, y1)
    end_point = min(x2, y2)
    if start_point >= end_point:
        return False, ()
    else:
        return True, (start_point, end_point)

def find_overlapping_rectangle(rect1, rect2):
    # find overlap on x-axis
    is_x_overlapping, overlapping_x = find_line_overlap(rect1["x"], rect1["x"]+rect1["width"],
                rect2["x"], rect2["x"]+rect2["width"])
    if is_x_overlapping:
        is_y_overlapping, overlapping_y = find_line_overlap(rect1["y"], rect1["y"]+rect1["height"],
                rect2["y"], rect2["y"]+rect2["height"])
    if is_x_overlapping and is_y_overlapping:
        return {
            "x" : overlapping_x[0],
            "y" : overlapping_y[0],
            "width" : overlapping_x[1]-overlapping_x[0],
            "height" : overlapping_y[1]-overlapping_y[0]
        }
    else:
        return {}

r1 = {
    "x" : 2,
    "y" : 5,
    "width": 4,
    "height": 4
}

r2 = {
    "x" : 4,
    "y" : 8,
    "width": 4,
    "height": 4
}

overlapping_rectangle = find_overlapping_rectangle(r1, r2)
if len(overlapping_rectangle) > 0:
    print(overlapping_rectangle)
