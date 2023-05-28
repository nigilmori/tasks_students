import datetime
import enum
import typing as tp  # noqa


class GranularityEnum(enum.Enum):
    """
    Enum for describing granularity
    """
    DAY = datetime.timedelta(days=1)
    TWELVE_HOURS = datetime.timedelta(hours=12)
    HOUR = datetime.timedelta(hours=1)
    THIRTY_MIN = datetime.timedelta(minutes=30)
    FIVE_MIN = datetime.timedelta(minutes=5)


def truncate_to_granularity(dt: datetime.datetime, gtd: GranularityEnum) -> datetime.datetime:
    """
    :param dt: datetime to truncate
    :param gtd: granularity
    :return: resulted datetime
    """
    tme = datetime.datetime.combine(datetime.date.min, dt.time()) - datetime.datetime.min
    otv_tme = datetime.timedelta(seconds=(tme.total_seconds() - (tme.total_seconds() % gtd.value.total_seconds())))
    return datetime.datetime.combine(dt.date(), datetime.time(0, 0, 0))+otv_tme


class DtRange:
    def __init__(
            self,
            before: int,
            after: int,
            shift: int,
            gtd: GranularityEnum
    ) -> None:
        """
        :param before: number of datetimes should take before `given datetime`
        :param after: number of datetimes should take after `given datetime`
        :param shift: shift of `given datetime`
        :param gtd: granularity
        """
        self._before = before
        self._after = after
        self._shift = shift
        self._gtd = gtd

    def __call__(self, dt: datetime.datetime) -> list[datetime.datetime]:
        """
        :param dt: given datetime
        :return: list of datetimes in range
        """
        center_datetime = truncate_to_granularity(dt, self._gtd) + self._shift * self._gtd.value
        otv = []
        for i in range(-self._before, self._after+1):
            otv.append(center_datetime + i * self._gtd.value)
        return otv


def get_interval(
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        gtd: GranularityEnum
) -> list[datetime.datetime]:
    """
    :param start_time: start of interval
    :param end_time: end of interval
    :param gtd: granularity
    :return: list of datetimes according to granularity
    """
    start_granular_time = truncate_to_granularity(start_time, gtd)
    end_granular_time = truncate_to_granularity(end_time, gtd)
    if start_granular_time != start_time:
        start_granular_time += gtd.value
    otv = []
    while start_granular_time <= end_granular_time:
        otv.append(start_granular_time)
        start_granular_time += gtd.value
    return otv
