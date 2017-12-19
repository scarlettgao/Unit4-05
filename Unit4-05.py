# Created by: Scarlett Gao
# Created on: Nov 2017
# Created for: ICS3U

def volume(radius, height):
    Volume = ((2 * 3.14 * (radius ** 2) * height))
    return Volume
    
height = raw_input('Enter height: ')
height = int(height)
radius = raw_input('Enter radius: ' )
radius = int(radius)

if height < 0 or radius < 0:
    print ('Please input valid number.')
else:
    volume_print = volume(radius, height)
    print('The volume of cylinder is ' + str(volume_print) + ' cm^3')
