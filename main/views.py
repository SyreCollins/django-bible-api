import os
import json
from rest_framework.views import APIView
from rest_framework.response import Response

class BibleBookView(APIView):
    def get(self, request, book_name, chapter_number=None, verse_number=None):
        try:
            # Get the directory of the current file
            dir_path = os.path.dirname(os.path.realpath(__file__))
            # Construct the full path to the JSON file
            file_path = os.path.join(dir_path, f'Biblekjv-jsons/{book_name}.json')
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
            if chapter_number:
                data = data['chapters'][chapter_number-1]
                if verse_number:
                    data = data['verses'][verse_number-1]
            return Response(data)
        except:
            return Response({"error": "Book name, chapter or verse probably not available."})
