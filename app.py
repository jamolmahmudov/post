from flask import Flask, request
import telegram

TOKEN = "6904974035:AAFjfkFsHnygmw12JS4CdQFcjxUHvWwy624"
chat_id = '6897251542'
bot = telegram.Bot(TOKEN)

app = Flask(__name__)

@app.route("/")
def main():
    data = request.get_json()
    print(data)
    bot.send_message(chat_id= chat_id, text = "ok jnja")
    return "main"
if __name__=="__main__":
    app.run(debug=True)