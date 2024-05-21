from ..restaurant_hours import RestaurantHours


def test_format_opening_hours_closed_days() -> None:
    input_data = {
        "monday": [],
        "tuesday": [],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": [],
    }

    expected_output = (
        "Monday: Closed\n"
        "Tuesday: Closed\n"
        "Wednesday: Closed\n"
        "Thursday: Closed\n"
        "Friday: Closed\n"
        "Saturday: Closed\n"
        "Sunday: Closed"
    )

    restaurant = RestaurantHours(input_data)
    assert restaurant.format_opening_hours() == expected_output


def test_format_opening_hours_open_hours():
    input_data = {
        "monday": [{"type": "open", "value": 32400}, {"type": "close", "value": 72000}],
        "tuesday": [
            {"type": "open", "value": 36000},
            {"type": "close", "value": 64800},
        ],
        "wednesday": [],
        "thursday": [
            {"type": "open", "value": 37800},
            {"type": "close", "value": 64800},
        ],
        "friday": [{"type": "open", "value": 36000}],
        "saturday": [
            {"type": "close", "value": 3600},
            {"type": "open", "value": 36000},
        ],
        "sunday": [
            {"type": "close", "value": 3600},
            {"type": "open", "value": 43200},
            {"type": "close", "value": 75600},
        ],
    }

    expected_output = (
        "Monday: 9 AM - 8 PM\n"
        "Tuesday: 10 AM - 6 PM\n"
        "Wednesday: Closed\n"
        "Thursday: 10:30 AM - 6 PM\n"
        "Friday: 10 AM - 1 AM\n"
        "Saturday: 10 AM - 1 AM\n"
        "Sunday: 12 PM - 9 PM"
    )

    restaurant = RestaurantHours(input_data)
    assert restaurant.format_opening_hours() == expected_output


def test_format_opening_hours_cross_day_hours():
    input_data = {
        "monday": [],
        "tuesday": [],
        "wednesday": [],
        "thursday": [],
        "friday": [{"type": "open", "value": 64800}],  # 6 PM
        "saturday": [
            {"type": "close", "value": 3600},  # 1 AM
            {"type": "open", "value": 32400},  # 9 AM
            {"type": "close", "value": 39600},  # 11 AM
            {"type": "open", "value": 57600},  # 4 PM
            {"type": "close", "value": 82800},  # 11 PM
        ],
        "sunday": [],
    }

    expected_output = (
        "Monday: Closed\n"
        "Tuesday: Closed\n"
        "Wednesday: Closed\n"
        "Thursday: Closed\n"
        "Friday: 6 PM - 1 AM\n"
        "Saturday: 9 AM - 11 AM, 4 PM - 11 PM\n"
        "Sunday: Closed"
    )

    restaurant = RestaurantHours(input_data)
    assert restaurant.format_opening_hours() == expected_output


def test_unix_to_readable_time():
    input_data = 32400
    expected_output = "9 AM"

    input_data_1 = 37800
    expected_output_1 = "10:30 AM"

    restaurant = RestaurantHours({})

    assert restaurant.unix_to_readable_time(input_data) == expected_output
    assert restaurant.unix_to_readable_time(input_data_1) == expected_output_1


def test_normalize_hours():
    input_data = {
        "monday": [],
        "tuesday": [],
        "wednesday": [],
        "thursday": [],
        "friday": [{"type": "open", "value": 64800}],  # 6 PM
        "saturday": [
            {"type": "close", "value": 3600},  # 1 AM
            {"type": "open", "value": 32400},  # 9 AM
            {"type": "close", "value": 39600},  # 11 AM
            {"type": "open", "value": 57600},  # 4 PM
            {"type": "close", "value": 82800},  # 11 PM
        ],
        "sunday": [],
    }

    expected_output = {
        "monday": [],
        "tuesday": [],
        "wednesday": [],
        "thursday": [],
        "friday": [{"type": "open", "value": 64800}, {"type": "close", "value": 3600}],
        "saturday": [
            {"type": "open", "value": 32400},  # 9 AM
            {"type": "close", "value": 39600},  # 11 AM
            {"type": "open", "value": 57600},  # 4 PM
            {"type": "close", "value": 82800},  # 11 PM
        ],
        "sunday": [],
    }

    restaurant = RestaurantHours(input_data)

    assert restaurant.normalize_hours() == expected_output
