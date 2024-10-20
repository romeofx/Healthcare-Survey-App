{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "154cd998-6bb5-4403-b192-ad366d531ae0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on all addresses (0.0.0.0)\n",
      " * Running on http://127.0.0.1:5000\n",
      " * Running on http://172.20.10.2:5000\n",
      "Press CTRL+C to quit\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, render_template, request, redirect\n",
    "from flask_pymongo import PyMongo  \n",
    "import threading\n",
    "\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "# MongoDB configuration\n",
    "app.config[\"MONGO_DBNAME\"] = 'survey_db'\n",
    "app.config[\"MONGO_URI\"] = 'mongodb+srv://survey_db:plpIDaoxlIEGF8CO@healthcare-application0.ne1an.mongodb.net/'\n",
    "\n",
    "\n",
    "\n",
    "# Initialize PyMongo\n",
    "mongo = PyMongo(app)\n",
    "\n",
    "@app.route('/', methods=['GET', 'POST'])\n",
    "def index():\n",
    "    if request.method == 'POST':\n",
    "        # Collect form data\n",
    "        age = request.form['age']\n",
    "        gender = request.form['gender']\n",
    "        total_income = request.form['total_income']\n",
    "        expenses = {\n",
    "            'utilities': request.form.get('utilities', 0),\n",
    "            'entertainment': request.form.get('entertainment', 0),\n",
    "            'school_fees': request.form.get('school_fees', 0),\n",
    "            'shopping': request.form.get('shopping', 0),\n",
    "            'healthcare': request.form.get('healthcare', 0)\n",
    "        }\n",
    "\n",
    "        # Store the data in MongoDB\n",
    "        participant_data = {\n",
    "            'age': age,\n",
    "            'gender': gender,\n",
    "            'total_income': total_income,\n",
    "            'expenses': expenses\n",
    "        }\n",
    "        mongo.db.participants.insert_one(participant_data)\n",
    "        return redirect('/success')\n",
    "\n",
    "    return '''\n",
    "    <form method=\"POST\">\n",
    "        Age: <input type=\"number\" name=\"age\"><br>\n",
    "        Gender: <input type=\"text\" name=\"gender\"><br>\n",
    "        Total Income: <input type=\"number\" name=\"total_income\"><br>\n",
    "        Utilities: <input type=\"number\" name=\"utilities\"><br>\n",
    "        Entertainment: <input type=\"number\" name=\"entertainment\"><br>\n",
    "        School Fees: <input type=\"number\" name=\"school_fees\"><br>\n",
    "        Shopping: <input type=\"number\" name=\"shopping\"><br>\n",
    "        Healthcare: <input type=\"number\" name=\"healthcare\"><br>\n",
    "        <input type=\"submit\">\n",
    "    </form>\n",
    "    '''\n",
    "@app.route('/success')\n",
    "def success():\n",
    "    return 'Data successfully submitted!'\n",
    "\n",
    "# Running Flask in a separate thread to keep Jupyter notebook active\n",
    "def run_flask():\n",
    "     app.run(host='0.0.0.0', port=5000)\n",
    "\n",
    "\n",
    "threading.Thread(target=run_flask).start()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2ead301c-6e22-4a74-9928-919cf742b1dc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
