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
from data_loaders import load_data
from data_processor import process_data, create_cleaning_report


logger = logging.getLogger(__name__)


def setup_logging(verbose=False):
    level = logging.DEBUG if verbose else logging.INFO

    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)-8s %(name)s - %(message)s",
        datefmt="%H:%M:%S"
    )



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


def validate_input(filepath):
    if Path(filepath).is_file():
        logger.info(f"Input file validated: {filepath}")
        return True
    else:
        logger.error(f"Input file not found: {filepath}")
        return False


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

    try:
        df = process_data(df, config)
        logger.info(f"Processing complete: {len(original_df)} -> {len(df)} rows")
    except ValueError as error:
        logger.error(error)
        sys.exit(1)

    report = create_cleaning_report(original_df, df)
    print(f"Data cleaning report: {report}")

    df.to_csv(args.output)
    logger.info(f"Saved cleaned data to {args.output}")


if __name__ == "__main__":
    main() 
