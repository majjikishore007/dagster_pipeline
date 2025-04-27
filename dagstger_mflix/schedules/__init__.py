# In schedules.py
from dagster import schedule, RunRequest
from ..jobs import movies_job
from ..partitions import monthly_partition 
@schedule(
    cron_schedule="* * * * *",
    job=movies_job,
   
)
def movies_manual_schedule(context):
    """
    Manually determines the partition key for the current month and yields a RunRequest.
    """
  
    execution_time = context.scheduled_execution_time
    partition_key_for_current_month = monthly_partition.get_partition_key_for_timestamp(
        execution_time.timestamp()
    )


    yield RunRequest(
        run_key=f"monthly_{partition_key_for_current_month}",
        partition_key=partition_key_for_current_month
    )

movies_schedule = movies_manual_schedule