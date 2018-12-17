import connection
import datetime
import calculations

THIS_MONDAY = calculations.define_date_of_monday()
LAST_MONDAY = calculations.define_date_of_monday((9999, 12, 31))

@connection.connection_handler
def fill_geogrpahy(cursor, geo):
    cursor.execute("""
                    INSERT INTO geography (
                            country_iso, 
                            country_source1, 
                            country_optima, 
                            country_norm, 
                            country_sap, 
                            cluster_lvl1, 
                            cluster_lvl2
                            )
                    VALUES (
                            %(cy_iso)s,
                            %(cy_s1)s,
                            %(cy_opt)s,
                            %(cy_norm)s,
                            %(cy_sap)s,
                            %(clust1)s,
                            %(clust2)s);""",
                   {
                       'cy_iso': geo.get('country_iso'),
                       'cy_s1': geo.get('country_s1'),
                       'cy_opt': geo.get('country_optima'),
                       'cy_norm': geo.get('country_norm'),
                       'cy_sap': geo.get('country_sap'),
                       'clust1': geo.get('cluster_lvl1'),
                       'clust2': geo.get('cluster_lvl2')
                    }
                   )


@connection.connection_handler
def fill_customer(cursor, customer):
    cursor.execute("""
                    INSERT INTO customers (
                            customer_source1, 
                            customer_source1_node, 
                            customer_s1_shipment, 
                            customer_optima, 
                            customer_sap, 
                            customer_da, 
                            customer_norm_name, 
                            country
                            )
                    VALUES (
                            %(cust_s1)s,
                            %(cust_s1_node)s,
                            %(cust_s1_shipment)s,
                            %(cust_optima)s,
                            %(cust_sap)s,
                            %(cust_da)s,
                            %(cust_norm)s,
                            %(cust_cy)s);""",
                   {
                       'cust_s1': customer.get('customer_s1'),
                       'cust_s1_node': customer.get('customer_s1_node'),
                       'cust_s1_shipment': customer.get('customer_s1_node'),
                       'cust_optima': customer.get('customer_optima'),
                       'cust_sap': customer.get('customer_sap'),
                       'cust_da': customer.get('customer_da'),
                       'cust_norm': customer.get('customer_norm'),
                       'cust_cy': customer.get('country')
                    }
                   )


@connection.connection_handler
def fill_optima(cursor, optima, version):
    cursor.execute("""
                    INSERT INTO optima (
                            version, 
                            country, 
                            customer, 
                            line_up, 
                            promo_id, 
                            promo_start, 
                            promo_end, 
                            sos, 
                            eos, 
                            volume
                            )
                    VALUES (
                            %(version)s,
                            %(country)s,
                            %(customer)s,
                            %(lineup)s,
                            %(promo_id)s,
                            %(promo_start)s,
                            %(promo_end)s,
                            %(promo_sos)s,
                            %(promo_eos)s,
                            %(promo_vol)s);""",
                   {
                       'version': version,
                       'country': optima.get('country'),
                       'customer': optima.get('customer'),
                       'lineup': optima.get('line_up'),
                       'promo_id': optima.get('promo_id'),
                       'promo_start': optima.get('promo_start'),
                       'promo_end': optima.get('promo_end'),
                       'promo_sos': optima.get('sos'),
                       'promo_eos': optima.get('eos'),
                       'promo_vol': optima.get('volume')
                    }
                   )


@connection.connection_handler
def fill_product(cursor, product):
    cursor.execute("""
                    INSERT INTO products (
                            fpc, 
                            description, 
                            it_ean, 
                            sw_ean, 
                            cs_ean, 
                            pt_ean, 
                            cpg, 
                            category, 
                            brand, 
                            optima_lineup, 
                            family3, 
                            phase_in_date, 
                            phase_out_date, 
                            predecessor, 
                            successor
                            )
                    VALUES (
                            %(fpc)s,
                            %(description)s,
                            %(it_ean)s,
                            %(sw_ean)s,
                            %(cs_ean)s,
                            %(pt_ean)s,
                            %(cpg)s,
                            %(cat)s,
                            %(brand)s,
                            %(optima_lineup)s,
                            %(family3)s,
                            %(phase_in_date)s,
                            %(phase_out_date)s,
                            %(predecessor)s,
                            %(successor)s);""",
                   {
                       'fpc': product.get('fpc'),
                       'description': product.get('description'),
                       'it_ean': product.get('it_ean'),
                       'sw_ean': product.get('sw_ean'),
                       'cs_ean': product.get('cs_ean'),
                       'pt_ean': product.get('pt_ean'),
                       'cat': product.get(''),
                       'brand': product.get('description'),
                       'optima_lineup': product.get('description'),
                       'family3': product.get('description'),
                       'phase_in_date': product.get('description'),
                       'phase_out_date': product.get('description'),
                       'predecessor': product.get('description'),
                       'successor': product.get('description')
                   }
                   )


@connection.connection_handler
def fill_shipment(cursor, shipment):
    cursor.execute("""
                    INSERT INTO shipments (
                            order_nr, 
                            fpc_id, 
                            year, 
                            month, 
                            day, 
                            customer, 
                            uom, 
                            shipment
                            )
                    VALUES (
                            %(order_nr)s,
                            %(fpc)s,
                            %(year)s,
                            %(month)s,
                            %(day)s,
                            %(customer)s,
                            %(uom)s,
                            %(shipment)s);""",
                   {
                       'order_nr': shipment.get('order_nr'),
                       'fpc': shipment.get('fpc_id'),
                       'year': shipment.get('year'),
                       'month': shipment.get('month'),
                       'day': shipment.get('day'),
                       'customer': shipment.get('customer'),
                       'uom': shipment.get('uom'),
                       'shipment': shipment.get('shipment')
                    }
                   )


@connection.connection_handler
def get_number_of_bis(cursor, start_date=THIS_MONDAY, end_date=LAST_MONDAY):
    cursor.execute("""
                    SELECT COUNT(da_id) FROM da
                    INNER JOIN da_vol ON da_vol.da_id = da.id
                    WHERE da.version_flag = 'y' AND da_vol.week >= %(start_date)s AND da_vol.week < %(end_date)s; """,
                   {
                       'start_date': start_date,
                       'end_date': end_date
                   }
                   )
    return cursor.fetchone().get('da_id')


@connection.connection_handler
def get_volume_of_bis(cursor, start_date=THIS_MONDAY, end_date=LAST_MONDAY):
    cursor.execute("""
                    SELECT SUM(volume) FROM da_vol
                    INNER JOIN da ON da.id = da_vol.da_id
                    WHERE da.version_flag = 'y' AND da_vol.week >= %(start_date)s AND da_vol.week < %(end_date)s;""",
                   {
                       'start_date': start_date,
                       'end_date': end_date
                   }
                   )
    return cursor.fetchone().get('volume')


@connection.connection_handler
def get_nr_of_unique_customers(cursor, start_date=THIS_MONDAY, end_date=LAST_MONDAY):
    cursor.execute("""
                    SELECT COUNT(customer_name) FROM da
                    INNER JOIN da_vol ON da_vol.da_id = da.id
                    WHERE da.version_flag = 'y' AND da_vol.week >= %(start_date)s AND da_vol.week < %(end_date)s;""",
                   {
                       'start_date': start_date,
                       'end_date': end_date
                   }
                   )
    return cursor.fetchone().get('customer_name')


@connection.connection_handler
def get_countries_and_clusters(cursor):
    cursor.execute("""
                    SELECT country_iso, cluster_lvl1, cluster_lvl2 FROM geography""")
    return cursor.fetchall()


@connection.connection_handler
def get_shipment(cursor, category, country, customer, lineup, start_date, end_date=THIS_MONDAY):
    cursor.execute("""
                    SELECT shipment FROM shipments
                    LEFT OUTER JOIN customers ON shipments.customer = customers.customer_s1_shipment
                    LEFT OUTER JOIN products ON shipments.fpc_id = products.fpc
                    WHERE 
                        products.category = %(category)s AND
                        customers.country = %(country)s AND
                        customers.customer_norm_name = %(customer_name)s AND
                        products.family3 = %(lineup)s AND
                        shipments.year >= %(start_year)s AND
                        shipments.year <= %(end_year)s AND
                        shipments.month >= %(start_month)s AND
                        shipments.month <= %(end_month)s AND
                        shipments.day >= %(start_day)s AND
                        shipments.day < %(end_day)s;""",
                   {
                       'category': category,
                       'country': country,
                       'customer_name': customer,
                       'lineup': lineup,
                       'start_year': start_date[0],
                       'end_year': end_date[0],
                       'start_month': start_date[1],
                       'end_month': end_date[1],
                       'start_day': start_date[2],
                       'end_day': end_date[2]
                   }
                   )
    return cursor.fetchall()


@connection.connection_handler
def get_submitted_da_volume(cursor, start_date, category, country, customer, lineup, weeks_back, end_date=THIS_MONDAY):
    cursor.execute("""
                    SELECT volume FROM da_vol
                    RIGHT OUTER JOIN da ON da_vol.da_id = da.id
                    LEFT OUTER JOIN map_product ON da.product_category = map_product.da_category
                    LEFT OUTER JOIN customers ON da.customer_name = customers.customer_da
                    WHERE
                        map_product.category= %(category)s AND
                        da.country = %(country)s AND
                        customers.customer_norm_name = %(customer)s AND
                        da.product_code = %(lineup)s AND
                        da_vol.week >= %(start_date)s AND
                        da_vol.week < %(end_date)s AND
                        da.last_updated + 7 * %(weeks_back)s <= da_vol.week AND
                        da.version_flag = 'y';""",
                   {
                       'category': category,
                       'country': country,
                       'customer': customer,
                       'lineup': lineup,
                       'start_date': start_date,
                       'weeks_back': weeks_back,
                       'end_date': end_date
                   }
                   )
    return cursor.fetchall()


@connection.connection_handler
def add_new_bi(cursor, da_elements):
    cursor.execute("""
                    INSERT INTO da (
                        da_name, 
                        da_group, 
                        country, 
                        da_description, 
                        da_long_descr, 
                        fm, 
                        da_type_lvl1, 
                        da_type_lvl2, 
                        da_type_lvl3, 
                        cpg, 
                        product_category, 
                        product_level, 
                        product_code, 
                        start_date, 
                        end_date, 
                        nr_of_periods, 
                        cust_start_date, 
                        cust_end_date, 
                        unit_of_measure, 
                        location, 
                        created, 
                        submitted, 
                        last_updated, 
                        w01_vol, w02_vol, w03_vol, w04_vol, w05_vol, w06_vol, w07_vol, w08_vol, w09_vol, 
                        w10_vol, w11_vol, w12_vol, w13_vol, w14_vol, w15_vol, w16_vol, w17_vol, w18_vol, w19_vol, 
                        w20_vol, w21_vol, w22_vol, w23_vol, w24_vol
                        )
                    VALUES (
                        %(da_name)s, 
                        %(da_group)s, 
                        %(country)s, 
                        %(da_description)s, 
                        %(da_long_descr)s, 
                        %(fm)s, 
                        %(da_type_lvl1)s, 
                        %(da_type_lvl2)s, 
                        %(da_type_lvl3)s, 
                        %(cpg)s, 
                        %(product_category)s, 
                        %(product_level)s, 
                        %(product_code)s, 
                        %(start_date)s, 
                        %(end_date)s, 
                        %(nr_of_periods)s, 
                        %(cust_start_date)s, 
                        %(cust_end_date)s, 
                        %(unit_of_measure)s, 
                        %(location)s, 
                        %(created)s, 
                        %(submitted)s, 
                        %(last_updated)s, 
                        %(w01_vol)s, 
                        %(w02_vol)s, 
                        %(w03_vol)s, 
                        %(w04_vol)s, 
                        %(w05_vol)s, 
                        %(w06_vol)s, 
                        %(w07_vol)s, 
                        %(w08_vol)s, 
                        %(w09_vol)s, 
                        %(w10_vol)s, 
                        %(w11_vol)s, 
                        %(w12_vol)s, 
                        %(w13_vol)s, 
                        %(w14_vol)s, 
                        %(w15_vol)s, 
                        %(w16_vol)s, 
                        %(w17_vol)s, 
                        %(w18_vol)s, 
                        %(w19_vol)s, 
                        %(w20_vol)s, 
                        %(w21_vol)s, 
                        %(w22_vol)s, 
                        %(w23_vol)s, 
                        %(w24_vol)s);""",
                   {
                       'da_name': da_elements.get('da_name'),
                       'da_group': da_elements.get('da_group'),
                       'country': da_elements.get('country'),
                       'da_description': da_elements.get('da_description'),
                       'da_long_descr': da_elements.get('da_long_descr'),
                       'fm': da_elements.get('fm'),
                       'da_type_lvl1': da_elements.get('da_type_lvl1'),
                       'da_type_lvl2': da_elements.get('da_type_lvl2'),
                       'da_type_lvl3': da_elements.get('da_type_lvl3'),
                       'cpg': da_elements.get('cpg'),
                       'product_category': da_elements.get('product_category'),
                       'product_level': da_elements.get('product_level'),
                       'product_code': da_elements.get('product_code'),
                       'start_date': da_elements.get('start_date'),
                       'end_date': da_elements.get('end_date'),
                       'nr_of_periods': da_elements.get('nr_of_periods'),
                       'cust_start_date': da_elements.get('cust_start_date'),
                       'cust_end_date': da_elements.get('cust_end_date'),
                       'unit_of_measure': da_elements.get('unit_of_measure'),
                       'location': da_elements.get('location'),
                       'created': da_elements.get('created'),
                       'submitted': da_elements.get('submitted'),
                       'last_updated': da_elements.get('last_updated'),
                       'w01_vol': da_elements.get('w01_vol'),
                       'w02_vol': da_elements.get('w02_vol'),
                       'w03_vol': da_elements.get('w03_vol'),
                       'w04_vol': da_elements.get('w04_vol'),
                       'w05_vol': da_elements.get('w05_vol'),
                       'w06_vol': da_elements.get('w06_vol'),
                       'w07_vol': da_elements.get('w07_vol'),
                       'w08_vol': da_elements.get('w08_vol'),
                       'w09_vol': da_elements.get('w09_vol'),
                       'w10_vol': da_elements.get('w10_vol'),
                       'w11_vol': da_elements.get('w11_vol'),
                       'w12_vol': da_elements.get('w12_vol'),
                       'w13_vol': da_elements.get('w13_vol'),
                       'w14_vol': da_elements.get('w14_vol'),
                       'w15_vol': da_elements.get('w15_vol'),
                       'w16_vol': da_elements.get('w16_vol'),
                       'w17_vol': da_elements.get('w17_vol'),
                       'w18_vol': da_elements.get('w18_vol'),
                       'w19_vol': da_elements.get('w19_vol'),
                       'w20_vol': da_elements.get('w20_vol'),
                       'w21_vol': da_elements.get('w21_vol'),
                       'w22_vol': da_elements.get('w22_vol'),
                       'w23_vol': da_elements.get('w23_vol'),
                       'w24_vol': da_elements.get('w24_vol')
                   }
                   )

    cursor.execute("""
                    SELECT 
                        id, 
                        start_date, 
                        end_date, 
                        w01_vol, 
                        w02_vol, 
                        w03_vol, 
                        w04_vol, 
                        w05_vol, 
                        w06_vol, 
                        w07_vol, 
                        w08_vol, 
                        w09_vol, 
                        w10_vol, 
                        w11_vol, 
                        w12_vol, 
                        w13_vol, 
                        w14_vol, 
                        w15_vol, 
                        w16_vol,
                        w17_vol,
                        w18_vol,
                        w19_vol,
                        w20_vol,
                        w21_vol,
                        w22_vol,
                        w23_vol,
                        w24_vol
                    FROM da
                    WHERE id = (SELECT MAX(ID) FROM da);""")
    last_id = cursor.fetchone()
    starting_date = calculations.define_date_of_monday(last_id.get('start_date'))

    for key, value in last_id.items():
        if key in "vol" and value != 0:
            iteration = 0
            week = starting_date + datetime.timedelta(days=iteration * 7)
            cursor.execute("""
                            INSERT INTO da_vol (da_id, week, volume)
                            VALUES (
                                %(da_id)s,
                                %(week)s,
                                %(volume)s);""",
                           {
                               'da_id': last_id.get('id'),
                               'week': week,
                               'volume': value
                           }
                           )
            iteration += 1
