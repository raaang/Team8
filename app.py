from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.irl8uln.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/member/join_form')
def join_from():
    return render_template('/member/join_form.html')

@app.route('/member/join', methods=['POST'])
def join():
    id = request.form['id_give']
    name = request.form['name_give']
    birthday = request.form['birthday_give']
    pw = request.form['pw_give']

    birthyear = int(birthday.split('.')[0])

    print(id, name, birthday, birthyear, pw)

    if(birthyear < 2003):
        doc = {
            'id': id,
            'name': name,
            'birthday': birthday,
            'pw': pw
        }
        db.member.insert_one(doc)

        return jsonify({'msg': '회원가입 완료!'})

    return jsonify({'msg': '미성년자입니다. 회원가입이 불가능합니다.'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)