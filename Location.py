def reverse_array(array):
    for i in range(len(array)):
        if (i % 2) == 0:
            # the index of the array is odd
            pass
        else:
            # reverse the array with even index
            array[i].reverse()
    return array


def array_match(base, change):
    """
    :param base: base array that has a specific column length
    :param change: array that changes column length to match base array
    :return: new changed array that has same column length as base array
    """
    for i in range(len(base)):
        base_len = len(base[i])
        change_len = len(change[i])
        if base_len == change_len:
            pass
        else:
            minimum = min(base_len, change_len)
            if minimum == base_len:
                change[i] = change[i][:minimum]
            else:
                base[i] = base[i][:minimum]

    return base, change


def array_manage(baseDistance, newDistance):
    """
    :param baseDistance: list of old distance
    :param newDistance: list of new distance
    :return: list of people data
    """
    peopledata = list()

    for ls in range(len(baseDistance)):
        tem = []
        for element in range(len(baseDistance[ls])):
            # the value of new distance must be small than the vector space distance.
            difference = baseDistance[ls][element] - newDistance[ls][element]
            if difference > 5:
                tem.append(1)
            else:
                tem.append(0)
        peopledata.append(tem)
    return peopledata


def make_2D(peopleData, newDistance):
    """
    :param peopleData: list of locations where people area
    :param newDistance: list of new distances
    :return: a tuple that contains (x,y) --> will be plotted on GUI
    """
    import math
    tilt_angles = [20, 40, 60, 80, 20, 40, 60, 80]
    rotate_angles = []
    projected = []
    points = []
    x_var = []
    y_var = []
    for elements in range(0, 180, 3):
        rotate_angles.append(elements)
    for i in range(len(baseDistance)):
        data = peopleData[i]
        if data == 0:
            pass
        else:  # data == 1
            temp = []
            for distance in newDistance[i]:
                z = distance * math.cos(math.radians(tilt_angles[i]))
                temp.append(z)
            projected.append(temp)

    for r in range(len(rotate_angles)):
        for d in range(len(projected)):
            x = projected[d][r] * math.sin(math.radians(rotate_angles[r]))
            y = projected[d][r] * math.cos(math.radians(rotate_angles[r]))
            x_var.append(x)
            y_var.append(y)

    return x_var, y_var


if __name__ == '__main__':
    # creating an array
    # there must be 8 sub-arrays in one array

    from random import randint
    baseDistance = []
    detected = []
    for i in range(8):
        temp_b = []
        temp_dec = []
        var = 10
        for j in range(60):
            temp_b.append(var)
            temp_dec.append(randint(0,var))
        var += 10
        baseDistance.append(temp_b)
        detected.append(temp_dec)

    print("length of base " + str(len(baseDistance)))
    print(len(baseDistance[0]))
    print(baseDistance)

    print("length of detected " + str(len(detected)))
    print(len(detected[0]))
    print(detected)

    """
    baseDistance = [[10, 10, 10, 10, 10, 10, 10, 10], [20, 20, 20, 20, 20, 20, 20, 20],
                    [30, 30, 30, 30, 30, 30, 30, 30], [40, 40, 40, 40, 40, 40, 40, 40],
                    [40, 40, 40, 40, 40, 40, 40, 40], [40, 40, 40, 40, 40, 40, 40, 40],
                    [40, 40, 40, 40, 40, 40, 40, 40], [40, 40, 40, 40, 40, 40, 40, 40]]  # The original box detection
    detected = [[1, 1, 5, 7, 3, 10, 3, 4, 6, 8], [20, 20, 20, 18, 10, 5, 2], [5, 2, 4, 7, 30], [12, 40, 40],
                [20, 20, 20, 18, 10, 5, 2], [20, 20, 20, 18, 10, 5, 2], [20, 20, 20, 18, 10, 5, 2],
                [20, 20, 20, 18, 10, 5, 2]]  # The detected distance
    """
    newDistance = reverse_array(detected)
    print("===reverse even array to match arduino program===")
    print(newDistance)
    aftermatch = array_match(baseDistance, newDistance)
    newb = aftermatch[0]
    newd = aftermatch[1]
    print("===after array match===")
    print(newb)
    print(newd)
    print("===finding whether there is a change in distance===")
    peopleData = array_manage(newb, newd)
    print(peopleData)
    print("===creating a 2d graph===")
    data_transmit = make_2D(peopleData, newd)
    print(data_transmit)

    x_var = data_transmit[0]
    y_var = data_transmit[1]

    print("===Plotting the points===")
    import matplotlib.pyplot as plt
    plt.scatter(x_var,y_var)
    plt.show()