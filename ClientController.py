@app.route('/api/user/create', methods=['POST'])
def create_user():
    return "юзера створено"

@app.route('/api/user/getProfile', methods=['GET'])
def get_user():
    return "Отримано профіль користувача"

@app.route('/api/user/delete', methods=['DELETE'])
def delete_user():
    return "юзера видалено"

@app.route('/api/user/login', methods=['POST'])
def login_user():
    return "юзер ввійшов в акаунт"

@app.route('/api/user/logout', methods=['POST'])
def logout_user():
    return "юзер вийшов з акаунту"

@app.route('/api/user/clone', methods=['POST'])
def clone_user():
    return "юзер скопійований"

@app.route('/api/user/update', methods=['PUT'])
def update_user():
    return "юзера оновлено"

@app.route('/api/user/updateProfile', methods=['PUT'])
def update_profile():
    return "профіль юзера оновлено"

@app.route('/api/user/switchAccount', methods=['POST'])
def switch_account():
    return "активний акаунт змінено"
