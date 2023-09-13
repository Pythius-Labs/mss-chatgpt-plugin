import json
from flask import Flask, request, send_from_directory
import requests
from quart import request, jsonify

_BASE_URL = "https://webservices.mss1.com/MSSSubconAPI"
_AUTH_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoibWVsbGlzIiwibmFtZWlkIjoiNjU3MDkiLCJuYmYiOjE2OTQ1NTIwMzgsImV4cCI6MTY5NDYzODQzOCwiaWF0IjoxNjk0NTUyMDM4LCJpc3MiOiJNU1MifQ.AP7LBO164u950VbizVBE6Cm9fy-2ESFiuWDphqxxAKs"
headers = {'Authorization':f'Bearer {_AUTH_TOKEN}','accept':'application/json','Content-Type':'application/json'}


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/.well_known/ai_plugin.json')
def serve_mss_api_plugin():
    return send_from_directory('.', 'mss-api-plugin.json')

@app.route('/openapi.yaml')
def serve_openapi_yaml():
    return send_from_directory('.', 'mss-api-plugin.yaml')   

@app.get('/contacts')
async def _contacts_get():
    response = requests.get(f'{_BASE_URL}/contacts', headers=headers)
    return jsonify(response.json()), response.status_code

@app.get('/damage_claim')
async def _damage_claim_get():
    response = requests.get(f'{_BASE_URL}/damage_claim', headers=headers)
    return jsonify(response.json()), response.status_code

@app.get('/damage_claim/<string:job_num>')
async def _damage_claim_job_num_get(job_num):
    response = requests.get(f'{_BASE_URL}/damage_claim/{job_num}', headers=headers)
    return jsonify(response.json()), response.status_code

@app.get('/damage_claim/<string:job_num>/note')
async def _damage_claim_job_num_note_get(job_num):
    response = requests.get(f'{_BASE_URL}/damage_claim/{job_num}/note', headers=headers)
    return jsonify(response.json()), response.status_code

@app.get('/damage_claim/<string:job_num>/picture')
async def _damage_claim_job_num_picture_get(job_num):
    response = requests.get(f'{_BASE_URL}/damage_claim/{job_num}/picture', headers=headers)
    return jsonify(response.json()), response.status_code

@app.get('/damage_claim/<string:job_num>/service')
async def _damage_claim_job_num_service_get(job_num):
    response = requests.get(f'{_BASE_URL}/damage_claim/{job_num}/service', headers=headers)
    return jsonify(response.json()), response.status_code

@app.get('/jobs/<string:job_id>/msscontacts')
async def _jobs_job_id_msscontacts_get(job_id):
    response = requests.get(f'{_BASE_URL}/jobs/{job_id}/msscontacts', headers=headers)
    return jsonify(response.json()), response.status_code

@app.get('/jobs/<string:job_id>/crates')
async def _jobs_job_id_crates_get(job_id):
    response = requests.get(f'{_BASE_URL}/jobs/{job_id}/crates', headers=headers)
    return jsonify(response.json()), response.status_code

@app.get('/jobs/<string:job_id>/doc')
async def _jobs_job_id_doc_get(job_id):
    response = requests.get(f'{_BASE_URL}/jobs/{job_id}/doc', headers=headers)
    return jsonify(response.json()), response.status_code

@app.get('/jobs/<string:job_id>/notes')
async def _jobs_job_id_notes_get(job_id):
    response = requests.get(f'{_BASE_URL}/jobs/{job_id}/notes', headers=headers)
    return jsonify(response.json()), response.status_code

@app.get('/jobs/<string:job_id>/phones')
async def _jobs_job_id_phones_get(job_id):
    response = requests.get(f'{_BASE_URL}/jobs/{job_id}/phones', headers=headers)
    return jsonify(response.json()), response.status_code

@app.get('/jobs/<string:job_id>/pictures')
async def _jobs_job_id_pictures_get(job_id):
    response = requests.get(f'{_BASE_URL}/jobs/{job_id}/pictures', headers=headers)
    return jsonify(response.json()), response.status_code

@app.get('/jobs')
async def _jobs_get():
    response = requests.get(f'{_BASE_URL}/jobs', headers=headers)
    return jsonify(response.json()), response.status_code

@app.get('/jobs/<string:job_id>')
async def _jobs_job_id_get(job_id):
    response = requests.get(f'{_BASE_URL}/jobs/{job_id}', headers=headers)
    return jsonify(response.json()), response.status_code

@app.get('/job-search')
async def _jobsearch_get():
    response = requests.get(f'{_BASE_URL}/job-search', headers=headers)
    return jsonify(response.json()), response.status_code

@app.get('/jobs/<string:job_id>/services')
async def _jobs_job_id_services_get(job_id):
    response = requests.get(f'{_BASE_URL}/jobs/{job_id}/services', headers=headers)
    return jsonify(response.json()), response.status_code

@app.get('/new-jobs')
async def _newjobs_get():
    response = requests.get(f'{_BASE_URL}/new-jobs', headers=headers)
    return jsonify(response.json()), response.status_code

@app.get('/schedule_status_subcon')
async def _schedule_status_subcon_get():
    response = requests.get(f'{_BASE_URL}/schedule_status_subcon', headers=headers)
    return jsonify(response.json()), response.status_code

@app.get('/updated-jobs')
async def _updatedjobs_get():
    response = requests.get(f'{_BASE_URL}/updated-jobs', headers=headers)
    return jsonify(response.json()), response.status_code


def main():
    #import uvicorn
    #uvicorn.run("main:app", host="localhost", port=8000)
    with app.app_context():
        app.run(debug=True, host="0.0.0.0", port=5003)

if __name__ == "__main__":
    main()