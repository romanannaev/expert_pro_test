from typing import Any, List, Dict
import datetime
import logging
from copy import deepcopy


class RestaurantHours:
    days: List[str] = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]

    def __init__(self, hours: Dict[str, List[Dict[str, Any]]]) -> None:
        self.hours: Dict[str, List[Dict[str, Any]]] = hours

    def unix_to_readable_time(self, unix_time: int) -> str:
        dt: datetime.datetime = datetime.datetime.fromtimestamp(
            unix_time, datetime.timezone.utc
        )

        if unix_time % 3600 == 0:
            return dt.strftime("%-I %p")

        return dt.strftime("%-I:%M %p")

    def normalize_hours(self) -> Dict[str, List[Dict[str, Any]]]:
        normalized_hours: Dict[str, List[Dict[str, Any]]] = deepcopy(self.hours)

        previous_day = self.days[-1]
        for day in self.days:
            if normalized_hours[day] and normalized_hours[day][0]["type"] == "close":
                normalized_hours[previous_day].append(normalized_hours[day].pop(0))

                if len(normalized_hours[previous_day]) % 2 != 0:
                    logging.warning(
                        "Something incorrect in stucture of this working hours: %s",
                        self.hours[previous_day],
                    )

            previous_day: str = day

        return normalized_hours

    def format_opening_hours(self) -> str:
        readable_hours: List[str] = []
        normalized_hours: Dict[str, List[Dict[str, Any]]] = self.normalize_hours()

        for day in self.days:
            intervals: List[Dict[str, Any]] = normalized_hours[day]
            if not intervals:
                readable_hours.append(f"{day.capitalize()}: Closed")
                continue

            day_intervals = []
            i = 0
            while i < len(intervals):
                open_time: str = self.unix_to_readable_time(intervals[i]["value"])
                if i + 1 < len(intervals) and intervals[i + 1]["type"] == "close":
                    close_time: str = self.unix_to_readable_time(
                        intervals[i + 1]["value"]
                    )
                    day_intervals.append(f"{open_time} - {close_time}")
                    i += 2

                else:
                    i += 1

            readable_hours.append(f"{day.capitalize()}: {', '.join(day_intervals)}")

        return "\n".join(readable_hours)
