import math

DIRECTION_NORTH_EAST = 'NE'
DIRECTION_NORTH_WEST = 'NW'
DIRECTION_SOUTH_WEST = 'SW'
DIRECTION_SOUTH_EAST = 'SE'


# Euclidean Distance Formula->
# distance = sqrt((x2-x1)*(x2-x1)+(y2-y1)(y2-y1))
def distance_formula(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))


# Implementing A* Algorithm using Euclidean distance
# f=g+h
# g=distance of starting pt to the immediate moving pt
# h=distance of immediate moving pt to destination pt
def calculate_a_star(start_x, start_y, moving_x, moving_y, dest_x, dest_y):
    g = distance_formula(start_x, start_y, moving_x, moving_y)
    h = distance_formula(moving_x, moving_y, dest_x, dest_y)
    return g + h


# checking steps conditions in one direction in one shot
# NE-3,SE-4,NW-5,SW-2
# Since while computing I am staring from 0 steps for each direction
# Making computation is post Increment , greater than is compute on less
def check_steps_in_one_dir(direction, steps):
    if (direction == DIRECTION_NORTH_EAST) & (steps > 2):
        return False
    elif (direction == DIRECTION_SOUTH_EAST) & (steps > 1):
        return False
    elif (direction == DIRECTION_NORTH_WEST) & (steps > 4):
        return False
    elif (direction == DIRECTION_SOUTH_WEST) & (steps > 3):
        return False
    return True


# As per A* Computing probables in given four direction
# Moving to minimum F as per A*
def compute_efficient_path(x, y):
    print('Insect is about to move to destination via efficeint path')
    temp_x = 0
    temp_y = 0
    direction_steps = [0, 0, 0, 0]
    steps = 0
    list_coordinates = list()
    while (temp_x != x) | (temp_y != y):
        print('Insect is moving')
        steps += 1
        list_coordinates.append((temp_x, temp_y))
        f_ryt = calculate_a_star(temp_x, temp_y, temp_x + 1, temp_y + 1, x, y)
        f_left = calculate_a_star(temp_x, temp_y, temp_x - 1, temp_y - 1, x, y)
        f_up = calculate_a_star(temp_x, temp_y, temp_x - 1, temp_y + 1, x, y)
        f_bot = calculate_a_star(temp_x, temp_y, temp_x + 1, temp_y - 1, x, y)
        if not check_steps_in_one_dir(DIRECTION_NORTH_EAST, direction_steps[0]):
            min_f = min([f_left, f_up, f_bot])
        elif not check_steps_in_one_dir(DIRECTION_SOUTH_WEST, direction_steps[1]):
            min_f = min([f_ryt, f_up, f_bot])
        elif not check_steps_in_one_dir(DIRECTION_NORTH_WEST, direction_steps[2]):
            min_f = min([f_ryt, f_left, f_bot])
        elif not check_steps_in_one_dir(DIRECTION_SOUTH_EAST, direction_steps[3]):
            min_f = min([f_ryt, f_left, f_up])
        else:
            min_f = min([f_ryt, f_left, f_up, f_bot])

        if (min_f == f_ryt) & (check_steps_in_one_dir(DIRECTION_NORTH_EAST, direction_steps[0])):
            direction_steps = [direction_steps[0] + 1, 0, 0, 0]
            temp_x = temp_x + 1
            temp_y = temp_y + 1
        elif (min_f == f_left) & (check_steps_in_one_dir(DIRECTION_SOUTH_WEST, direction_steps[1])):
            direction_steps = [0, direction_steps[1] + 1, 0, 0]
            temp_x = temp_x - 1
            temp_y = temp_y - 1
        elif (min_f == f_up) & (check_steps_in_one_dir(DIRECTION_NORTH_WEST, direction_steps[2])):
            direction_steps = [0, 0, direction_steps[2] + 1, 0]
            temp_x = temp_x - 1
            temp_y = temp_y + 1
        elif (min_f == f_bot) & (check_steps_in_one_dir(DIRECTION_SOUTH_EAST, direction_steps[3])):
            direction_steps = [0, 0, 0, direction_steps[3] + 1]
            temp_x = temp_x + 1
            temp_y = temp_y - 1
    list_coordinates.append((temp_x, temp_y))
    print('Hurray Insect reach the destination')
    print('The efficient path insect followed was:')
    print(list_coordinates)


def start_computing(x, y):
    print('starting processing')
    # distance = math.sqrt((x * x) + (y * y))
    # # distance = math.sqrt((x - x)**2 + (y - y)**2)
    if x == 0 and y == 0:
        print('Insect stays at origin')
    # elif x == 0 and y < 0 and distance <= 4:
    #     # SE-4
    #     print('oneshot')
    # elif x == 0 and y > 0 and distance <= 5:
    #     # NW-5
    #     print('oneshot')
    # elif y == 0 and x < 0 and distance <= 2:
    #     # SW-2
    #     print('oneshot')
    # elif y == 0 and x > 0 and distance <= 3:
    #     # NE-3
    #     print('oneshot')
    else:
        compute_efficient_path(x, y)


# def original_coordinates(x, y):
#     print("original")
#

# rotate plane 45 degree counterclockwise
# def updated_coordinates(x, y):
#     # rotation axes by angle a = (x,y)-->(X,Y)
#     # X=xcos(a)+ysin(a)
#     # Y=-xsin(a)+ycos(a)
#     # here a = 45
#     angle = math.radians(45)
#     return (x * math.cos(angle)) + (y * math.sin(angle)), (y * math.cos(angle)) - (x * math.sin(angle))

def check_input(user_response):
    try:
        float(user_response)
        is_dig = True
    except ValueError:
        is_dig = False
    return is_dig


def convert_number(user_response):
    if user_response >= 0:
        return math.ceil(user_response)
    else:
        return math.floor(user_response)


if __name__ == '__main__':
    print('Hello! Lets Help Insect')
    user_response_x = input("Please Enter x coordinate")
    user_response_y = input("Please Enter y coordinate")
    if (check_input(user_response_x)) & (check_input(user_response_y)):
        start_computing(float(user_response_x), float(user_response_y))
    else:
        print("Please Provide Proper Input")
