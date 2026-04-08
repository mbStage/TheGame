import os   
import shutil


game_name = 'the_game'

if not os.path.exists(game_name):
    os.makedirs(game_name)  
else :
    print(f"Directory '{game_name}' already exists. Please choose a different name or remove the existing directory.")
    exit(1)

shutil.copy(f'levels/game_data.json', f'archive/{game_name}/game_data.json')
shutil.copy(f'static/style.css', f'archive/{game_name}/style.css')


for file in os.listdir('static'):
    if file.endswith('.jpg'):
        shutil.move(f'static/{file}', f'archive/{game_name}/{file}')





