""" Author : Shreyansh Kumar
    Date: 24-July-2018
"""
__about__ = "Data Transformation."

__all__ = ['Transform']


class Transform:

    def __init__(self,input_file=None):
        self.file_path = input_file

    def transform(self):

        """ One hot encoding for engine location """

        engine_loc_transform = {
                                'front': 1,
                                'mid': 2,
                                'back': 3
                                }

        """ Cylinder count transformation """

        cylinders_count = {
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8
        }

        """ Boolean flag for aspiration """

        aspiration_flag = {
            'turbo': 1,
            'std': 0
        }

        transformed_data = []
        with open(self.file_path) as f:

            """ Add headers to a header list. """
            header = ["engine-location",
                      "num-of-cylinders",
                      "engine-size",
                      "weight",
                      "horsepower",
                      "aspiration",
                      "price",
                      "make"]
            transformed_data.append(header)
            """ Skip the header line. """
            next(f)
            for x in f:
                """ Split the data in the line. """
                x = x.split(";")

                """ Check for the bad data present. """
                if '-' in x or ' -' in x or '- ' in x or ' ' in x or None in x:

                    """ Skip the bad data. """
                    pass
                else:
                    try:

                        """ check for the engine location. """
                        loc = x[8]
                        elt = engine_loc_transform[loc]
                        """ Convert cent to euro in float. """
                        cent_to_euro = float(x[22])/100

                        """ Aspiration representation in boolean form. """
                        aspiration = aspiration_flag[x[1]]

                        engine_size= int(x[9])
                        weight = int(x[24])
                        """ Convert horsepower to decimal representation from German representation. """
                        try:
                            if x[15].__contains__(","):
                                horsepower = x[15].split(',')
                                horsepower = float(str(horsepower[0]+"."+horsepower[1]))
                            elif x[15].__contains__("."):
                                horsepower = float(x[15])
                            else:
                                horsepower = float(x[15])
                        except Exception as e:
                            print("Error: ",e)

                        make = x[17]
                        """ Add all the transformed data to the list. """
                        list = [elt,
                                cylinders_count[x[19]],
                                engine_size,
                                weight,
                                horsepower,
                                aspiration,
                                cent_to_euro,
                                make]

                        transformed_data.append(list)

                    except Exception as e:
                        """ Print the exception occurred. """
                        print("ERROR:",e)

        """ Return the transformed and clean data in list of list format. """
        return transformed_data

    def full_tranformation(self):

        """ One hot encoding for engine location """

        engine_loc_transform = {
                                'front': 1,
                                'mid': 2,
                                'back': 3
                                }

        """ Cylinder count transformation """

        cylinders_count = {
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8
        }

        """ Boolean flag for aspiration """

        aspiration_flag = {
            'turbo': 1,
            'std': 0
        }

        transformed_data = []
        with open(self.file_path) as f:

            """ Add headers to a header list. """
            header=[
                'aspiration',
                'body-style'
                'bore',
                'city-mpg',
                'compression-ratio',
                'curb-weight',
                'drive-wheels',
                'engine-location',
                'engine-size',
                'engine-type',
                'fuel-system',
                'fuel-type',
                'height',
                'highway-mpg',
                'horsepower',
                'length',
                'make',
                'normalized-losses',
                'num-of-cylinders',
                'num-of-doors',
                'peak-rpm',
                'price',
                'stroke',
                'weight',
                'wheel-base',
                'width']
            transformed_data.append(header)
            """ Skip the header line. """
            next(f)

            """ drive wheels. """
            drive_wheels = {'fwd': 1,
                            'rwd': 2,
                            '4wd': 4,
                            '6wd': 6,
                            '8wd': 8,
                            '12wd': 12}

            """ Fuel type. """
            fuel_cache = {
                'gas': 1,
                'diesel': 2,
                'petrol': 3
            }

            """ Engine location in the vehicle, can be transformed to int. """
            e_loc = {
                'front': 1,
                'mid': 2,
                'back': 3
            }

            """ Number of cylinders."""
            no_of_cylinders = {
                'one': 1,
                'two': 2,
                'three':3,
                'four':4,
                'five':5,
                'six':6,
                'seven':7,
                'eight':8,
                'twelve':12
            }

            """ Door count. """
            no_of_doors = {
                'one':1,
                'two':2,
                'three':3,
                'four':4,
                'five':5
            }

            temp_data = list()
            for x in f:
                temp_data = []
                """ Split the data in the line. """
                x = x.split(";")
                """ Check for the bad data present. """
                if '-' in x or ' -' in x or '- ' in x or ' ' in x or None in x:

                    """ Skip the bad data. """
                    pass
                else:
                    try:

                        """ Aspiration representation in boolean form. """
                        aspiration = aspiration_flag[x[1]]
                        temp_data.append(aspiration)
                        """ Body style """
                        body = str(x[2])
                        temp_data.append(body)
                        """ Bore - Diameter of the cylinder so, it should be in float """
                        bore = float(x[3])
                        temp_data.append(bore)
                        """ city-mpg - It is miles per gallon so it would be type float"""
                        city_mpg = float(x[4])
                        temp_data.append(city_mpg)
                        """ compression-ratio """
                        compression_ratio = x[5]
                        temp_data.append(compression_ratio)
                        """ curb-weight is the standard weight of the vehicle so it should be float."""
                        curb_weight = float(x[6])
                        temp_data.append(curb_weight)
                        """ drive-wheels """
                        dw = drive_wheels[x[7]]
                        temp_data.append(dw)
                        """ engine location """
                        engine_loc = e_loc[x[8]]
                        temp_data.append(engine_loc)
                        """ engine-size - Engine is engine displacement so it can be in int type  """
                        engine_size = int(x[9])
                        temp_data.append(engine_size)
                        """ engine-type can be string """
                        engine_type = x[10]
                        temp_data.append(engine_type)
                        """ fuel-system can be string """
                        fuel_system = x[11]
                        temp_data.append(fuel_system)
                        """ fuel-type """
                        fuel_type = fuel_cache[x[12]]
                        temp_data.append(fuel_type)
                        """ height is a float type """
                        height = float(x[13])
                        temp_data.append(height)
                        """ highway-mpg is estimate fuel so it will be in float. Fuel efficiency. """
                        highway_mpg = float(x[14])
                        temp_data.append(highway_mpg)
                        """ horsepower """
                        if x[15].__contains__(","):
                            horsepower = x[15].split(',')
                            horsepower = float(str(horsepower[0] + "." + horsepower[1]))
                        elif x[15].__contains__("."):
                            horsepower = float(x[15])
                        else:
                            horsepower = float(x[15])
                        temp_data.append(horsepower)
                        """ length """
                        length = float(x[16])
                        temp_data.append(length)
                        """ make """
                        make = x[17]
                        temp_data.append(make)
                        """ normalized-losses , the normalization might me int or a float."""
                        normalized_losses = float(x[18])
                        temp_data.append(normalized_losses)
                        """ num-of-cylinders is an integer field. """
                        num_of_cylinders = no_of_cylinders[x[19]]
                        temp_data.append(num_of_cylinders)
                        """ num-of-doors is an integer field. """
                        num_of_doors = no_of_doors[x[20]]
                        temp_data.append(num_of_doors)
                        """ peak-rpm. Revolution per minute can be taken as integer value."""
                        peak_rpm = int(x[21])
                        temp_data.append(peak_rpm)
                        """ price. It is a float entity. As it is in cents we have to convert it into Euros."""
                        price = float(x[22])/100
                        temp_data.append(price)
                        """ stroke. It is the distance so measured in float."""
                        stroke = float(x[23])
                        temp_data.append(stroke)
                        """weight."""
                        weight = int(x[24])
                        temp_data.append(weight)
                        """Wheel base measured between rotational centers of wheels"""
                        wheel_base = float(x[25])
                        temp_data.append(wheel_base)
                        """Width """
                        width = float(x[26])
                        temp_data.append(width)

                        """ Add all the transformed data to the list. """
                        transformed_data.append(temp_data)

                    except Exception as e:
                        """ Print the exception occurred. """
                        print("ERROR:",e)

        """ Return the transformed and clean data in list of list format. """
        return transformed_data