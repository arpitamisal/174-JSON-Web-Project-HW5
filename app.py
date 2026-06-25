from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), "truckinglist.json")


def load_data():
    if not os.path.exists(DATA_FILE):
        raise FileNotFoundError("truckinglist.json not found")

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def get_companies_list(data):
    if "Mainline" not in data or "Table" not in data["Mainline"] or "Row" not in data["Mainline"]["Table"]:
        raise KeyError("Invalid JSON structure")
    return data["Mainline"]["Table"]["Row"]


@app.route("/")
def index():
    return """
    <h2>Trucking Company API</h2>
    <p>This is a RESTful API for managing trucking company data.</p>
    <p>Available endpoints:</p>
    <ul>
        <li>GET /companies</li>
        <li>GET /companies/&lt;name&gt;</li>
        <li>POST /companies</li>
        <li>PUT /companies/&lt;name&gt;</li>
        <li>DELETE /companies/&lt;name&gt;</li>
    </ul>
    """


@app.route("/companies", methods=["GET"])
def get_all_companies():
    try:
        data = load_data()
        companies = get_companies_list(data)
        return jsonify(companies), 200
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 500
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON file"}), 500
    except KeyError:
        return jsonify({"error": "Invalid trucking JSON structure"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/companies/<string:name>", methods=["GET"])
def get_company(name):
    try:
        data = load_data()
        companies = get_companies_list(data)

        for company in companies:
            if company.get("Company", "").lower() == name.lower():
                return jsonify(company), 200

        return jsonify({"error": "Company not found"}), 404
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 500
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON file"}), 500
    except KeyError:
        return jsonify({"error": "Invalid trucking JSON structure"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/companies", methods=["POST"])
def add_company():
    try:
        new_company = request.get_json()

        if not new_company:
            return jsonify({"error": "Request body must be valid JSON"}), 400

        required_fields = ["Company", "Services", "Hubs", "Revenue", "HomePage", "Logo"]
        for field in required_fields:
            if field not in new_company:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        data = load_data()
        companies = get_companies_list(data)

        for company in companies:
            if company.get("Company", "").lower() == new_company["Company"].lower():
                return jsonify({"error": "Company already exists"}), 400

        companies.append(new_company)
        save_data(data)

        return jsonify({"message": "Company added successfully", "company": new_company}), 201

    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 500
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON file"}), 500
    except KeyError:
        return jsonify({"error": "Invalid trucking JSON structure"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/companies/<string:name>", methods=["PUT"])
def update_company(name):
    try:
        update_data = request.get_json()

        if not update_data:
            return jsonify({"error": "Request body must be valid JSON"}), 400

        data = load_data()
        companies = get_companies_list(data)

        for company in companies:
            if company.get("Company", "").lower() == name.lower():
                company.update(update_data)
                save_data(data)
                return jsonify({"message": "Company updated successfully", "company": company}), 200

        return jsonify({"error": "Company not found"}), 404

    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 500
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON file"}), 500
    except KeyError:
        return jsonify({"error": "Invalid trucking JSON structure"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/companies/<string:name>", methods=["DELETE"])
def delete_company(name):
    try:
        data = load_data()
        companies = get_companies_list(data)

        for i, company in enumerate(companies):
            if company.get("Company", "").lower() == name.lower():
                deleted_company = companies.pop(i)
                save_data(data)
                return jsonify({"message": "Company deleted successfully", "company": deleted_company}), 200

        return jsonify({"error": "Company not found"}), 404

    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 500
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON file"}), 500
    except KeyError:
        return jsonify({"error": "Invalid trucking JSON structure"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400


@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(debug=True)
