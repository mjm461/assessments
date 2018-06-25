import pandas as pd
import argparse
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
import matplotlib.pyplot as plt
import operator


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--assessments', type=str, default="assessments.csv", help="CSV file input")
    parser.add_argument('--parcel', type=str, help="The parcel to compare", required=False)
    args = parser.parse_args()

    grade = {'A': 1, 'A-':2, 'B+': 3, 'B':4, 'B-': 5, 'C+':6, 'C':7, 'C-':8, 'D+':9, 'D':10, 'D-':11, 'F':12}
    basement = { 'Full': 1, 'Part': 0}
    data = pd.read_csv(args.assessments)
    data = data.loc[data['Garage'] >= 1]

    data['Grade'] = data['Grade'].map(grade)
    data['Basement'] = data['Basement'].map(basement)

    columns = ['Bedroom','Full Bath','Living Area','Total Rooms', 'Grade', 'Garage', 'Basement']

    parcel = data.loc[data['Parcel Id'] == args.parcel][columns]

    df=data[columns]

    for type in ['Zillow Estimate', 'County Total']:
        y=data[type]

        #x_train,x_test,y_train,y_test=train_test_split(df,y,train_size=0.8,random_state=42)
        reg=LinearRegression()
        reg.fit(df,y)
        sorted_x = sorted(grade.items(), key=operator.itemgetter(1))
        lg = []
        for k, v in sorted_x:
            parcel['Grade'] = v
            lg.append(reg.predict(parcel)[0])

        grad=GradientBoostingRegressor(n_estimators=400, max_depth=5, min_samples_split=2, learning_rate=0.1, loss='ls')
        grad.fit(df,y)

        gb = []
        for k, v in sorted_x:
            parcel['Grade'] = v
            gb.append(grad.predict(parcel)[0])


        d = {'col1': [1, 2], 'col2': [3, 4]}

        results = pd.DataFrame(data={
            'Grade': [x[1] for x in sorted_x],
            'LinearRegression': lg,
            'GradientBoosting': gb
        })

        ax = None
        ax = results.plot(x='Grade', y='LinearRegression', color='red', ax=ax)
        ax = results.plot(x='Grade', y='GradientBoosting', color='blue', ax=ax)
        ax.grid('on', which='major')
        ax.set_xticklabels([x[0] for x in sorted_x])
        plt.title(type)

        plt.show()
