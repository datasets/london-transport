<a href="https://datahub.io/core/london-transport"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25)" alt="badge" /></a>

London public journeys by type of transport - this dataset was scrapped from 
[London data](https://data.london.gov.uk)

### Data

The dataset is inside data folder. The data presents number of journeys on the public transport network by TFL reporting period, by type of transport. Data is broken down by bus, underground, DLR, tram, Overground and cable car.

* Period lengths are different in periods 1 and 13, and the data is not adjusted to account for that.
* Docklands Light Railway journeys are based on automatic passenger counts at stations.
* Overground and Tram journeys are based on automatic on-carriage passenger counts. 
* Reliable Overground journey numbers have only been available since October 2010.

The Emirates Air Line cable car service began 28 June 2012.

### Preparation

You will need Python 3.6 or greater and dataflows library to run the script

To update the data run the process script locally:

```
# Install dataflows
pip install dataflows

# Run the script
python london-data.py:
```

### Licence

Open goverment licence

> You are encouraged to use and re-use the Information that is available under this licence freely and flexibly, with only a few conditions. Using Information under this licence Use of copyright and database right material expressly made available under this licence (the 'Information') indicates your acceptance of the terms and conditions below. The Licensor grants you a worldwide, royalty-free, perpetual, non-exclusive licence to use the Information subject to the conditions below. This licence does not affect your freedom under fair dealing or fair use or any other copyright or database right exceptions and limitations.

You may find further information [here](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
