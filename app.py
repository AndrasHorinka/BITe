from flask import Flask, render_template, request, flash, redirect, url_for
import operations
import os
from werkzeug.utils import secure_filename


APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'uploads')
ALLOWED_EXTENSIONS = set(['csv'])

app = Flask(__name__)
app.secret_key = "b'x\xe8u\xf1\x8b\xba\xbf\x85\x086K\x87\xb2\xb8\x07\x98"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024

@app.route('/')
def index():
    menus = [{'menu_title': 'Menu1', 'url': 'index', 'parameters': {}},
             {'menu_title': 'Menu2', 'url': 'index', 'parameters': {}},
             {'menu_title': 'Menu3', 'url': 'index', 'parameters': {}}]
    news = [{'message': 'news1', 'url': 'index', 'parameters': {}},
            {'message': 'news2', 'url': 'index', 'parameters': {}},
            {'message': 'news3', 'url': 'index', 'parameters': {}}]
    # SAMPLING FOR HTML BUILD UP - delete on long run. final gets data from operations.
    # dashboard = operations.feed_main_page_dashboard()
    dashboard = {
                'nr_of_bi':
                     {'total': 150, 'current_week': 60, 'next_two_weeks': 90, 'next_four_weeks': 120},
                'submitted_volume':
                     {'total': 2500, 'current_week': 1000, 'next_two_weeks': 1500, 'next_four_weeks': 1750},
                'unique_customers':
                     {'total': 28, 'current_week': 8, 'next_two_weeks': 13, 'next_four_weeks': 22}}
    # SAMPLING FOR HTML BUILD UP - delete on long run. final gets data from operations.
    # countries = operations.feed_main_page_countries()
    countries = {'primary': ['CE', 'CEN', 'CES'], 'secondary': ['HU', 'CZ', 'SK', 'HR', 'SI', 'PL', 'BT', 'CSR',
                                                                'Hun/Cro/Slo']}
    week_backs = ['1', '2', '4']
    return render_template('main.html', menus=menus, news=news, dashboard=dashboard, countries=countries, week_backs=week_backs)


@app.route('/error')
def error():
    return "Something went wrong"


@app.route('/maintenance')
def maintenance():
    return render_template('maintenance.html')


@app.route('/maintenance/geography')
def maintenance_geography():
    data = operations.maintain_geopgraphy()
    return render_template('base_data_maintain.html', data=data)


@app.route('/maintenance/customer')
def maintenance_customers():
    data = operations.maintain_customer()
    return render_template('base_data_maintain.html', data=data)


@app.route('/maintenance/category')
def maintenance_categories():
    data = operations.maintain_customer()
    return render_template('base_data_maintain.html', data=data)


@app.route('/maintenance/brand')
def maintenance_brands():
    data = operations.maintain_brand()
    return render_template('base_data_maintain.html', data=data)


@app.route('/maintenance/optima_lineup')
def maintenance_optima_lineups():
    data = operations.maintain_optima_lineup()
    return render_template('base_data_maintain.html', data=data)


@app.route('/maintenance/family3')
def maintenance_family3():
    data = operations.maintain_family3()
    return render_template('base_data_maintain.html', data=data)


@app.route('/maintenance/SKU')
def maintenance_fpc():
    pass


@app.route('/maintenance/DA_level_type')
def maintenance_da_level_types():
    data = operations.maintain_da_level_type()
    return render_template('base_data_maintain.html', data=data)


@app.route('/maintenance/DA_periodicity')
def maintenance_periodicity():
    data = operations.maintain_da_periodicity()
    return render_template('base_data_maintain.html', data=data)


@app.route('/maintenance/DA_status')
def maintenance_da_status():
    data = operations.maintain_da_status()
    return render_template('base_data_maintain.html', data=data)


@app.route('/maintenance/CPG')
def maintenance_CPG():
    data = operations.maintain_CPG()
    return render_template('base_data_maintain.html', data=data)


@app.route('/uploads', methods=['GET', 'POST'])
def upload_file():
    def allowed_file(filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def check_if_file_is_selected(uploaded_file):
        if uploaded_file.filename == '':
            flash('No selected file', 'error')
            return redirect(request.url)
        return True

    def inner_upload(uploaded_file):
        if uploaded_file and allowed_file(uploaded_file.filename):
            secured_filename = secure_filename(uploaded_file.filename)
            uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], secured_filename))
        return secured_filename

    if request.method == 'POST':
        if "optima" in request.files:
            file = request.files.get('optima')
            if check_if_file_is_selected(file):
                flash("Optima successfully uploaded", 'success')
                filename = inner_upload(file)
                operations.load_optima(os.path.join("uploads", filename))

        elif 'shipment' in request.files:
            file = request.files.get('shipment')
            if check_if_file_is_selected(file):
                flash("Shipment successfully uploaded", 'success')
                filename = inner_upload(file)
                operations.load_shipment(os.path.join("uploads", filename))

        return redirect(request.url)

    return render_template('uploads.html')


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )
