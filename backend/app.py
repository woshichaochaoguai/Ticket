from flask import Flask, request, jsonify
from flask_cors import CORS
from .gemini_client import GeminiClient
from .knowledge_base import KnowledgeBase
import os

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

try:
    gemini = GeminiClient()
    kb = KnowledgeBase(directory='knowledge_files')
except ValueError as e:
    print(f"Initialization Error: {e}")
    gemini = None
    kb = None


@app.route('/api/status', methods=['GET'])
def status():
    if gemini is None:
        return jsonify({"status": "error", "message": "Gemini client not initialized. Check GOOGLE_API_KEY."}), 500
    return jsonify({
        "status": "ok",
        "message": "Backend is running.",
        "kb_items": len(kb.documents) if kb else 0
    })


@app.route('/api/process', methods=['POST'])
def process_ticket():
    if gemini is None:
        return jsonify({"error": "Server not configured correctly. Check API key."}), 500

    data = request.json
    ticket_text = data.get('ticket')

    if not ticket_text:
        return jsonify({"error": "Ticket text is required."}), 400

    summary = gemini.summarize_ticket(ticket_text)
    relevant_kbs = kb.search(summary, top_k=5)
    analysis = gemini.analyze_ticket(summary, relevant_kbs)
    english_reply = gemini.generate_english_reply(analysis)

    return jsonify({
        "summary": summary,
        "knowledge_base_results": relevant_kbs,
        "analysis": analysis,
        "english_reply": english_reply
    })


@app.route('/api/kb/sync', methods=['POST'])
def sync_kb():
    if kb:
        kb.sync()
        return jsonify({"message": "Knowledge base synced successfully.", "item_count": len(kb.documents)})
    return jsonify({"error": "Knowledge base not initialized."}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5001)
