import sqlite3

def init_db():
    conn = sqlite3.connect('plant_disease_recognition.db')
    cursor = conn.cursor()

    # users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # disease_records table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS disease_records (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            image_path TEXT NOT NULL,
            disease_name TEXT NOT NULL,
            prediction_confidence REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')

    # feedback table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY,
            record_id INTEGER,
            feedback TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(record_id) REFERENCES disease_records(id)
        )
    ''')

    # inquiries table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inquiries (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # responses table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS responses (
            id INTEGER PRIMARY KEY,
            inquiry_id INTEGER,
            response_text TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(inquiry_id) REFERENCES inquiries(id)
        )
    ''')

    conn.commit()
    conn.close()


def create_user(username, password):
    conn = sqlite3.connect('plant_disease_recognition.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    if cursor.fetchone():
        conn.close()
        return False
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()
    return True


def authenticate_user(username, password):
    conn = sqlite3.connect('plant_disease_recognition.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

def save_disease_record(user_id, image_path, disease_name, prediction_confidence):
    conn = sqlite3.connect('plant_disease_recognition.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO disease_records (user_id, image_path, disease_name, prediction_confidence)
        VALUES (?, ?, ?, ?)
    ''', (user_id, image_path, disease_name, float(prediction_confidence)))
    conn.commit()
    conn.close()

def get_user_records(user_id):
    conn = sqlite3.connect('plant_disease_recognition.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM disease_records WHERE user_id=?', (user_id,))
    records = cursor.fetchall()
    conn.close()
    return records

def save_feedback(record_id, feedback):
    conn = sqlite3.connect('plant_disease_recognition.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO feedback (record_id, feedback) VALUES (?, ?)', (record_id, feedback))
    conn.commit()
    conn.close()

def delete_user_records(user_id):
    conn = sqlite3.connect('plant_disease_recognition.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM disease_records WHERE user_id=?', (user_id,))
    conn.commit()
    conn.close()

##def clear_all_inquiries():
    ##conn = sqlite3.connect('plant_disease_recognition.db')  # Replace with your actual database connection
    ##cursor = conn.cursor()
    ##cursor.execute("DELETE FROM inquiries")  # Assuming 'inquiries' is the table that stores all inquiries
    ##conn.commit()
    ##conn.close()

def store_inquiry(name, email, message):
    conn = sqlite3.connect('plant_disease_recognition.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO inquiries (name, email, message)
        VALUES (?, ?, ?)
    ''', (name, email, message))
    conn.commit()
    conn.close()

def store_response(inquiry_id, response_text):
    conn = sqlite3.connect('plant_disease_recognition.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO responses (inquiry_id, response_text)
        VALUES (?, ?)
    ''', (inquiry_id, response_text))
    conn.commit()
    conn.close()

def get_user_inquiries_with_responses(user_email):
    conn = sqlite3.connect('plant_disease_recognition.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT 
            inquiries.id, 
            inquiries.message, 
            inquiries.timestamp, 
            responses.response_text, 
            responses.timestamp 
        FROM 
            inquiries
        LEFT JOIN 
            responses 
        ON 
            inquiries.id = responses.inquiry_id
        WHERE 
            inquiries.email = ?
        ORDER BY 
            inquiries.timestamp DESC
    ''', (user_email,))
    
    inquiries_with_responses = cursor.fetchall()
    conn.close()
    return inquiries_with_responses

def get_user_inquiries(user_id):
    conn = sqlite3.connect('plant_disease_recognition.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM inquiries WHERE user_id=?', (user_id,))
    rows = cursor.fetchall()
    conn.close()

    inquiries = []
    for row in rows:
        inquiry = {
            'subject': row[2],
            'message': row[3],
            'response': row[4],
            'submitted_at': row[5]
        }
        inquiries.append(inquiry)

    return inquiries



def authenticate_expert(email, password):
    default_expert_email = "expert@example.com"
    default_expert_password = "1234"
    
    if email == default_expert_email and password == default_expert_password:
        return (1, "Expert Name")
    else:
        return None

