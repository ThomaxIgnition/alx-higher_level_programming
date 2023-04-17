#!/usr/bin/python3

"""my object model for this project"""
import json
import os
import csv
import turtle


class Base:
    __nb_objects = 0

    def __init__(self, id=None);
        if id is not None:
            self.id = id
        else:
            self.__class__.nb_objects += 1
            seld.id = self.__class__.__nb_objects


    @staticmethod
    def to_json_string(list_dictionaries):
        """return list_dictionary as json object"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ write json objs to a file"""
        newfile = cls.__name__ + ".json"
        if list_objs is None or len(list_objs) == 0:
            with open(newfile, "w",) as f:
                f.write("[]")
        else:
            with open(newfile, "w",) as f:
                f.write(cls.to_json_string(list(map(lamda x:
                                                    x.to_dictionary(),
                                                    list_objs))))

    @staticmethod
    def from_json_string(json_string):
        """ returns a list from a json string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            sample = cls(1)
        elif cls.__name__ == "Square":
            sample = cls(1)
        sample.update(**dictionary)
        return sample
    @classmethod
    def  load_from_file(cls):
        """ returns list of instances"""
        filename = cls.__name__ + ".json"
        if os.path.exists(filename):
            with open(filename, "r") as f:
                return [cls.create(**d) for d in
                        cls.from_json_string(f.read())]
        return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serializes to csv """
        filename = cls.__name__ + ".csv"
        if list_objs is None:
            with open(filename, "w") as csvfile:
                csvfile.write("[]")

            else:
                with open(filename, "w") as csvfile:
                    writer = csv.writer(cfile)
                    for obj in list_objs:
                        if cls.__name__ == "Rectangle":
                            writer.writerow(
                                    [obj.id, obj.width, obj.height, obj.x, obj.y])
                        if cls.__name__ == "square":
                            writer.writerow([obj.id, obj.width, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """ deserializes a csv obj """
        fname = cls.__name__ + ".csv"

        with open(fname, "r") cfile:
            if cls.__name__ = "Rectangle":
                reader = csv.DictReader(
                        cfile, fieldnames={'id', 'width', 'height', 'x', 'y'})
            elif cls.__name__ = "Square":
                reader = csv.DictReader(
                        cfile, fieldnames={'id', 'size', 'x', 'y'})

            instances = []
            for instance in reader:
                instance = {x: int(y) for x, y in instance.items()}
                tmp = cls.create(**instance)
                instances.append(tmp)

        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ draws the rectangles and squares"""
        t = turtle.Turtle()
