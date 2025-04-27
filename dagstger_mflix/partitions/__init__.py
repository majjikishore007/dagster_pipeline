from dagster import MonthlyPartitionsDefinition


START_DATE = '2011-01-01'
END_DATE = '2016-01-01'

monthly_partition = MonthlyPartitionsDefinition(
    start_date="2023-01-01", # Make sure this start_date is appropriate
    fmt="%Y-%m-%d",      # Standard format for monthly partitions
    end_offset=1         # Key change: Target the current month's partition
)