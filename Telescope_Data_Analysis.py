# Script Name       :
# Author            :
# Last Modified     :
# Version           :
#
# Modifications     :
#
# Description       :


from Telescope.Telescope_Function_Library import frb_name, frb_data_numbers, data_split, convert_decimal
from Telescope.Telescope_Function_Library import elevation_calculation


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

        with open('FRBS_Finished_Calculation.dat', 'w') as f:
            f.write("FRB Name \t \t Elevation \t \t \t Azimuth \n")
            f.write(name_of_frb + "\t" + elevation_string + "\t" + azimuth_string)
            print("Calculation finished. Data output to file: FRBS_Finished_Calculation.dat")

    except Exception as err:
        print("An Error has occurred: Could not output file. " + str(err))

    input('Press ENTER twice to quit.')
    input()

if __name__ == '__main__':
    main()
