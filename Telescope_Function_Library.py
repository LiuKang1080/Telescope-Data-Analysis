import math
import re
import datetime


def frb_name(line):
    """
    Function that has the FRB Name RegEx.
    :param: line: line parameter from for loop that is read from FRBS.dat file.
    :return: obj_name: Returns the FRB / Object's name.
    """
    frb_regex = re.compile(r'FRB\d{6}')
    match_object = frb_regex.search(line)
    obj_name = match_object.group()
    return obj_name


def frb_data_numbers(line):
    """
    Searches the inputs for the RA and DEC RegEx.
    :param: line: line parameter from for loop that is read from FRBS.dat file.
    :return: Returns a Tuple containing both RA and DEC that is found by the RegEx.
    """
    radec_regex = re.compile(r'''(
        (-)?\d{2}:\d{2}:\d{2}
        )''', re.VERBOSE)

    match_object = radec_regex.findall(line)

    try:
        raj_total = match_object[0]
    except Exception as err:
        print('An Exception has occurred' + str(err))
        print('Please check to see if Data in .dat file is formatted properly:')
        print('Each line should be in the format [ FRBName XX:YY:ZZ (-)XX:YY:ZZ ]')
        print('---')
    try:
        dej_total = match_object[1]
    except Exception as err:
        print('An Exception has occurred' + str(err))
        print('Please check to see if Data in .dat file is formatted properly.')
        print('Each line should be in the format [ FRBName XX:YY:ZZ (-)XX:YY:ZZ ]')
        print('---')

    ra_data = raj_total[0]
    dec_data = dej_total[0]
    return ra_data, dec_data


def data_split(tuple_data):
    """
    Takes the Tuple from frb_data_number and calculates the RA(H,M,S) and Dec(H,M,S) in degrees.
    :param: tuple_data: Tuple containing both RAJ and DECJ.
    :return: ra, de: Right Ascension and Declination in degrees, return as a Tuple.
    """
    ra_final_list = []
    dec_final_list = []

    ra = tuple_data[0]
    ra_list = ra.split(':')
    for ra_data in ra_list:
        try:
            ra_final_list.append(int(ra_data))
        except Exception as err:
            print("An Error has occurred, the string could not be converted to an integer:" + str(err))
    rah, ram, ras = ra_final_list

    dec = tuple_data[1]
    dec_list = dec.split(':')
    for dec_data in dec_list:
        try:
            dec_final_list.append(int(dec_data))
        except Exception as err:
            print("An Error has occurred, the string could not be converted to an integer:" + str(err))
    dech, decm, decs = dec_final_list

    ra = (rah + (ram / 60.0) + (ras/3600.0)) * (360.0 / 24.0)
    de = (dech + (decm / 60.0) + (decs/3600.0)) * (360.0 / 24.0)
    return ra, de


def convert_decimal(ra_data):
    """
    Converts the current minute into decimal value.
    :param: First index of the Tuple that is returned from data_split (Right Ascension).
    :return: hour_angle.
    """
    dt = datetime.datetime.now()
    dth, dtm, dts = dt.hour, dt.minute, dt.second
    decimal = dtm / 60
    decimal_sec = dts / 3600
    lst = dth + decimal + decimal_sec
    lstd = (lst * 360) / 24
    hour_angle = ra_data[0] - lstd
    return hour_angle


def elevation_calculation(declination_in_degrees, full_hour_angle):
    """
    Calculate Elevation and Azimuth
    :param: declination_in_degrees: (de) second index in Tuple from data_split
    :param: full_hour_angle: hour_angle variable from convert_decimal
    :return: elevation and azimuth are returned as Tuple.
    """
    # Latitude at GreenBank Telescope = 38.5

    de = declination_in_degrees[1]
    hour_angle = full_hour_angle

    elevation = (math.asin(math.sin(de * (math.pi / 180)) * math.sin(38.5 * (math.pi / 180)) + math.cos(de * (math.pi / 180)) * math.cos(38.5 * (math.pi / 180)) * math.cos(hour_angle * (math.pi / 180)))) * (180 / math.pi)

    azimuth = (math.asin(((-1) * math.sin(hour_angle * (math.pi / 180)) * math.cos(de * (math.pi / 180))) / (math.cos(elevation * (math.pi / 180))))) * (180 / math.pi)

    return elevation, azimuth
