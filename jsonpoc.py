import json
import base64

thegame = {
    'levels':
    {
        'level1': {
            'header' : 'Welcome to Level 1',
            'question' : 'Find the hidden message in following image <br><br><img src="/static/l1_1.jpg" alt="4 handsome guys" style="width: 550px; height: auto;">',
            'answer' : 'December2026',
            'hint' : 'Look at the bright side of life ☀️☀️',
            'contents' : {
                'l1_1' : {
                    'mime_type': 'image/jpg',
                    'data': 'base64_encoded_image_data_here'
                }
            }
        }, 
        'level2': {
            'header' : 'Welcome to Level 2',
            'question' : 'What is 3 + 3?',
            'answer' : '6',
            'hint' : 'It is the same as 3 * 2',
        }
    },
    'css': {
        'style.css': 'base64_encoded_css_data_here'
    }

}


with open('static/style.css', 'r') as f:
    css_data = f.read()
    ## base64 encode the css data
    css_data = base64.b64encode(css_data.encode('utf-8')).decode('utf-8')
    thegame['css']['style.css'] = css_data


with open('./static/l3_3.jpg', 'rb') as f:
    image_data = f.read()
    ## base64 encode the image data
    image_data = base64.b64encode(image_data).decode('utf-8')
    thegame['levels']['level1']['contents'][1]['data'] = image_data

thegame['levels']['level1']['contents'][1]['mime_type'] = 'image/jpg'


with open('./levels/game_data.json', 'w') as f:
    json.dump(thegame, f, indent=4) 


level = 2

print(len(thegame['levels']))
print(thegame['levels'][f'level{level}']['hint'])