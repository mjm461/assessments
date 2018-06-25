from assessment.puller import AggregatePuller
import csv
import argparse
import os

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--zwid', type=str, help="Zillow API ID")
    parser.add_argument('--parcels', type=str, help="Path to file containing parcels or a comma parcel list")
    args = parser.parse_args()

    ap = AggregatePuller(zwid=args.zwid)

    if os.path.exists(args.parcels):
        parcel_ids = set([h.split("\t")[0].replace("-", "")
                          for h in open(args.parcels).read().split("\n") if h and not h.startswith("#")])
    else:
        parcel_ids = [parcel_id for parcel_id in args.parcels.split(",")]

    with open('assessments.csv', 'w') as f:  # Just use 'w' mode in 3.x
        w = csv.DictWriter(f, ap.headers)
        w.writeheader()
        for i, parcel_id in enumerate(parcel_ids):
            print("Parsing %s (%d of %d)" % (parcel_id, i + 1, len(parcel_ids)))
            w.writerow(ap.parse(parcel_id))
