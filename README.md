### Pull/analyze housing data from Allegheny County Tax Site
Website:  http://www2.county.allegheny.pa.us/RealEstate/Search.aspx
-  [assessment/assessments.py](assessment/assessments.py) - Pulls the data from the County/Zillow to be analyized
-  [assessments/ml](assessment/ml/README.md) - Multiple scripts to analyze the data

#### Build/install

```bash
python setup.py install
```

- For more details on distutils:  https://docs.python.org/3/distutils/introduction.html

#### Pulling assessment data for analysis
1. *Optional* - Sign up for a Zillow Token:  https://www.zillow.com/howto/api/APIOverview.htm

2. Create a text file of housing ID's you are interested in pulling from the site, only the ID is necessary, such as assessments.txt.
    ```
    0000-S-00000-0000-01
    0000-S-00000-0000-02
    ```

- Alternative:  Pass a list of comma separated IDs:  0000-S-00000-0000-01,0000-S-00000-0000-02,...

3. Extract the data with [assessment/assessments.py](assessment/assessments.py) :

    ```bash
    python -m assessment.assessments --parcels assessments.txt  --zwid <Zillow Token>
    ```

    Notes about this module:

    - Caches the website in a ./data/:
        - Limits the number of times you hit the website
        - TODO:  Cache data in a Database (probably DynamoDb)

    - Outputs the file to assessments.csv:
        - The current output is a CSV
        - TODO: Create a data store (again probably DynamoDb)

4. Analyze the data using sklearn - samples scripts are here: [assessments/ml](assessment/ml/README.md)
