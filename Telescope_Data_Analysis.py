# Script Name       : Telescope_Data_Analysis.py
# Author            : Shivakumar Mahakali, Devin Williams
# Last Modified     : 7/19/2017
# Version           : 2.00
#
# Modifications     : Added logging infrastructure.
#
# Description       : Main script that reads data from a given .dat file. Calculates the highest elevation, and outputs
#                     a logging file "FRBS_Calculations.log" with the FRB Name, object's Elevation, and object's Azimuth
#                     along with the time of calculation. Any errors are logged to "Error_Logs.log".


from Telescope.Telescope_Function_Library import frb_name, frb_data_numbers, data_split, convert_decimal
from Telescope.Telescope_Function_Library import elevation_calculation, setup_loggers


def main():

    data_list = []
    frb_name_list = []
    elevation_list = []
    azimuth_list = []

    data_file = input('Enter the full data file name...')

    with open(data_file, 'r') as FRBS_data:
        for line in FRBS_data:
            data_list.append(line)

        for i in range(1, len(data_list)):
            data_line = data_list[i]
            name_of_object = frb_name(str(data_line))
            frb_name_list.append(name_of_object)

            data_values = frb_data_numbers(str(data_line))
            data_in_degrees = data_split(data_values)

            hour_angle = convert_decimal(data_in_degrees)
            elevation_num, azimuth_num = elevation_calculation(data_in_degrees, hour_angle)
            elevation_list.append(elevation_num)
            azimuth_list.append(azimuth_num)

    max_elevation_index = max(range(len(elevation_list)), key=elevation_list.__getitem__)

    name_of_frb = frb_name_list[max_elevation_index]
    max_elevation = elevation_list[max_elevation_index]
    max_azimuth = azimuth_list[max_elevation_index]

    elevation_string = str(max_elevation)
    azimuth_string = str(max_azimuth)

    try:
        normal_logger = setup_loggers('normal_logger', 'FRBS_Calculations.log')
        normal_logger.info('\n' + 'Data is calculated from: ' + data_file + '\n' 'FRB Name: \t' + name_of_frb +
                           '\n' 'Elevation:\t' + elevation_string + '\n' 'Azimuth:\t' + azimuth_string + '\n')

    except Exception as err:
        error_logger = setup_loggers('error_logger', 'Error_Logs.log')
        error_logger.exception("An Error has occurred: Could not output file. \n" + str(err))

    input('Press ENTER twice to quit.')
    input()

if __name__ == '__main__':
    main()
