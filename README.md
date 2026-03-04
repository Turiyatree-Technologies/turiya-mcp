# Public Jobs API

A secure 4-endpoint API system that allows controlled public distribution of active job listings using secret API keys.

---

## 🚀 What Was Built

A Frappe-based external API layer that:

* Generates and manages secure external API keys
* Allows partners to fetch active job listings
* Restricts access using API key authentication
* Ensures only approved jobs are publicly distributed

---

## 📁 New Files Created

| File                       | Purpose                                             |
| -------------------------- | --------------------------------------------------- |
| `external_api_key.json`    | DocType definition (registered via `bench migrate`) |
| `external_api_key.py`      | Python controller for API key logic                 |
| `external_api/__init__.py` | Module initializer                                  |
| `external_api/api.py`      | Contains all 4 API endpoints                        |

---

## 📌 API Base Path

```
/api/method/top.top_one_backend.external_api.api.
```

---

# 🔐 API Endpoints

---

## 1️⃣ Generate API Key

**Endpoint**

```
POST /api/method/top.top_one_backend.external_api.api.generate_api_key
```

**Authentication**

* Frappe session cookie
  **OR**
* `Authorization: token <api_key>:<api_secret>`

**Request Body**

```json
{
  "key_name": "My Partner Key"
}
```

**Response**

```json
{
  "status": true,
  "id": "EXTKEY.001",
  "api_key": "top_a1b2c3d4...",
  "key_name": "My Partner Key"
}
```

⚠️ **IMPORTANT**

The `api_key` is shown in full only once during creation.
After that, `list_api_keys` will return a masked version.

---

## 2️⃣ Revoke API Key

**Endpoint**

```
DELETE /api/method/top.top_one_backend.external_api.api.revoke_api_key
```

**Authentication**

Same as Generate API Key.

**Permissions**

* Regular users → Can revoke their own keys
* System Managers → Can revoke any key

**Request Body**

```json
{
  "key_id": "EXTKEY.001"
}
```

**Response**

```json
{
  "status": true,
  "message": "API key revoked successfully."
}
```

---

## 3️⃣ List API Keys

**Endpoint**

```
GET /api/method/top.top_one_backend.external_api.api.list_api_keys
```

**Authentication**

Same as above.

**Permissions**

* Regular users → See only their keys
* System Managers → See all keys

**Response**

```json
{
  "status": true,
  "data": [
    {
      "id": "EXTKEY.001",
      "key_name": "My Partner Key",
      "api_key": "top_...d4e5f6",
      "is_active": 1,
      "created_by": "user@example.com",
      "creation": "2026-03-03 ..."
    }
  ]
}
```

🔒 **Security Note**

The `api_key` returned here is masked (only last 6 characters visible).

---

## 4️⃣ Get Public Jobs

**Endpoint**

```
GET /api/method/top.top_one_backend.external_api.api.get_public_jobs
```

**Authentication**

No Frappe login required.

Provide API key via:

* Header:

  ```
  X-API-Key: top_a1b2c3d4...
  ```

  **OR**

* Query parameter:

  ```
  ?api_key=top_a1b2c3d4...
  ```

---

### 🔍 Optional Filter

```
?job_title=engineer
```

* Case-insensitive substring match

---

### ✅ Returns Only Jobs Where

```
status = "ACTIVE"
AND
allow_external_distribution = 1
```

---

### 📦 Response

```json
{
  "status": true,
  "total": 3,
  "data": [
    {
      "id": "JOB001",
      "job_title": "Software Engineer",
      "company_name": "Acme Corp",
      "location": [...],
      "industry": "Technology",
      "job_description": "...",
      "required_skills": [...],
      "preferred_skills": [...],
      "required_experience": [...],
      "required_qualification": [...],
      "posted_on": "2026-03-01 ...",
      "expires_on": "2026-04-01 ...",
      "application_channels": [...]
    }
  ]
}
```

---

# 🧪 Quick cURL Examples

### Generate API Key

```bash
curl -X POST \
  -H "Authorization: token YOUR_API_KEY:YOUR_API_SECRET" \
  -H "Content-Type: application/json" \
  -d '{"key_name": "Partner Feed"}' \
  https://dev-app.turiyaskills.co/api/method/top.top_one_backend.external_api.api.generate_api_key
```

---

### Fetch All Active Public Jobs

```bash
curl -H "X-API-Key: top_<your_key>" \
  https://dev-app.turiyaskills.co/api/method/top.top_one_backend.external_api.api.get_public_jobs
```

---

### Filter by Job Title

```bash
curl -H "X-API-Key: top_<your_key>" \
  "https://dev-app.turiyaskills.co/api/method/top.top_one_backend.external_api.api.get_public_jobs?job_title=engineer"
```

---

# 🌍 Making a Job Publicly Distributable

In the **Job Description DocType**, ensure:

* `Status = ACTIVE`
* `Allow External Distribution = ✅ checked`

Only jobs matching **both conditions** will appear in the public feed.

---

# 🔒 Security Design

* API keys are securely generated
* Keys are masked when listed
* Access control based on user role
* Public endpoint strictly filtered to approved jobs only

---

# 📦 Summary

This API system enables secure third-party job distribution while maintaining:

* Controlled access
* Role-based key management
* Explicit job approval workflow
* Clean and scalable architecture

---

If you'd like, I can also generate a version formatted specifically for GitHub (with badges, table of contents, etc.).
