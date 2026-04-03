from fastapi import FastAPI, Request

app = FastAPI()

patients = {}

@app.get("/")
@app.head("/")
def root():
    return {"status": "online", "message": "Hospital Management API is running"}

@app.post("/store")
async def store(request: Request):
    body = await request.json()
    patient_id = body.get("patient_id")
    if not patient_id:
        return {"status": "error", "message": "patient_id is required"}
    patients[patient_id] = body
    return {"status": "success", "message": "Patient stored", "data": body}

@app.post("/query")
async def query(request: Request):
    body = await request.json()
    patient_id = body.get("patient_id")
    if not patient_id:
        return {"status": "error", "message": "patient_id is required"}
    patient = patients.get(patient_id)
    if not patient:
        return {"status": "error", "message": "Patient not found"}
    return {"status": "success", "data": patient}

@app.post("/delete")
async def delete(request: Request):
    body = await request.json()
    patient_id = body.get("patient_id")
    if not patient_id:
        return {"status": "error", "message": "patient_id is required"}
    if patient_id not in patients:
        return {"status": "error", "message": "Patient not found"}
    del patients[patient_id]
    return {"status": "success", "message": f"Patient {patient_id} deleted"}

@app.post("/modify")
async def modify(request: Request):
    body = await request.json()
    patient_id = body.get("patient_id")
    if not patient_id:
        return {"status": "error", "message": "patient_id is required"}
    if patient_id not in patients:
        return {"status": "error", "message": "Patient not found"}
    patients[patient_id].update(body)
    return {"status": "success", "message": "Patient updated", "data": patients[patient_id]}
