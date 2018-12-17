from flask import Flask, render_template, request
import operations

app = Flask(__name__)


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
    dashboard = {'nr_of_bi': {'total': 150, 'current_week': 60, 'next_two_weeks': 90, 'next_four_weeks': 120},
                 'submitted_volume': {'total': 2500, 'current_week': 1000, 'next_two_weeks': 1500, 'next_four_weeks': 1750},
                 'unique_customers': {'total': 28, 'current_week': 8, 'next_two_weeks': 13, 'next_four_weeks': 22},}
    # SAMPLING FOR HTML BUILD UP - delete on long run. final gets data from operations.
    # countries = operations.feed_main_page_countries()
    countries = {'primary': ['CE', 'CEN', 'CES',], 'secondary': ['HU', 'CZ', 'SK', 'HR', 'SI', 'PL', 'BT', 'CSR', 'Hun/Cro/Slo']}
    week_backs = ['1', '2', '4']
    return render_template('main.html', menus=menus, news=news, dashboard=dashboard, countries=countries, week_backs=week_backs)


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )
