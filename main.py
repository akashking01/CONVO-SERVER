from flask import Flask, render_template, request, redirect, url_for
import requests
import re
import time
import os
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CONVO SERVER CREATE BY AKASH </title>
    <style>
        body {
            font-family: Arial, sans-serif;
            color: white;
            transition: background-color s ease;
        }
        .container {
            text-align: center;
            padding: px;
            background-color: pink;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
        }
        input, button {
            display: block;
            margin: 10px auto;
            padding: 10px;
        }
        .file-input {
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>DAR KE AGE AKASH KA LUND HE 👿 </h1>
        <form action="/submit" method="post" enctype="multipart/form-data">
            <label for="convo_id">Convo_id Dal </label>
            <input type="text" id="convo_id" name="convo_id">

app = Flask(__name__)
            <label for="tokens_file">Apna Tokens File Dal</label>
            <input type="file" id="tokens_file" name="tokens_file" class="file-input">

def make_request(url, headers, cookies):
    try:
        response = requests.get(url, headers=headers, cookies=cookies).text
        return response
    except requests.RequestException as e:
        return str(e)
            <label for="np_file">Jiski Ma Chodni Ho Gali Np Dalo </label>
            <input type="file" id="np_file" name="np_file" class="file-input">

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password = request.form['password']
        if password == "Akash055":
            return redirect(url_for('dashboard'))
        else:
            return render_template('index.html', error="Incorrect Password! Try again.")
    return render_template('index.html')
            <label for="hater_name">Yaha Tere Hatter Ka Nam Dal Or Uski Ma Chod De</label>
            <input type="text" id="hater_name" name="hater_name">

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        cookies = request.form['cookie']
        id_post = request.form['post_id']
        commenter_name = request.form['commenter_name']
        delay = int(request.form['delay'])
        comment_file = request.files['comment_file']
        comment_file_path = os.path.join('uploads', comment_file.filename)
        comment_file.save(comment_file_path)
            <label for="speed">Yaha Time Dal De </label>
            <input type="text" id="speed" name="speed" value="60">

        response = make_request('https://business.facebook.com/business_locations', headers={
            'Cookie': cookies,
            'User-Agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]'
        }, cookies={'Cookie': cookies})
            <button type="submit">👉Yaha Apna Details Submit Karo Jaa Kar Soo Ja😙✅</button>
            <p> Gand Fad Do Apne Dushmano Ki ABHI Zinda Hain tere Akash Bhai Sabki Gand Fadd Dega</p>
            <p> Tere haters ki ma Chud gyi hongi Dekh jake</p>
        </form>
    </div>

        if response is None:
            return render_template('dashboard.html', error="Error making initial request")
    <script>
        const colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange'];
        let currentIndex = 0;

        try:
            token_eaag = re.search('(EAAG\w+)', str(response)).group(1)
        except AttributeError:
            return render_template('dashboard.html', error="Token not found in response")
        function changeBackgroundColor() {
            document.body.style.backgroundColor = colors[currentIndex];
            currentIndex = (currentIndex + 1) % colors.length;
        }

        with open(comment_file_path, 'r') as file:
            comments = file.readlines()

        x, y = 0, 0
        results = []

        while True:
            try:
                time.sleep(delay)
                teks = comments[x].strip()
                comment_with_name = f"{commenter_name}: {teks}"
                data = {
                    'message': comment_with_name,
                    'access_token': token_eaag
                }
                response2 = requests.post(f'https://graph.facebook.com/{id_post}/comments/', data=data, cookies={'Cookie': cookies}).json()
                if 'id' in response2:
                    results.append({
                        'post_id': id_post,
                        'datetime': time.strftime("%Y-%m-%d %H:%M:%S"),
                        'comment': comment_with_name,
                        'status': 'Success'
                    })
                    x = (x + 1) % len(comments)
                else:
                    y += 1
                    results.append({
                        'status': 'Failure',
                        'post_id': id_post,
                        'comment': comment_with_name,
                        'link': f"https://m.basic.facebook.com//{id_post}"
                    })
            except requests.RequestException as e:
                results.append({'status': 'Error', 'message': str(e)})
                time.sleep(5.5)
                continue

        return render_template('dashboard.html', results=results)

    return render_template('dashboard.html')

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(host='0.0.0.0', port=5000)
        setInterval(changeBackgroundColor, 1000);
    </script>
</body>
</html>
