"""
DS 3500 - MP1

Usage:
    python pipeline.py --input data.csv --output clean.csv
    python pipeline.py --input data.csv --output results.json --format json --verbose
"""

import argparse
import logging
import sys
from pathlib import Path
from src import (
    create_cleaning_report,
    load_data,
    process_data,
    save_data,
    setup_logging,
    validate_dataframe,
    validate_input,
)



logger = logging.getLogger(__name__)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Analyze a data file"
    )

    parser.add_argument(
        "--input", "-i",
        required=True,
        help="Path to the input file"
    )

    parser.add_argument(
        "--config", "-c",
        required=True,
        help="Path to YAML config file"

    )

    parser.add_argument(
        "--output", "-o",
        required=True,
        help="Path to the output file"
    )


    parser.add_argument(
        "--verbose", "-v", 
        action="store_true", 
        help="Enable verbose logging"
    )

    return parser.parse_args()


def main():
    args = parse_arguments()

    setup_logging(verbose=args.verbose)

    logger.debug(f"Arguments parsed: {vars(args)}")

    if not validate_input(args.config):
        sys.exit(1)

    if not validate_input(args.input):
        sys.exit(1)

    try:
        df = load_data(args.input)
        config = load_data(args.config)
        logger.debug(f"Input files loaded: {args.input}, {args.config}")
    except ValueError as error:
        logger.error(error)
        sys.exit(1)

    original_df = df.copy()


    validation = config.get("validation", {})
    required_columns = validation.get("required_columns", [])
    numeric_columns = validation.get("numeric_columns", [])

    try:
        df = validate_dataframe(df, required_columns, numeric_columns)
        logger.info(f"Rows before validation: {len(original_df)}. Rows after validation: {len(df)}")
    except ValueError as error:
        logger.error(error)
        sys.exit(1)

    post_validation_df = df.copy()

    try:
        df = process_data(df, config)
        logger.info(f"Processing complete: {len(post_validation_df)} -> {len(df)} rows")
    except ValueError as error:
        logger.error(error)
        sys.exit(1)

    report = create_cleaning_report(post_validation_df, df)

    df = save_data(df, args.output)
    logger.info(f"Saved cleaned data to {args.output}")

    print(f"Data cleaning report: {report}")



if __name__ == "__main__":
    main() 
