from contextlib import contextmanager

from src.infraestructure.database.sqlalchemy import (database, init_database,
                                                     metadata)


def assert_validation_error(len_, loc, type_, excinfo):
    def write_message(expected, gotten):
        return f"expected: '{expected}', got: '{gotten}'"

    errors = excinfo.value.errors()
    assert len(errors) == len_, write_message(len_, len(errors))

    error, *_ = errors
    assert error["loc"] == (loc,), write_message(loc, error.get("loc", None))
    assert error["type"] == type_, write_message(
        type_, error.get("type", None)
    )


def _truncate_tables():
    database.execute(
        """TRUNCATE {} RESTART IDENTITY""".format(
            ",".join(
                f'"{table.name}"' for table in reversed(metadata.sorted_tables)
            )
        )
    )


@contextmanager
def clear_database():
    init_database()
    _truncate_tables()
    yield
    _truncate_tables()
