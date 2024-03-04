from flask import Flask, render_template, request
import csv

app = Flask(__name__)

def search_exam_center(serial_number):
    with open('seatplan.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if int(row['From']) <= serial_number <= int(row['To']):
                return {
                    'Sl': row['Sl'],
                    'Name of the Exam Centers': row['Name of the Exam Centers'],
                    'Address': row['Address'],
                    'Capacity': row['Capacity']
                }
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        serial_number = request.form['serial_number']
        try:
            serial_number = int(serial_number)
            exam_center = search_exam_center(serial_number)
            if exam_center:
                return render_template('result.html', exam_center=exam_center)
            else:
                return render_template('result.html', error="No exam center found for the given serial number.")
        except ValueError:
            return render_template('result.html', error="Please enter a valid serial number.")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
