from flask import request
import db_queries
import connection
import calculations
import converter

def sample_fill_geographies():
    geos = connection.read_file('/sql_setup/geography_sample.csv')
    for geo in geos:
        db_queries.fill_geogrpahy(geo)


def sample_fill_customers():
    customers = connection.read_file('/sql_setup/customer_map_sample.csv')
    for customer in customers:
        db_queries.fill_customer(customer)


def sample_fill_optima():
    optimas = connection.read_file('/sql_setup/optima_sample.csv')
    version = calculations.define_date_of_monday()
    for optima in optimas:
        db_queries.fill_optima(optima, version)


def sample_fill_product():
    products = connection.read_file('/sql_setup/productmap_baby_sample.csv')
    for product in products:
        db_queries.fill_product(product)


def sample_fill_shipment():
    shipments = connection.read_file('/sql_setup/shipment_sample.csv')
    for shipment in shipments:
        db_queries.fill_shipment(shipment)



def feed_main_page_dashboard():
    current_week = calculations.define_date_of_monday()
    next_two_weeks = calculations.define_date_of_monday(weeks=2)
    next_four_weeks = calculations.define_date_of_monday(weeks=4)

    nr_of_bi = dict()
    nr_of_bi['total'] = db_queries.get_number_of_bis()
    nr_of_bi['current_week'] = db_queries.get_number_of_bis(current_week.get('start_date'),
                                                            current_week.get('end_date'))
    nr_of_bi['next_two_weeks'] = db_queries.get_number_of_bis(next_two_weeks.get('start_date'),
                                                              next_two_weeks.get('end_date'))
    nr_of_bi['next_four_weeks'] = db_queries.get_number_of_bis(next_four_weeks.get('start_date'),
                                                               next_four_weeks.get('end_date'))

    submitted_volume = dict()
    submitted_volume['total'] = db_queries.get_number_of_bis()
    submitted_volume['current_week'] = db_queries.get_number_of_bis(current_week.get('start_date'),
                                                                    current_week.get('end_date'))
    submitted_volume['next_two_weeks'] = db_queries.get_number_of_bis(next_two_weeks.get('start_date'),
                                                                      next_two_weeks.get('end_date'))
    submitted_volume['next_four_weeks'] = db_queries.get_number_of_bis(next_four_weeks.get('start_date'),
                                                                       next_four_weeks.get('end_date'))

    unique_customers = dict()
    unique_customers['total'] = db_queries.get_number_of_bis()
    unique_customers['current_week'] = db_queries.get_number_of_bis(current_week.get('start_date'),
                                                                    current_week.get('end_date'))
    unique_customers['next_two_weeks'] = db_queries.get_number_of_bis(next_two_weeks.get('start_date'),
                                                                      next_two_weeks.get('end_date'))
    unique_customers['next_four_weeks'] = db_queries.get_number_of_bis(next_four_weeks.get('start_date'),
                                                                       next_four_weeks.get('end_date'))

    dashboard = dict()
    dashboard.update({'nr_of_bi': nr_of_bi, 'submitted_volume': submitted_volume, 'unique_customers': unique_customers})
    return dashboard


def feed_main_page_countries():
    geographies = db_queries.get_countries_and_clusters()
    all_geos = list()
    for geo in geographies:
        for key, values in enumerate(geo):
            all_geos.append(values)

    return list(set(all_geos.sort()))


def get_bi_accuracy(category='*', country='*', customer='*', lineup='*', start_date=(2000, 1, 1), end_date=None, weeks_back=1):
    """ Returns a list of % integers for BI % Accuracy. All arguments are optional - if any of them are omitted -> total Univerese is considered.
    Arguments:
        category: string - representing a CATEGORY within PRODUCTS database.
        country: string - representing COUNTRY within CUSTOMER database.
        customer: string - representing CUSTOMER_NORM_NAME within CUSTOMER database.
        lineup: string - representing FAMILY3 within PRODUCTS database. --> SEE ISSUE TRACKING!
        start_date: tuple - (year, month, day)
        end_date: tuple - (year, month, day)
        weeks_back: integer - default 1 weeks back
    Returns:
        accuracy: list of floats (ie. 54.30)
    """
    ship_query = db_queries.get_shipment(category='*', country='*', customer='*', lineup='*',
                                         start_date=('2000', '01', '01'), end_date=('9999', '12', '31'))
    shipments = converter.convert_dict_in_lists_to_list(ship_query)

    def send_proper_bi_query(bi_query):
        das = converter.convert_dict_in_lists_to_list(bi_query)
        accuracy = calculations.calculate_bi_accuracy(shipments, das)
        return accuracy

    if end_date:
        bi_query = db_queries.get_submitted_da_volume(start_date, category=category, country=country, customer=customer,
                                                      lineup=lineup, end_date=end_date, weeks_back=weeks_back)
        return send_proper_bi_query(bi_query)

    bi_query = db_queries.get_submitted_da_volume(start_date, category=category, country=country, customer=customer,
                                                  lineup=lineup, weeks_back=weeks_back)
    return send_proper_bi_query(bi_query)


def add_new_bi():
    """ Adds a new line into DA table. da_details = request.form
    Arguments:
        da_details: a dictionary with the elements of a DA (da_name, status, da_group, country, da_description,
        da_ long_descr, fm, da_type_lvl1, da_type_lvl2, da_type_lvl3, periodicity, cpg, product_category, product_level,
        product_code, cust_dimension, customer_name, start_date, end_date, nr_of_periods, cust_start_date,
        cust_end_date, unit_of_measure, location, created, submitted, last_updated and weekly volume."""

    keys = ['da_name', 'status', 'da_group', 'country', 'da_description',
            'da_long_descr', 'fm', 'da_type_lvl1', 'da_type_lvl2', 'da_type_lvl3', 'periodicity', 'cpg',
            'product_category', 'product_level',
            'product_code', 'cust_dimension', 'customer_name', 'start_date', 'end_date', 'nr_of_periods',
            'cust_start_date',
            'cust_end_date', 'unit_of_measure', 'location', 'created', 'submitted', 'last_updated']
    da = dict()
    for key in keys:
        if key in request:
            da['key'] = request.form['key']

    db_queries.add_new_bi(da)
