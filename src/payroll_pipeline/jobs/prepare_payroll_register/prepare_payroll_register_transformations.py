from pyspark.sql import Column, DataFrame, Window
from pyspark.sql import functions as F


def create_unique_key(payroll_register_raw: DataFrame) -> DataFrame:
    """create a payroll_register_key, which should be an md5 hashed key, concatenating the employee_id, pay_run_id, and lohnart_code, to be used to deduplicate the dataset."""
    raise NotImplementedError("generate layer target")


def cast_data_types(create_unique_key_result: DataFrame) -> DataFrame:
    """cast gl_account and lohnart_code as integers, cast pay_date as date"""
    raise NotImplementedError("generate layer target")


def filter_retro_runs(cast_data_types_result: DataFrame) -> DataFrame:
    """Keep only rows where pay_run = 'retro'"""
    raise NotImplementedError("generate layer target")


def filter_regular_runs(cast_data_types_result: DataFrame) -> DataFrame:
    """Take the deduplicated payroll register and filter where pay_run = 'regular'"""
    raise NotImplementedError("generate layer target")


def sum_retro_amounts(filter_retro_runs_result: DataFrame) -> DataFrame:
    """Group the dataframe filtered for retro amounts on employee_id, pay_period, and lohnart_code, and take the sum of amount_eur."""
    raise NotImplementedError("generate layer target")


def join_regular_and_retro_data(filter_regular_runs_result: DataFrame, sum_retro_amounts_result: DataFrame) -> DataFrame:
    """Join the grouped retro pay dataframe to the filtered regular pay dataframe on employee_id, pay_period and lohnart_code."""
    raise NotImplementedError("generate layer target")


def combine_regular_and_retro_pay(join_regular_and_retro_data_result: DataFrame) -> DataFrame:
    """Replace the regular amount with regular plus retro pay, treating a missing retro total as zero."""
    raise NotImplementedError("generate layer target")
