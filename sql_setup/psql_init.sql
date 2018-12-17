ALTER TABLE IF EXISTS ONLY public.products DROP CONSTRAINT IF EXISTS fk1_category CASCADE;
ALTER TABLE IF EXISTS ONLY public.products DROP CONSTRAINT IF EXISTS fk2_brand CASCADE;
ALTER TABLE IF EXISTS ONLY public.products DROP CONSTRAINT IF EXISTS fk3_optima_lineup CASCADE;
ALTER TABLE IF EXISTS ONLY public.products DROP CONSTRAINT IF EXISTS fk4_family_three CASCADE;
ALTER TABLE IF EXISTS ONLY public.products DROP CONSTRAINT IF EXISTS fk5_cpg CASCADE;

ALTER TABLE IF EXISTS ONLY public.customers DROP CONSTRAINT IF EXISTS fk_customers CASCADE;

ALTER TABLE IF EXISTS ONLY public.da DROP CONSTRAINT IF EXISTS fk1_da_cy CASCADE;
ALTER TABLE IF EXISTS ONLY public.da DROP CONSTRAINT IF EXISTS fk2_da_cpg CASCADE;
ALTER TABLE IF EXISTS ONLY public.da DROP CONSTRAINT IF EXISTS fk3_da_status CASCADE;
ALTER TABLE IF EXISTS ONLY public.da DROP CONSTRAINT IF EXISTS fk4_da_version CASCADE;
ALTER TABLE IF EXISTS ONLY public.da DROP CONSTRAINT IF EXISTS fk5_da_period CASCADE;
ALTER TABLE IF EXISTS ONLY public.da DROP CONSTRAINT IF EXISTS fk6_da_category CASCADE;
ALTER TABLE IF EXISTS ONLY public.da DROP CONSTRAINT IF EXISTS fk7_da_prod_level CASCADE;
ALTER TABLE IF EXISTS ONLY public.da DROP CONSTRAINT IF EXISTS fk8_da_prod_code CASCADE;
ALTER TABLE IF EXISTS ONLY public.da DROP CONSTRAINT IF EXISTS fk9_da_da_type CASCADE;

ALTER TABLE IF EXISTS ONLY public.gpdb_optima_lineup DROP CONSTRAINT IF EXISTS fk1_da_brand CASCADE;
ALTER TABLE IF EXISTS ONLY public.gpdb_optima_lineup DROP CONSTRAINT IF EXISTS fk2_da_category CASCADE;

ALTER TABLE IF EXISTS ONLY public.gpdb_family_three DROP CONSTRAINT IF EXISTS fk1_da_brand CASCADE;
ALTER TABLE IF EXISTS ONLY public.gpdb_family_three DROP CONSTRAINT IF EXISTS fk2_da_category CASCADE;

ALTER TABLE IF EXISTS ONLY public.gpdb_brand DROP CONSTRAINT IF EXISTS fk1_da_category CASCADE;

ALTER TABLE IF EXISTS ONLY public.da_vol DROP CONSTRAINT IF EXISTS fk1_da_id CASCADE;

ALTER TABLE IF EXISTS ONLY public.shipments DROP CONSTRAINT IF EXISTS shipments_fk0 CASCADE;
ALTER TABLE IF EXISTS ONLY public.shipments DROP CONSTRAINT IF EXISTS shipments_fk1 CASCADE;

ALTER TABLE IF EXISTS ONLY public.optima DROP CONSTRAINT IF EXISTS optima_fk1 CASCADE;
ALTER TABLE IF EXISTS ONLY public.optima DROP CONSTRAINT IF EXISTS optima_fk2 CASCADE;
ALTER TABLE IF EXISTS ONLY public.optima DROP CONSTRAINT IF EXISTS optima_fk3 CASCADE;

ALTER TABLE IF EXISTS ONLY public.products DROP CONSTRAINT IF EXISTS pk_products CASCADE;
ALTER TABLE IF EXISTS ONLY public.customers DROP CONSTRAINT IF EXISTS pk_customers CASCADE;
ALTER TABLE IF EXISTS ONLY public.geography DROP CONSTRAINT IF EXISTS pk_geography CASCADE;
ALTER TABLE IF EXISTS ONLY public.da DROP CONSTRAINT IF EXISTS pk_da CASCADE;
ALTER TABLE IF EXISTS ONLY public.gpdb_optima_lineup DROP CONSTRAINT IF EXISTS pk_optima_lineup CASCADE;
ALTER TABLE IF EXISTS ONLY public.gpdb_family_three DROP CONSTRAINT IF EXISTS pk_family_three CASCADE;
ALTER TABLE IF EXISTS ONLY public.gpdb_brand DROP CONSTRAINT IF EXISTS pk_brand CASCADE;
ALTER TABLE IF EXISTS ONLY public.gpdb_category DROP CONSTRAINT IF EXISTS pk_category CASCADE;
ALTER TABLE IF EXISTS ONLY public.da_product_type DROP CONSTRAINT IF EXISTS pk_da_type CASCADE;
ALTER TABLE IF EXISTS ONLY public.da_product_code DROP CONSTRAINT IF EXISTS pk_prod_code CASCADE;
ALTER TABLE IF EXISTS ONLY public.da_product_level DROP CONSTRAINT IF EXISTS pk_prod_level CASCADE;
ALTER TABLE IF EXISTS ONLY public.da_periodicity DROP CONSTRAINT IF EXISTS pk_periodicity CASCADE;
ALTER TABLE IF EXISTS ONLY public.da_version DROP CONSTRAINT IF EXISTS pk_da_version CASCADE;
ALTER TABLE IF EXISTS ONLY public.da_status DROP CONSTRAINT IF EXISTS pk_da_status CASCADE;
ALTER TABLE IF EXISTS ONLY public.da_cpg DROP CONSTRAINT IF EXISTS pk_cpg CASCADE;


DROP SEQUENCE IF EXISTS public.customers_customer_id_seq CASCADE;
DROP SEQUENCE IF EXISTS public.geography_country_id_seq CASCADE;
DROP SEQUENCE IF EXISTS public.da_id_seq CASCADE;
DROP SEQUENCE IF EXISTS public.gpdb_optima_lineup_optima_lineup_id_seq CASCADE;
DROP SEQUENCE IF EXISTS public.gpdb_family_three_family_id_seq CASCADE;
DROP SEQUENCE IF EXISTS public.gpdb_brand_brand_id_seq CASCADE;
DROP SEQUENCE IF EXISTS public.gpdb_category_category_id_seq CASCADE;
DROP SEQUENCE IF EXISTS public.da_product_type_da_type_id_seq CASCADE;
DROP SEQUENCE IF EXISTS public.da_product_code_da_product_code_id_seq CASCADE;
DROP SEQUENCE IF EXISTS public.da_product_level_da_product_level_id_seq CASCADE;
DROP SEQUENCE IF EXISTS public.da_periodicity_da_period_id_seq CASCADE;
DROP SEQUENCE IF EXISTS public.da_version_da_version_flag_id_seq CASCADE;
DROP SEQUENCE IF EXISTS public.da_status_da_status_id_seq CASCADE;
DROP SEQUENCE IF EXISTS public.da_cpg_da_cpg_id_seq CASCADE;


DROP TABLE IF EXISTS public.products;
DROP TABLE IF EXISTS public.customers;
DROP TABLE IF EXISTS public.da;
DROP TABLE IF EXISTS public.gpdb_optima_lineup;
DROP TABLE IF EXISTS public.gpdb_family_three;
DROP TABLE IF EXISTS public.gpdb_brand;
DROP TABLE IF EXISTS public.gpdb_category;
DROP TABLE IF EXISTS public.da_product_type;
DROP TABLE IF EXISTS public.da_product_code;
DROP TABLE IF EXISTS public.da_product_level;
DROP TABLE IF EXISTS public.da_periodicity;
DROP TABLE IF EXISTS public.da_version;
DROP TABLE IF EXISTS public.da_status;
DROP TABLE IF EXISTS public.da_cpg;
DROP TABLE IF EXISTS public.da_vol;
DROP TABLE IF EXISTS public.shipments;
DROP TABLE IF EXISTS public.optima;
DROP TABLE IF EXISTS public.geography;


CREATE TABLE products (
	fpc INTEGER NOT NULL,
	description VARCHAR(255) NOT NULL,
	it_ean INTEGER,
	sw_ean INTEGER,
	cs_ean INTEGER,
	pt_ean INTEGER,
	cpg INTEGER NOT NULL,
	category INTEGER NOT NULL,
	brand INTEGER NOT NULL,
	optima_lineup INTEGER NOT NULL,
	family_three INTEGER NOT NULL,
	phase_in_date DATE,
	phase_out_date DATE,
	predecessor INTEGER,
	successor INTEGER);

CREATE TABLE customers (
	customer_id SERIAL NOT NULL,
	cust_dimension VARCHAR(150) NOT NULL DEFAULT 'customer group',
	customer_source1 VARCHAR(255) NOT NULL,
	customer_source1_node INTEGER NOT NULL,
	customer_s1_shipment VARCHAR(255) NOT NULL UNIQUE,
	customer_optima VARCHAR(255) NOT NULL UNIQUE,
	customer_sap VARCHAR(255) NOT NULL,
	customer_da VARCHAR(255) NOT NULL,
	customer_norm_name VARCHAR(255) NOT NULL,
	country INTEGER NOT NULL);

CREATE TABLE geography (
	country_id SERIAL NOT NULL,
	country_iso VARCHAR(40) NOT NULL UNIQUE,
	country_source1 VARCHAR(255) NOT NULL UNIQUE,
	country_optima VARCHAR(255) NOT NULL UNIQUE,
	country_norm VARCHAR(255) NOT NULL UNIQUE,
	country_sap VARCHAR(255) NOT NULL UNIQUE,
	cluster_lvl1 VARCHAR(255) NOT NULL,
	cluster_lvl2 VARCHAR(255) NOT NULL);

CREATE TABLE da (
	id SERIAL NOT NULL,
	version_flag_id INTEGER NOT NULL DEFAULT '0',
	da_name VARCHAR(255) NOT NULL,
	da_status_id INTEGER NOT NULL,
	da_group VARCHAR(255) NOT NULL,
	country INTEGER NOT NULL,
	da_description VARCHAR(255) NOT NULL,
	da_long_descr VARCHAR(255),
	da_type INTEGER NOT NULL,
	period_id INTEGER NOT NULL,
	cpg INTEGER NOT NULL,
	product_category_id INTEGER NOT NULL,
	product_level INTEGER NOT NULL,
	product_code INTEGER NOT NULL,
	da_customer_id INTEGER NOT NULL,
	start_date DATE NOT NULL,
	end_date DATE NOT NULL,
	nr_of_periods INTEGER NOT NULL,
	cust_start_date DATE,
	cust_end_date DATE,
	unit_of_measure VARCHAR(5) NOT NULL,
	location VARCHAR(10) NOT NULL,
	created DATE NOT NULL,
	submitted DATE NOT NULL,
	last_updated DATE);

CREATE TABLE gpdb_optima_lineup (
	optima_lineup_id SERIAL NOT NULL,
	optima_lineup_desc VARCHAR(120) NOT NULL,
	category_id INTEGER NOT NULL,
	brand_id INTEGER NOT NULL);

CREATE TABLE gpdb_family_three (
	family_id SERIAL NOT NULL,
	family_desc VARCHAR(150),
	category_id INTEGER NOT NULL,
	brand_id INTEGER NOT NULL);

CREATE TABLE gpdb_brand (
	brand_id SERIAL NOT NULL,
	category_id INTEGER NOT NULL,
	da_brand_name VARCHAR(80) NOT NULL,
	s1_brand_node INTEGER NOT NULL,
	s1_brand_desc VARCHAR(80) NOT NULL,
	sap_brand_desc VARCHAR(80) NOT NULL);

CREATE TABLE gpdb_category (
	category_id SERIAL NOT NULL,
	da_category_name VARCHAR(80) NOT NULL,
	s1_category_node INTEGER NOT NULL,
	s1_category_desc VARCHAR(120) NOT NULL,
	sap_category_desc VARCHAR(120) NOT NULL);

CREATE TABLE da_product_type (
	da_type_id SERIAL NOT NULL,
	da_type_lvl1 VARCHAR(150) NOT NULL,
	da_type_lvl2 VARCHAR(150),
	da_type_lvl3 VARCHAR(150));

CREATE TABLE da_product_code (
	da_product_code_id SERIAL NOT NULL,
	da_product_code_desc VARCHAR(150) NOT NULL);

CREATE TABLE da_product_level (
	da_product_level_id SERIAL NOT NULL,
	da_product_level_desc VARCHAR(80));

CREATE TABLE da_periodicity (
	da_period_id SERIAL NOT NULL,
	da_periodicity_name VARCHAR(100) NOT NULL DEFAULT 'weekly');

CREATE TABLE da_version (
	da_version_flag_id SERIAL NOT NULL,
	da_version_flag VARCHAR(2) NOT NULL);

CREATE TABLE da_status (
	da_status_id SERIAL NOT NULL,
	da_status_name VARCHAR(100) NOT NULL DEFAULT 'draft');

CREATE TABLE da_cpg (
	da_cpg_id SERIAL NOT NULL,
	da_cpg_name VARCHAR(2) NOT NULL);

CREATE TABLE da_vol (
	da_id INTEGER NOT NULL,
	da_fm INTEGER NOT NULL,
	da_week DATE NOT NULL,
	da_volume FLOAT(20) DEFAULT '0');

CREATE TABLE shipments (
	order_nr VARCHAR(100),
	fpc_id INTEGER NOT NULL,
	shipment_week DATE NOT NULL,
	customer INTEGER NOT NULL,
	uom VARCHAR(2) NOT NULL,
	shipment INTEGER NOT NULL);

CREATE TABLE optima (
  version DATE NOT NULL,
	country INTEGER NOT NULL,
	customer INTEGER NOT NULL,
	line_up INTEGER NOT NULL,
	promo_id VARCHAR(100) NOT NULL,
	promo_start DATE NOT NULL,
	promo_end DATE NOT NULL,
	sos DATE NOT NULL,
	eos DATE NOT NULL,
	volume FLOAT(20));


ALTER TABLE ONLY products ADD CONSTRAINT pk_products PRIMARY KEY (fpc);
ALTER TABLE ONLY customers ADD CONSTRAINT pk_customers PRIMARY KEY (customer_id);
ALTER TABLE ONLY geography ADD CONSTRAINT pk_geography PRIMARY KEY (country_id);
ALTER TABLE ONLY da ADD CONSTRAINT pk_da PRIMARY KEY (id);
ALTER TABLE ONLY gpdb_optima_lineup ADD CONSTRAINT pk_optima_lineup PRIMARY KEY (optima_lineup_id);
ALTER TABLE ONLY gpdb_family_three ADD CONSTRAINT pk_family_three PRIMARY KEY (family_id);
ALTER TABLE ONLY gpdb_brand ADD CONSTRAINT pk_brand PRIMARY KEY (brand_id);
ALTER TABLE ONLY gpdb_category ADD CONSTRAINT pk_category PRIMARY KEY (category_id);
ALTER TABLE ONLY da_product_type ADD CONSTRAINT pk_da_type PRIMARY KEY (da_type_id);
ALTER TABLE ONLY da_product_code ADD CONSTRAINT pk_prod_code PRIMARY KEY (da_product_code_id);
ALTER TABLE ONLY da_product_level ADD CONSTRAINT pk_prod_level PRIMARY KEY (da_product_level_id);
ALTER TABLE ONLY da_periodicity ADD CONSTRAINT pk_periodicity PRIMARY KEY (da_period_id);
ALTER TABLE ONLY da_version ADD CONSTRAINT pk_da_version PRIMARY KEY (da_version_flag_id);
ALTER TABLE ONLY da_status ADD CONSTRAINT pk_da_status PRIMARY KEY (da_status_id);
ALTER TABLE ONLY da_cpg ADD CONSTRAINT pk_cpg PRIMARY KEY (da_cpg_id);


ALTER TABLE ONLY products ADD CONSTRAINT fk1_category FOREIGN KEY (category) REFERENCES gpdb_category(category_id);
ALTER TABLE ONLY products ADD CONSTRAINT fk2_brand FOREIGN KEY (brand) REFERENCES gpdb_brand(brand_id);
ALTER TABLE ONLY products ADD CONSTRAINT fk3_optima_lineup FOREIGN KEY (optima_lineup) REFERENCES gpdb_optima_lineup(optima_lineup_id);
ALTER TABLE ONLY products ADD CONSTRAINT fk4_family_three FOREIGN KEY (family_three) REFERENCES gpdb_family_three(family_id);
ALTER TABLE ONLY products ADD CONSTRAINT fk5_cpg FOREIGN KEY (cpg) REFERENCES da_cpg(da_cpg_id);

ALTER TABLE ONLY customers ADD CONSTRAINT fk_customers FOREIGN KEY (country) REFERENCES geography(country_id);

ALTER TABLE ONLY da ADD CONSTRAINT fk1_da_cy FOREIGN KEY (country) REFERENCES geography(country_id);
ALTER TABLE ONLY da ADD CONSTRAINT fk2_da_cpg FOREIGN KEY (cpg) REFERENCES da_cpg(da_cpg_id);
ALTER TABLE ONLY da ADD CONSTRAINT fk3_da_status FOREIGN KEY (da_status_id) REFERENCES da_status(da_status_id);
ALTER TABLE ONLY da ADD CONSTRAINT fk4_da_version FOREIGN KEY (version_flag_id) REFERENCES da_version(da_version_flag_id);
ALTER TABLE ONLY da ADD CONSTRAINT fk5_da_period FOREIGN KEY (period_id) REFERENCES da_periodicity(da_period_id);
ALTER TABLE ONLY da ADD CONSTRAINT fk6_da_category FOREIGN KEY (product_category_id) REFERENCES gpdb_category(category_id);
ALTER TABLE ONLY da ADD CONSTRAINT fk7_da_prod_level FOREIGN KEY (product_level) REFERENCES da_product_level(da_product_level_id);
ALTER TABLE ONLY da ADD CONSTRAINT fk8_da_prod_code FOREIGN KEY (product_code) REFERENCES da_product_code(da_product_code_id);
ALTER TABLE ONLY da ADD CONSTRAINT fk9_da_da_type FOREIGN KEY (da_type) REFERENCES da_product_type(da_type_id);

ALTER TABLE ONLY gpdb_optima_lineup ADD CONSTRAINT fk1_da_brand FOREIGN KEY (brand_id) REFERENCES gpdb_brand(brand_id);
ALTER TABLE ONLY gpdb_optima_lineup ADD CONSTRAINT fk2_da_category FOREIGN KEY (category_id) REFERENCES gpdb_category(category_id);

ALTER TABLE ONLY gpdb_family_three ADD CONSTRAINT fk1_da_brand FOREIGN KEY (brand_id) REFERENCES gpdb_brand(brand_id);
ALTER TABLE ONLY gpdb_family_three ADD CONSTRAINT fk2_da_category FOREIGN KEY (category_id) REFERENCES gpdb_category(category_id);

ALTER TABLE ONLY gpdb_brand ADD CONSTRAINT fk1_da_category FOREIGN KEY (category_id) REFERENCES gpdb_category(category_id);

ALTER TABLE ONLY da_vol ADD CONSTRAINT fk1_da_id FOREIGN KEY (da_id) REFERENCES da(id);

ALTER TABLE ONLY shipments ADD CONSTRAINT shipments_fk0 FOREIGN KEY (fpc_id) REFERENCES products(fpc);
ALTER TABLE ONLY shipments ADD CONSTRAINT shipments_fk1 FOREIGN KEY (customer) REFERENCES customers(customer_id);

ALTER TABLE ONLY optima ADD CONSTRAINT optima_fk1 FOREIGN KEY (country) REFERENCES geography(country_id);
ALTER TABLE ONLY optima ADD CONSTRAINT optima_fk2 FOREIGN KEY (customer) REFERENCES customers(customer_id);
ALTER TABLE ONLY optima ADD CONSTRAINT optima_fk3 FOREIGN KEY (line_up) REFERENCES gpdb_optima_lineup(optima_lineup_id);