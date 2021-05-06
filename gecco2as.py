#!/usr/bin/env python3
"""Convert GECCO TSV output into an antiSMASH sideload JSON file."""

import argparse
import csv
import json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", type=argparse.FileType(mode='r', encoding="utf-8"),
                        help="GECCO .clusters.tsv file to convert")
    args = parser.parse_args()

    # static content
    tool = {
        "name": "GECCO",
        "version": "0.6.2",  # TODO: Get that from gecco somehow?
        "description": "Biosynthetic Gene Cluster prediction with Conditional Random Fields",
    }

    # Initialise the dynamic content
    records = []
    current_record = {
        "subregions": [],
    }
    first = True

    reader = csv.DictReader(args.infile, delimiter="\t")
    for row in reader:
        if first:
            first = False
            current_record["name"] = row["sequence_id"]
        if row["sequence_id"] != current_record["name"]:
            records.append(current_record)
            current_record = {
                "name": row["sequence_id"],
                "subregions": [],
            }
        subregion = {
            "start": int(row["start"]),
            "end": int(row["end"]),
            "label": row["type"],
            "details": {
                "alkaloid_probability": row["alkaloid_probability"],
                "polyketide_probability": row["polyketide_probability"],
                "ripp_probability": row["ripp_probability"],
                "saccharide_probability": row["saccharide_probability"],
                "terpene_probability": row["terpene_probability"],
                "nrp_probability": row["nrp_probability"],
                "other_probability": row["other_probability"],
                "average_p": row["average_p"],
                "max_p": row["max_p"],
            },
        }
        current_record["subregions"].append(subregion)

    records.append(current_record)


    print(json.dumps({"tool": tool, "records": records}, indent="    "))


if __name__ == "__main__":
    main()
