@app.route('/api/menu/create', methods=['POST'])
def create_menu():
    return "Меню створено"

@app.route('/api/menu/get', methods=['GET'])
def get_menu():
    return "Отримано меню"

@app.route('/api/menu/delete', methods=['DELETE'])
def delete_menu():
    return "Меню видалено"

@app.route('/api/menu/clone', methods=['POST'])
def clone_menu():
    return "Меню скопійовано"

@app.route('/api/menu/update', methods=['PUT'])
def update_menu():
    return "Меню оновлено"

