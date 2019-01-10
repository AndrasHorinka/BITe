import datetime
import numpy


def define_date_of_monday(date=(), weeks=1):
    """ Returns the date of Monday of the given week. Both arguments are optional.
    Arguments:
        date: a tuple of (year,month,day). If omitted it takes today's date as argument.
        weeks: an integer to tell how many weeks are needed. If omitted it takes one week only.
    Returns: a dictionary, with {'start_date': datetime object, 'end_date': datetime object}
    """
    def calculate_date(year, month, day):
        given_date = datetime.datetime(year, month, day)
        start_monday = given_date - datetime.timedelta(days=given_date.weekday())
        last_monday = start_monday + datetime.timedelta(days=weeks * 7)
        return {'start_date': start_monday, 'end_date': last_monday}

    if date:
        return calculate_date(int(date[0]), int(date[1]), int(date[2]))

    current_year = int(datetime.date.today().strftime("%Y"))
    current_month = int(datetime.date.today().strftime("%m"))
    current_day = int(datetime.date.today().strftime("%d"))
    return calculate_date(current_year, current_month, current_day)


def calculate_bi_accuracy(shipments, das):
    """ Returns a list of % integers for BI % Accuracy. All arguments are optional - if any of them are omitted -> total Univerese is considered.
    Arguments:
        shipments: a list of shipment volume
        das: a list of submitted BI volume
    Returns:
        accuracy: list of floats (%).
        """
    np_shipment = numpy.array(shipments)
    np_da = numpy.array(das)
    return np_shipment/np_da * 100
