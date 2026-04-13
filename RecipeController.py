@app.route('/api/recipe/create', methods=['POST'])
def create_recipe():
    return "Рецепт створено"

@app.route('/api/recipe/get', methods=['GET'])
def get_recipe():
    return "Отримано рецепт"

@app.route('/api/recipe/delete', methods=['DELETE'])
def delete_recipe():
    return "Рецепт видалено"

@app.route('/api/recipe/clone', methods=['POST'])
def clone_recipe():
    return "Рецепт скопійовано"

@app.route('/api/recipe/update', methods=['PUT'])
def update_recipe():
    return "Рецепт оновлено"

@app.route('/api/recipe/relate', methods=['POST'])
def relate_recipe():
    return "Рецепт звязано зі стравою"
