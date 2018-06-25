import pandas as pd
import numpy
import matplotlib.pyplot as plt
import argparse
from pandas.tseries import converter
converter.register()

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--assessments', type=str, default="assessments.csv", help="CSV file input")
    parser.add_argument('--parcel', type=str, help="The parcel to compare", required=False)
    args = parser.parse_args()

    df = pd.read_csv(args.assessments)
    df['Sale Date'] = pd.to_datetime(df['Sale Date'], format='%m/%d/%Y')
    parcel = df.loc[df['Parcel Id'] == args.parcel]

    ax = df.plot(kind='scatter', x='Lot Area', y='County Land Value')
    parcel.plot(kind='scatter', x='Lot Area', y='County Land Value', color='red', ax=ax)
    ax = df.plot(kind='scatter', x='Living Area', y='County Total', color='blue')
    recent = df.loc[df['Sale Date'] > numpy.datetime64('2015-01-01')]
    recent.plot(kind='scatter', x='Living Area', y='County Total', color='yellow', ax=ax)
    parcel.plot(kind='scatter', x='Living Area', y='County Total', color='red', ax=ax)

    ax = None
    color = ['red', 'blue', 'green']
    for nbeds in range(3,6):
        beds = df.loc[df['Bedroom'] == nbeds]
        ax = beds.plot(kind='scatter', x='Bedroom', y='County Total', color=color[nbeds%len(color)], ax=ax)
    ax = parcel.plot(kind='scatter', x='Bedroom', y='County Total', color='yellow', ax=ax)

    ax = None
    color = ['red', 'blue', 'green']
    for nbeds in range(2,5):
        beds = df.loc[df['Full Bath'] == nbeds]
        ax = beds.plot(kind='scatter', x='Full Bath', y='County Total', color=color[nbeds%len(color)], ax=ax)
    ax = parcel.plot(kind='scatter', x='Full Bath', y='County Total', color='yellow', ax=ax)

    ax = None
    match = df.loc[df['Bedroom'] == parcel['Bedroom'].values[0] ]
    match = match.loc[ match['Full Bath'] == parcel['Full Bath'].values[0] ]
    ax = match.plot(kind='scatter', x='Bedroom', y='County Total', color='blue')
    ax = parcel.plot(kind='scatter', x='Bedroom', y='County Total', color='yellow', ax=ax)

    plt.show()

