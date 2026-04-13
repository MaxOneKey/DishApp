@app.route('/api/plan/create', methods=['POST'])
def create_plan():
    return "План створено"

@app.route('/api/plan/get', methods=['GET'])
def get_plan():
    return "Отримано план"

@app.route('/api/plan/delete', methods=['DELETE'])
def delete_plan():
    return "План видалено"

@app.route('/api/plan/clone', methods=['POST'])
def clone_plan():
    return "План скопійовано"

@app.route('/api/plan/update', methods=['PUT'])
def update_plan():
    return "План оновлено"

@app.route('/api/plan/relate', methods=['POST'])
def relate_plan():
    return "План звязано з іншим планом"


