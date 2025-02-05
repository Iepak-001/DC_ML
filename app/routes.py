# app/routes.py
from flask import Blueprint, request, jsonify
from app.model import predict_and_allocate

# Create a Blueprint named 'routes'
routes = Blueprint('routes', __name__)

@routes.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from the request
        input_data = request.get_json()

        # If a list is received, take the first item
        if isinstance(input_data, list) and len(input_data) > 0:
            input_data = input_data[0]

        # Ensure input_data is a dictionary
        if not isinstance(input_data, dict):
            raise TypeError(f"Expected a dictionary but got {type(input_data)}")

        # Get prediction and bandwidth allocation
        predicted_segment, allocated_bandwidth = predict_and_allocate(input_data)
        
        return jsonify({
            "predicted_segment": predicted_segment,
            "allocated_bandwidth": allocated_bandwidth
        })

    except Exception as e:
        return jsonify({"error": str(e)})
