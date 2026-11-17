# MongoDB Atlas Configuration and Student Record Storage Using Express.js

[![Node.js](https://img.shields.io/badge/Node.js-v20%2B-green.svg)](https://nodejs.org/)
[![Express.js](https://img.shields.io/badge/Express.js-4.21.2-lightgrey.svg)](https://expressjs.com/)
[![MongoDB Atlas](https://img.shields.io/badge/MongoDB%20Atlas-Cloud%20M0-00ed64.svg)](https://www.mongodb.com/cloud/atlas)
[![Mongoose ODM](https://img.shields.io/badge/Mongoose-8.9.5-red.svg)](https://mongoosejs.com/)
[![Case Study](https://img.shields.io/badge/Academic-Case%20Study%20Q3-blue.svg)](documentation/Case-Study-Question-3.pdf)
[![Student](https://img.shields.io/badge/Student-P.%20Dinesh%20Kumar-orange.svg)](https://github.com/dineshkumar025)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An enterprise-standard academic case study demonstrating cloud database provisioning on **MongoDB Atlas**, establishing an authenticated, resilient connection to an **Express.js** backend using **Mongoose ODM**, and implementing reliable student record storage and retrieval.

---

## Academic Information & Context

- **Institution:** Anil Neerukonda Institute of Technology & Sciences (ANITS), Visakhapatnam
- **Department:** Department of Computer Science and Engineering
- **Course:** Full-Stack Web Development Lab (Course Code: `23CM4121`)
- **Academic Year:** 2025–2026 (B.Tech III Year I Semester)
- **Assigned Question:** **Question No. 3** (Unit V Worked Case Study Matrix)
- **Student Name:** **P. Dinesh Kumar**
- **Student Roll Number:** **A24126552101**
- **Target Database:** `StudentDB`
- **Target Collection:** `students`

### Official Question Statement

> **Question 3:**  
> *"Explain how MongoDB Atlas is configured to store student records. Describe the steps involved in creating a database, collection and connecting the Express.js backend to the database."*

---

## Table of Contents

1. [Architectural Overview](#architectural-overview)
2. [Technology Stack](#technology-stack)
3. [Step-by-Step MongoDB Atlas Cloud Setup Guide](#step-by-step-mongodb-atlas-cloud-setup-guide)
4. [Anatomy of the MongoDB Atlas SRV Connection URI](#anatomy-of-the-mongodb-atlas-srv-connection-uri)
5. [Express.js Backend Architecture & Implementation](#expressjs-backend-architecture--implementation)
6. [Frontend Demonstration Client](#frontend-demonstration-client)
7. [API Endpoint Reference](#api-endpoint-reference)
8. [Practical Verification & Screenshots](#practical-verification--screenshots)
9. [Quick Start & Windows Execution Guide](#quick-start--windows-execution-guide)
10. [Technical Viva Voce Questions & Answers](#technical-viva-voce-questions--answers)
11. [Formal Case Study PDF Report](#formal-case-study-pdf-report)

---

## Architectural Overview

The application follows a decoupled 3-tier cloud architecture separating the client presentation tier, the application routing/controller tier, and the cloud data persistence tier:

```
[ Browser Client UI ]  <--- HTTP / JSON REST API --->  [ Express.js Backend Server ]  <--- TLS 1.3 / SRV --->  [ MongoDB Atlas Cloud Cluster ]
  • index.html (Form/Table)                              • server.js (Port 5000)                                • AWS ap-south-1 (Mumbai)
  • style.css (Responsive UI)                            • routes/studentRoutes.js                              • 3-Node Multi-AZ Replica Set
  • script.js (Fetch API)                                • controllers/studentController.js                     • Database: StudentDB
                                                         • models/studentModel.js (Schema)                      • Collection: students
                                                         • config/db.js (Mongoose Lifecycle)                    • SCRAM-SHA-256 Authentication
```

![System Architecture](documentation/diagrams/architecture.svg)

---

## Technology Stack

| Layer | Component | Version | Role in Project |
| :--- | :--- | :--- | :--- |
| **Cloud Database** | MongoDB Atlas | Cloud 7.0 Engine | Managed 3-node replica set in AWS Mumbai (`ap-south-1`) hosting `StudentDB.students` |
| **Runtime** | Node.js | v20+ LTS | Asynchronous, non-blocking JavaScript server environment |
| **Backend Framework** | Express.js | 4.21.2 | Minimalist web framework providing REST routing, static hosting, and JSON parsing |
| **Object Data Modeling** | Mongoose ODM | 8.9.5 | Enforces strict student schema, B-Tree indexes, validation regexes, and connection pool |
| **Security & Config** | Dotenv | 16.4.7 | Isolates Atlas credentials and SRV connection strings in `.env` outside source control |
| **Cross-Origin** | CORS | 2.8.5 | Middleware enabling secure cross-origin API communication |
| **Frontend Presentation** | HTML5 / CSS3 / JS | Modern Standards | Responsive demonstration interface with live connection health badge and dynamic table |

---

## Step-by-Step MongoDB Atlas Cloud Setup Guide

Configuring MongoDB Atlas follows a structured 6-step engineering procedure:

![Atlas Configuration Workflow](documentation/diagrams/atlas-config-flow.svg)

### Step 1: Cloud Account Setup & Project Creation
1. Navigate to the MongoDB Cloud management console at [cloud.mongodb.com](https://cloud.mongodb.com/).
2. Authenticate or create an institutional account.
3. Create a dedicated Organization (e.g. `ANITS-CSE`) and initialize a new Project named `Student-Records-Q3`. Projects provide logical isolation for database clusters, alerting, and access lists.

### Step 2: Deploy an M0 Shared Replica Set Cluster
1. Within the project dashboard, click **"Build a Database"**.
2. Select the **M0 Shared Free Sandbox** tier (512 MB storage, shared vCPUs).
3. Select Cloud Provider **AWS** and Region **Mumbai (`ap-south-1`)** to minimize network latency from Indian campus networks.
4. Name the cluster **`Cluster0`** and click **"Create Deployment"**. Atlas provisions a 3-node replica set across availability zones within 1–3 minutes.

### Step 3: Configure Database User Security (SCRAM-SHA-256)
1. In the Atlas left navigation menu, go to **Security > Database Access**.
2. Click **"Add New Database User"**.
3. Choose **Password Authentication** (SCRAM-SHA-256).
4. Enter username: `dinesh_admin`.
5. Enter a strong alphanumeric password (e.g., `DineshAtlas#2026`).
6. Under **Database User Privileges**, select the built-in role **"Read and write to any database"** (`readWriteAnyDatabase@admin`).
7. Click **"Add User"** to commit credentials.

### Step 4: Configure Network Access & IP Allowlisting
1. In the Atlas left navigation menu, go to **Security > Network Access**.
2. Click **"Add IP Access List Entry"**.
3. Select **"Allow Access from Anywhere"** (`0.0.0.0/0`) for dynamic lab and local development environments.
4. Set description: `Development allowlist for Express server`.
5. Click **"Confirm"**. The firewall rule activates within seconds.

### Step 5: Create Database (`StudentDB`) & Collection (`students`)
1. In the Atlas dashboard, navigate to **Deployments > Database**.
2. Click **"Browse Collections"** on the `Cluster0` card.
3. Click **"+ Create Database"**.
4. Enter Database Name: **`StudentDB`**.
5. Enter Collection Name: **`students`**.
6. Click **"Create"**. Atlas initializes the namespace `StudentDB.students` on the primary node.

### Step 6: Extract the DNS SRV Connection URI String
1. Click the **"Connect"** button on the cluster card.
2. Select **"Drivers"** > Driver: **Node.js** > Version: **5.5 or later**.
3. Copy the standard connection URI string template:
   ```env
   MONGODB_URI=mongodb+srv://<username>:<password>@cluster0.abcde.mongodb.net/StudentDB?retryWrites=true&w=majority
   ```
4. Paste the URI into your local `.env` file, substituting your actual user credentials.

---

## Anatomy of the MongoDB Atlas SRV Connection URI

![Connection Flow Diagram](documentation/diagrams/connection-flow.svg)

```
mongodb+srv://dinesh_admin:P@ssw0rd123@cluster0.abcde.mongodb.net/StudentDB?retryWrites=true&w=majority
│             │            │           │                          │         │
│             │            │           │                          │         └─ Write Concern: majority node ack
│             │            │           │                          └─ Target Database Name: StudentDB
│             │            │           └─ Cloud Cluster Hostname (Resolves 3 replica nodes)
│             │            └─ SCRAM-SHA-256 Password
│             └─ Database User with readWrite privileges
└─ DNS Seedlist Protocol: Dynamic node discovery via DNS SRV & TXT records
```

---

## Express.js Backend Architecture & Implementation

The backend follows a modular design pattern:

```
backend/
├── config/
│   └── db.js                 # Database connection & Mongoose event listeners
├── models/
│   └── studentModel.js       # Student Mongoose Schema & B-Tree indexes
├── controllers/
│   └── studentController.js  # REST actions: health, insertStudent, getAllStudents, seed
├── routes/
│   └── studentRoutes.js      # Express route mapping (/health, /students, /students/seed)
├── server.js                 # Server entrypoint, middleware, and bootstrap
└── package.json              # Project dependencies & scripts
```

### 1. Connection Module (`backend/config/db.js`)
Establishes connection to MongoDB Atlas with automated lifecycle event listeners:
```javascript
const mongoose = require('mongoose');

mongoose.connection.on('connected', () => console.log('✅ [MongoDB Atlas] Connected to cluster.'));
mongoose.connection.on('error', (err) => console.error('❌ [MongoDB Atlas] Error:', err.message));
mongoose.connection.on('disconnected', () => console.warn('⚠️  [MongoDB Atlas] Disconnected.'));

const connectDB = async () => {
  const uri = process.env.MONGODB_URI;
  const dbName = process.env.DB_NAME || 'StudentDB';

  try {
    const conn = await mongoose.connect(uri, {
      dbName,
      retryWrites: true,
      w: 'majority',
    });
    console.log(`✅ Connected to database: '${conn.connection.name}' on host: ${conn.connection.host}`);
    return true;
  } catch (error) {
    console.error('❌ Connection failed:', error.message);
    return false;
  }
};
```

### 2. Student Mongoose Schema (`backend/models/studentModel.js`)
Enforces field validation, regex checking, department enums, and unique indexing:
```javascript
const mongoose = require('mongoose');

const studentSchema = new mongoose.Schema(
  {
    studentId: {
      type: String,
      required: [true, 'Student ID is required'],
      unique: true,
      trim: true,
      uppercase: true,
      match: [/^[A-Za-z0-9-]+$/, 'Alphanumeric and hyphens only'],
    },
    name: {
      type: String,
      required: [true, 'Student name is required'],
      trim: true,
      minlength: [2, 'Name must be at least 2 characters long'],
    },
    email: {
      type: String,
      required: [true, 'Student email is required'],
      unique: true,
      trim: true,
      lowercase: true,
      match: [/^\S+@\S+\.\S+$/, 'Valid email address required'],
    },
    department: {
      type: String,
      required: [true, 'Department is required'],
      enum: [
        'Computer Science and Engineering',
        'Information Technology',
        'Electronics and Communication Engineering',
        'Mechanical Engineering',
        'Civil Engineering',
      ],
    },
    year: {
      type: Number,
      required: [true, 'Academic year is required'],
      min: [1, 'Must be between 1 and 4'],
      max: [4, 'Must be between 1 and 4'],
    },
  },
  { timestamps: true }
);

studentSchema.index({ department: 1 });

// Explicitly bind to collection 'students' in database 'StudentDB'
const Student = mongoose.model('Student', studentSchema, 'students');
module.exports = Student;
```

---

## Frontend Demonstration Client

The frontend client demonstrates practical interaction with the cloud database:

![Data Flow Diagram](documentation/diagrams/data-flow.svg)

- **Live Pulse Status Badge:** Continuously queries `GET /api/health` to indicate database connection status, active host, and total record count.
- **Student Record Insertion:** Captures student details and issues a `POST /api/students` request, dynamically updating the table upon HTTP 201 Created.
- **Real-Time Records Table:** Renders student documents retrieved from `GET /api/students` along with the MongoDB 24-character hexadecimal `_id`.
- **Sample Record Seeder:** One-click seeding of 4 verified demonstration records (including student P. Dinesh Kumar, A24126552101).

---

## API Endpoint Reference

| Method | Endpoint | Description | Request Body | Response Code |
| :--- | :--- | :--- | :--- | :--- |
| `GET` | `/api/health` | Server uptime & Atlas connection state | None | `200 OK` |
| `POST` | `/api/students` | Store new student record in MongoDB Atlas | JSON `{ studentId, name, email, department, year }` | `201 Created` |
| `GET` | `/api/students` | Retrieve all student records from Atlas | None | `200 OK` |
| `GET` | `/api/students/:id` | Find student by ObjectId or Student ID | Param `:id` | `200 OK` / `404 Not Found` |
| `POST` | `/api/students/seed` | Populate initial sample student records | None | `201 Created` |

### Sample JSON Request Body (`POST /api/students`)
```json
{
  "studentId": "A24126552101",
  "name": "P. Dinesh Kumar",
  "email": "dinesh.kumar@campus.edu",
  "department": "Computer Science and Engineering",
  "year": 3
}
```

### Sample JSON Response Body (`HTTP 201 Created`)
```json
{
  "success": true,
  "message": "Student record successfully stored in MongoDB Atlas (StudentDB.students)",
  "data": {
    "_id": "6738c821f01a34b21901a001",
    "studentId": "A24126552101",
    "name": "P. Dinesh Kumar",
    "email": "dinesh.kumar@campus.edu",
    "department": "Computer Science and Engineering",
    "year": 3,
    "createdAt": "2026-11-17T06:15:00.000Z",
    "updatedAt": "2026-11-17T06:15:00.000Z"
  }
}
```

---

## Practical Verification & Screenshots

### 1. Terminal Startup & Handshake Output
![Terminal Server Output](documentation/screenshots/express-server-terminal.png)

### 2. MongoDB Atlas Cloud Console & Metrics
![Atlas Dashboard](documentation/screenshots/atlas-dashboard.png)

### 3. Stored Student BSON Documents in Atlas Document Viewer
![Atlas Collections Viewer](documentation/screenshots/atlas-collections-view.png)

### 4. Interactive Frontend Demonstration UI
![UI Demonstration](documentation/screenshots/ui-demonstration.png)

---

## Quick Start & Windows Execution Guide

### Prerequisites
- [Node.js](https://nodejs.org/) v18.0.0 or higher
- [Git](https://git-scm.com/) installed
- Active [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) Account

### Step 1: Clone the Repository
```powershell
git clone https://github.com/dineshkumar025/MongoDB-Atlas-Express-Student-Records.git
cd MongoDB-Atlas-Express-Student-Records
```

### Step 2: Install Backend Dependencies
```powershell
cd backend
npm install
```

### Step 3: Configure Environment Variables
Copy the template `.env.example` into `.env`:
```powershell
cp ..\.env.example .\.env
```
Open `.env` in any text editor and supply your actual Atlas cluster connection URI:
```env
MONGODB_URI=mongodb+srv://dinesh_admin:YourPassword123@cluster0.abcde.mongodb.net/StudentDB?retryWrites=true&w=majority
DB_NAME=StudentDB
PORT=5000
NODE_ENV=development
```

### Step 4: Start the Server
```powershell
npm start
```

### Step 5: Open Demonstration in Browser
Open your browser and navigate to:
```
http://localhost:5000
```
- Click **"🌱 Seed Sample Records"** to populate initial records into MongoDB Atlas.
- Use the form on the left to submit a new student record and verify real-time persistence.

---

## Technical Viva Voce Questions & Answers

<details>
<summary><strong>1. What is MongoDB Atlas and why is it preferred over a local MongoDB instance?</strong></summary>
MongoDB Atlas is a cloud Database-as-a-Service (DBaaS) providing automated cluster provisioning, multi-AZ replica sets, continuous backups, and automated patching. Unlike local MongoDB on localhost:27017, Atlas provides 99.95% high availability and TLS 1.3 encryption.
</details>

<details>
<summary><strong>2. What is the role of the <code>mongodb+srv://</code> protocol?</strong></summary>
The DNS SRV protocol allows MongoDB drivers to query DNS records dynamically to discover all 3 replica set member hostnames and connection options without hardcoding individual IP addresses.
</details>

<details>
<summary><strong>3. How does Mongoose prevent duplicate student IDs?</strong></summary>
By declaring <code>unique: true</code> on the <code>studentId</code> field, Mongoose commands MongoDB to build a unique B-Tree index. Any insertion of an existing studentId is rejected by MongoDB with error code 11000, which the Express controller catches and returns as HTTP 409 Conflict.
</details>

<details>
<summary><strong>4. Why is IP allowlisting mandatory in MongoDB Atlas?</strong></summary>
Atlas operates with a default-deny firewall. Unless an IP address or CIDR range (such as 0.0.0.0/0 for development) is added to the Network Access list, all inbound TCP connections are dropped at the perimeter firewall.
</details>

<details>
<summary><strong>5. What is the structure of a MongoDB ObjectId (<code>_id</code>)?</strong></summary>
A 12-byte BSON ObjectId consists of: 4 bytes of Unix timestamp (creation time), 5 bytes of unique machine/process identifier, and 3 bytes of incrementing counter, ensuring uniqueness across distributed replica sets.
</details>

---

## Formal Case Study PDF Report

The comprehensive 22-page academic case study report is available in the documentation folder:
- **PDF Report:** [`documentation/Case-Study-Question-3.pdf`](documentation/Case-Study-Question-3.pdf)
- **HTML Source:** [`documentation/Case-Study-Question-3.html`](documentation/Case-Study-Question-3.html)

---

## Student Attribution & Sign-Off

- **Student:** P. Dinesh Kumar
- **Roll Number:** A24126552101
- **Institution:** Anil Neerukonda Institute of Technology & Sciences (ANITS)
- **Evaluation:** Full-Stack Web Development Lab (23CM4121) | Unit V
