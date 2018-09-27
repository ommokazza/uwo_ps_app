"""Abstract Formatter class
"""
class BaseFormatter:
    """Abstract Formatter class
    """
    def apply(self, labels):
        """Abstract method for applying formatter.

        Arguments:
            label tuple (list): All elements are str type,
                [0] : (goods, rates, arrows)
                [1] : (town1, rates, arrows)
                ~ (Max) [5] : (town5, ratws, arrows)

        Return:
            Formatted string (str)
            Empty string if failed
        """
        raise NotImplementedError()

class FoxyFormatter(BaseFormatter):
    """Concreate formatter class for foxytrixy

        Refer to https://www.trevii.com/foxytrixy/UWO/
    """
    def apply(self, labels):
        try:
            if len(labels) < 2:
                raise Exception

            result = "?price '" + labels[0][0] + "' "
            for town in labels[1:]:
                result += "'%s' %s%s;" % (town[0], town[1],
                                          self.__get_arrow_dict(town[2]))
            return result
        except:
            return ""

    def __get_arrow_dict(self, label):
        arrows_dict = {"0" : "u", "1" : "n", "2" : "d"} # up / neutral / down
        return arrows_dict[label]