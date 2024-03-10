from flask import Flask, render_template 
import random 


app = Flask(__name__)

@app.route('/')
def index():
    gifts = [
        {
            'title': "Lì xì vui vẻ",
            'content': "Chúc bạn một năm mới ngập tràn niềm vui!!",
            'url': 'https://inkythuatso.com/uploads/thumbnails/800/2023/03/1-hinh-anh-ngay-moi-hanh-phuc-sieu-cute-inkythuatso-09-13-35-50.jpg',
        },
        {
            'title': "Lì xì tài lộc",
            'content': "Năm mới thật nhiều tài lộc, vạn sự như Ý!!!",
            'url': 'https://didongviet.vn/dchannel/wp-content/uploads/2023/11/New-Project-1-30-576x1024.jpg'
        },
        {
            'title': "Lì xì may mắn",
            'content': "Chúc bạn một năm mới thật nhiều may mắn!!",
            'url': 'https://bizweb.dktcdn.net/100/438/408/files/hinh-nen-may-man-yodyvn64-33ebf1d8-2266-4d6a-985a-9b3ce65111ba.jpg?v=1684910747989',
        },
        {
            'title': "Lì xì sức khỏe",
            'content': "Sức khỏe dồi dào, tiền vào ào ào",
            'url': "https://xwatch.vn/upload_images/images/2023/03/10/4-anh-anime-doraemon.jpg"
        }
    ]
    random.shuffle(gifts)
    return render_template('index.html', gifts=gifts)


@app.route('/detail')
def receiver_gift_page():
    return render_template('detail.html')


if __name__ == '__main__':
    app.run(debug=True)
