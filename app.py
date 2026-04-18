from flask import Flask, render_template, jsonify

app = Flask(__name__)

# তোর ২৬টি লেভেলের ডাটা
COURSE_DATA = {
    1: {"title": "লেভেল ১: ফিশিং অ্যাটাক", "study": "ফিশিং হলো সাইবার জগতের বড় জালিয়াতি। হ্যাকাররা নকল লিঙ্ক পাঠিয়ে আপনার পাসওয়ার্ড চুরি করে।", "quiz": "হ্যাকাররা সাধারণত ভুয়া লগইন পেজ কেন তৈরি করে?", "options": ["আপডেট করতে", "তথ্য চুরি করতে", "স্পিড বাড়াতে"], "ans": "তথ্য চুরি করতে"},
    2: {"title": "লেভেল ২: পাসওয়ার্ডের গুরুত্ব", "study": "সহজ পাসওয়ার্ড সহজেই হ্যাক হয়। পাসওয়ার্ডে বড়-ছোট অক্ষর, সংখ্যা ও স্পেশাল ক্যারেক্টার ব্যবহার করুন।", "quiz": "নিচের কোনটি সবথেকে শক্তিশালী পাসওয়ার্ড?", "options": ["Alamin123", "X7@kL9!p#z2", "11223344"], "ans": "X7@kL9!p#z2"},
    # একইভাবে বাকি লেভেলগুলোও এখানে থাকবে...
    26: {"title": "লেভেল ২৬: আপনি এখন প্রো!", "study": "অভিনন্দন! আপনি সাইবার নিরাপত্তার ২৬টি ধাপ পার করেছেন।", "quiz": "আপনি কি চূড়ান্ত পরীক্ষার জন্য প্রস্তুত?", "options": ["হ্যাঁ, আমি তৈরি!", "না, পরে দেব", "পারব না"], "ans": "হ্যাঁ, আমি তৈরি!"}
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_level/<int:lvl_id>')
def get_level(lvl_id):
    level = COURSE_DATA.get(lvl_id)
    if level: return jsonify(level)
    return jsonify({"error": "Finished"})

app.debug = True
