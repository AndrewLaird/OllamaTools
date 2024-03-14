from flask import Flask, request, jsonify
import subprocess
import json

app = Flask(__name__)

@app.route('/run_codellama', methods=['POST'])
def run_codellama():
    data = request.json
    messages = data.get('messages', '')  # Extract 'messages' from the request
    model = data.get('model', '')       # Extract 'model' from the request

    # Run the ollama command with messages and model
    try:
        result = subprocess.run(
            ['ollama', 'run', 'codellama', '--model', model, '--messages', json.dumps(messages)],
            capture_output=True, text=True, check=True
        )
    except subprocess.CalledProcessError as e:
        # Handle the case where the subprocess fails
        return jsonify({'error': 'Ollama subprocess failed', 'details': str(e)}), 500

    output = result.stdout
    if output:
        try:
            # Assuming the output is JSON formatted
            output_json = json.loads(output)
            return jsonify({'output': output_json})
        except json.JSONDecodeError:
            # Handle non-JSON output
            return jsonify({'error': 'Invalid JSON output', 'raw_output': output}), 500
    else:
        # Handle the case where there is no output
        return jsonify({'error': 'No output from Ollama'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8085)
