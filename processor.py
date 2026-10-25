import logging


logger = logging.getLogger(__name__)


class SalaryProcessor:
    """Process salary records from the repository."""

    def __init__(self, repository):
        self.repository = repository

    def count_high_salaries(self, threshold):
        """Count salary records above the given threshold."""
        count = 0

        for row in self.repository.stream_salaries():
            _, salary, _, _ = row

            if salary > threshold:
                count += 1

        logger.info(
            "Processed salary records. "
            "High salary count: %d",
            count,
        )

        return count