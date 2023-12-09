from flask import Flask, request, render_template
from services.db_service import DBService
app = Flask(__name__)


service = DBService()
@app.route("/")
def render_them():
    return render_template(f"list_example.html")


@app.route("/write_new_item", methods=["post"])
def write_new_item():
    my_json_data = request.json
    if "value" not in my_json_data:
        return "Failure"
    id = service.new_item(my_json_data["value"])
    return {"id":id}
    
@app.route("/list_items")
def read_list():
    return service.read_data()
@app.route("/filter_items")
def filter_set():
    args = request.args["search_for"]
    return service.filter_data(args)
@app.route("/delete_item", methods=["DELETE"])
def delete_item():
    my_json_data = request.json
    print(my_json_data)
    service.delete_item(my_json_data["id"])
    return {"status":"success"}

@app.route("/update_item", methods=["PUT"])
def update_list():
    my_json_data = request.json
    service.update_item(id=my_json_data["id"],value=my_json_data["value"])
    return {"status":"success"}