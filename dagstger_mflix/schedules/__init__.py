# In schedules.py
from dagster import schedule, RunRequest
from ..jobs import movies_job
from ..partitions import monthly_partition # Import your partition definition

@schedule(
    cron_schedule="* * * * *", # Or "0 0 1 * *" for monthly
    job=movies_job,
   
)
def movies_manual_schedule(context):
    """
    Manually determines the partition key for the current month and yields a RunRequest.
    """
    # Get the partition key for the current time/date
    # context.scheduled_execution_time is recommended over datetime.datetime.now()
    # for testability and consistency with Dagster's time handling.
    execution_time = context.scheduled_execution_time
    partition_key_for_current_month = monthly_partition.get_partition_key_for_timestamp(
        execution_time.timestamp()
    )

    # Optional: Add logic here if needed, e.g., check if the partition already exists/succeeded

    yield RunRequest(
        # run_key helps idempotency - ensures only one run for this partition for this schedule tick
        run_key=f"monthly_{partition_key_for_current_month}",
        partition_key=partition_key_for_current_month
    )

# Assign the decorated function to the variable name Dagster expects
movies_schedule = movies_manual_schedule