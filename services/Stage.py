from django.db.models import QuerySet

from db.models import Stage


def get_stages() -> QuerySet[Stage]:
    return Stage.objects.all()


def create_stage(
        stage_name: str,
        stage_rows: int,
        stage_seats_in_row: int
) -> Stage:
    return Stage.objects.create(
        name=stage_name,
        rows=stage_rows,
        seats_in_row=stage_seats_in_row
    )
