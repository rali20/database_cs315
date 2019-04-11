import sqlite3
from flask import Flask, render_template, request

conn = sqlite3.connect('hospital.db')
with open("../queries.sql") as f :
  queries = f.read()
  conn.executescript(queries)
