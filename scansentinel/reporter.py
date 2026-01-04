import json
import csv
import os

class Reporter:
  @staticmethod
  def export_json(data, filename="export.json"):
    try:
      with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
        print(f"✅ Data succesvol geexporteerd naar {filename}")
    except Exception as e:
      print(f"⚠️ Fout bij het exporteren JSON: {e}")