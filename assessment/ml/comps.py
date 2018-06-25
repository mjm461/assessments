import pandas as pd
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--assessments', type=str, default="assessments.csv", help="CSV file input")
    parser.add_argument('--parcel', type=str, help="The parcel to compare", required=False)
    args = parser.parse_args()

    df = pd.read_csv(args.assessments)

    df['Comp Sale Price Mean'] = df[['Comp Sale Price 1', 'Comp Sale Price 2', 'Comp Sale Price 3', 'Comp Sale Price 4']].mean(axis=1)
    df['Comp County Total Mean'] = df[['Comp County Total 1', 'Comp County Total 2', 'Comp County Total 3', 'Comp County Total 4']].mean(axis=1)

    df['County Total Diff'] = df.apply(lambda x: x['County Total'] - x['Comp County Total Mean'], axis=1)

    print("Assessment vs the assessments of its comps:", df['County Total Diff'].mean())
    print("Area County $ Total/sqft:", df.apply(lambda x: x['County Total'] / x['Living Area'], axis=1).mean())

    if args.parcel:
        parcel = df.loc[df['Parcel Id'] == args.parcel]
        print("Parcel assessment vs the assessments of its comps:",  parcel.apply(lambda x: x['County Total'] - x['Comp County Total Mean'], axis=1).values[0])
        print("Parcel County $ Total/sqft:", parcel.apply(lambda x: x['County Total'] / x['Living Area'], axis=1).values[0])
