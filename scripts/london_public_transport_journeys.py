import datetime

from dataflows import Flow, load, dump_to_path, PackageWrapper, ResourceWrapper,printer

def set_format_and_name(package: PackageWrapper):
    package.pkg.descriptor['title'] = 'London public journeys by type of transport'
    package.pkg.descriptor['name'] = 'london-public-transport'
    # Change path and name for the resource:
    package.pkg.descriptor['resources'][0]['path'] = 'data/public-transport-journeys.csv'
    package.pkg.descriptor['resources'][0]['name'] = 'london-public-transport'

    yield package.pkg
    res_iter = iter(package)
    first: ResourceWrapper = next(res_iter)
    yield first.it
    yield from package

def filter_rows_journeys(rows):
    for row in rows:
        if row['Bus journeys (m)'] != '':
            yield row

def london_underground_journeys(link):
    Flow(
        load(link,
             sheet=2, engine='openpyxl', format='xlsx'),
        filter_rows_journeys,
        set_format_and_name,
        dump_to_path('data'),
        printer(num_rows=1)
    ).process()


london_underground_journeys('https://data.london.gov.uk/download/public-transport-journeys-type-transport/a7a69c22-150c-49f3-a1fd-90d4c24d98d4/tfl-journeys-type.xls')