from flask import request
import db_queries
import connection
import calculations


def sample_fill_geographies():
    geos = connection.read_file('/sql_setup/geography_sample.csv')
    for geo in geos:
        db_queries.fill_geogrpahy(geo)


def sample_fill_customers():
    customers = connection.read_file('/sql_setup/customer_map_sample.csv')
    for customer in customers:
        db_queries.fill_customer(customer)


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
        for values in geo.values():
            all_geos.append(values)

    all_geos.sort()
    return list(set(all_geos))


def maintain_geopgraphy():
    return db_queries.get_all_geographies()


def maintain_customer():
    return db_queries.get_all_customers()


def maintain_category():
    return db_queries.get_all_categories()


def maintain_brand():
    return db_queries.get_all_brands()


def maintain_optima_lineup():
    return db_queries.get_all_optima_lineups()


def maintain_family3():
    return db_queries.get_all_family3()


def maintain_SKU():
    return db_queries.get_all_FPCs()


def maintain_da_level_type():
    return db_queries.get_all_da_level_types()


def maintain_da_periodicity():
    return db_queries.get_all_da_periodicity()


def maintain_da_status():
    return db_queries.get_all_da_status()


def maintain_CPG():
    return db_queries.get_all_cpg()


def load_optima(filename):
    raw_optima = connection.read_file(filename)  # list of dictionaries

    def are_all_keys_included(promo_entry):
        MUST_HAVE_KEYS = ['country', 'customer', 'line_up', 'promo_id', 'promo_start', 'promo_end', 'sos', 'eos',
                          'volume']
        for key in MUST_HAVE_KEYS:
            if key not in promo_entry.keys():
                return False

        return True

    for entry in raw_optima:
        print(entry)
        if not are_all_keys_included(entry):
            return False

        promo_id = entry.get('promo_id')
        print(promo_id)
        line_up = entry.get('line_up')

        # convert country string into country ID
        country = entry.get('country')
        db_country = db_queries.get_country_id_by_optima_name(country)
        if not len(db_country) == 1:
            print("no CountryID found")
            return False
        entry['country'] = db_country.get('country_id')

        # convert customer string into customer ID
        customer = entry.get('customer')
        db_customer = db_queries.get_customer_id_by_optima_name(customer, entry.get('country'))
        if not len(db_customer) == 1:
            print("No CustomerID found")
            return False
        entry['customer'] = db_customer.get('customer_id')

        # convert lineup string into line_up ID
        lineup = entry.get('line_up')
        db_lineup = db_queries.get_lineup_id_by_optima_name(lineup)
        if not len(db_lineup) == 1:
            print("No Optima Lineup ID found")
            return False
        entry['line_up'] = db_lineup.get('optima_lineup_id')

        # converting sos to Monday of given week
        sos = entry.get('sos')
        sos_day = sos[3:5]
        sos_month = sos[0:3]
        sos_year = sos[5:]
        datetime_sos = calculations.define_date_of_monday((sos_year, sos_month, sos_day), 1)
        sos = datetime_sos.get('start_date')
        entry['sos'] = sos

        # converting eos to Monday of given week
        eos = entry.get('eos')
        eos_day = eos[3:5]
        eos_month = eos[0:3]
        eos_year = eos[5:]
        datetime_eos = calculations.define_date_of_monday((eos_year, eos_month, eos_day), 1)
        eos = datetime_eos.get('start_date')
        entry['eos'] = eos

        vol = int(entry.get('volume'))
        is_promo_already_stored = db_queries.is_optima_input_already_in(promo_id, line_up, sos, eos, vol)

        if len(is_promo_already_stored) == 0:
            db_queries.add_new_optima_promo(entry)







    # 1. check if all keys are are_all_keys_included() - done
    # 1b. convert all dates in each part into a datetime object
    # optima raw date format is: MM/DD/YYYY --> thus MDY mode is needed and no convertion is needed
    # 1c. convert all dataset into data_id -- done
    # 2. for each line check if it already exists or not? -- done
    # 2a. if it doesnt exists, add with current date --> it is set to default, done

    # 2b. if it exists, check if the time/volume got changed
    # 2c. if time/volume did not change - continue
    # 2d. if there is a change -
