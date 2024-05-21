from typing import Any, Literal
from flask import Flask, request, jsonify
from flask.wrappers import Response

from .schemas import OpeningHoursInput
from .restaurant_hours import RestaurantHours

app = Flask(__name__)


@app.route("/format_hours", methods=["POST"])
def format_hours() -> tuple[Response, Literal[200]] | tuple[Response, Literal[400]]:
    try:
        data: Any | None = request.get_json()
        hours_input: OpeningHoursInput = OpeningHoursInput.parse_obj(data)

        restaurant = RestaurantHours(hours_input.dict())
        readable_hours: str = restaurant.format_opening_hours()

        return jsonify({"readable_hours": readable_hours}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
