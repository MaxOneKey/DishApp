@app.route('/api/dish/create', methods=['POST'])
def create_dish():
    return "Страва створена"

@app.route('/api/dish/get', methods=['GET'])
def get_dish():
    return "Отримано страву"

@app.route('/api/dish/delete', methods=['DELETE'])
def delete_dish():
    return "Страву видалено"

@app.route('/api/dish/clone', methods=['POST'])
def clone_dish():
    return "Страву скопійовано"

@app.route('/api/dish/update',methods=['PUT'])
def update_dish():
    return "Страву оновлено"

@app.route('/api/dish/relate', methods=['POST'])
def relate_dish():
    return "Страва звязана з рецептом"
