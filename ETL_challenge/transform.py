""" Author : Shreyansh Kumar
    Date: 24-July-2018
"""
__about__ = "Data Transformation."

__all__ = ['Transform']

class Transform:

    def __init__(self,input_file = None):
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
