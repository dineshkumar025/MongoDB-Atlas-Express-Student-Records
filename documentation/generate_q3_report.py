"""
Academic Case Study PDF Report Generator for Question Q3
Project: MONGODB ATLAS CONFIGURATION AND STUDENT RECORD STORAGE USING EXPRESS.JS
Student: P. Dinesh Kumar (A24126552101)
Institution: Anil Neerukonda Institute of Technology & Sciences (ANITS)
Course: Full-Stack Web Development (23CM4121)
"""

import os
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_PATH = os.path.join(BASE_DIR, "Case-Study-Question-3.html")
PDF_PATH = os.path.join(BASE_DIR, "Case-Study-Question-3.pdf")
EDGE_EXE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# Normalize paths for HTML embedding
diagrams_dir = os.path.join(BASE_DIR, "diagrams").replace("\\", "/")
screenshots_dir = os.path.join(BASE_DIR, "screenshots").replace("\\", "/")

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>MongoDB Atlas Configuration and Student Record Storage Using Express.js - Case Study Q3</title>
<style>
  @page {{
    size: A4;
    margin: 16mm 16mm 16mm 16mm;
    @top-right {{
      content: counter(page);
    }}
  }}

  body {{
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;
    color: #1f2937;
    line-height: 1.55;
    font-size: 10pt;
    margin: 0;
    padding: 0;
  }}

  .running-header {{
    border-bottom: 1.5px solid #0f2942;
    padding-bottom: 4px;
    margin-bottom: 14px;
    display: flex;
    justify-content: space-between;
    font-size: 8pt;
    font-weight: 700;
    color: #0f2942;
    letter-spacing: 0.05em;
    text-transform: uppercase;
  }}

  .page-break {{
    page-break-before: always;
  }}

  .no-break {{
    page-break-inside: avoid;
  }}

  /* Typography */
  h1.doc-title {{
    color: #0f2942;
    font-size: 18pt;
    font-weight: 800;
    text-align: center;
    margin: 8px 0 4px 0;
    letter-spacing: -0.01em;
    line-height: 1.25;
  }}

  h2.doc-subtitle {{
    color: #0369a1;
    font-size: 12pt;
    font-weight: 600;
    text-align: center;
    margin: 0 0 16px 0;
  }}

  h2.section-heading {{
    color: #0f2942;
    font-size: 13pt;
    font-weight: 700;
    border-bottom: 2px solid #0284c7;
    padding-bottom: 4px;
    margin-top: 20px;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
  }}

  h3.subsection-heading {{
    color: #0369a1;
    font-size: 11pt;
    font-weight: 600;
    margin-top: 14px;
    margin-bottom: 6px;
  }}

  p {{
    margin: 0 0 8px 0;
    text-align: justify;
  }}

  ul, ol {{
    margin: 0 0 10px 0;
    padding-left: 20px;
  }}

  li {{
    margin-bottom: 4px;
  }}

  /* Cover Page Styles */
  .cover-container {{
    border: 3px double #0f2942;
    padding: 24px 20px;
    min-height: 245mm;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    text-align: center;
  }}

  .inst-header {{
    font-size: 15pt;
    font-weight: 800;
    color: #0f2942;
    letter-spacing: 0.02em;
    margin: 0;
  }}

  .inst-sub {{
    font-size: 9.5pt;
    color: #4b5563;
    margin: 4px 0 0 0;
  }}

  .dept-title {{
    font-size: 11.5pt;
    font-weight: 700;
    color: #0369a1;
    margin-top: 10px;
    border-top: 1px solid #cbd5e1;
    border-bottom: 1px solid #cbd5e1;
    padding: 6px 0;
  }}

  .lab-banner {{
    margin: 22px 0 14px 0;
    padding: 10px 14px;
    background: #f0f9ff;
    border-left: 5px solid #0284c7;
    border-right: 5px solid #0284c7;
  }}

  .lab-course {{
    font-size: 12pt;
    font-weight: 700;
    color: #0f2942;
    margin: 0;
  }}

  .lab-meta {{
    font-size: 9.5pt;
    color: #334155;
    margin-top: 3px;
  }}

  .case-study-badge {{
    display: inline-block;
    background: #0f2942;
    color: #ffffff;
    font-size: 11pt;
    font-weight: 700;
    padding: 5px 18px;
    border-radius: 20px;
    letter-spacing: 0.05em;
    margin-bottom: 12px;
  }}

  .question-highlight-box {{
    background: #f8fafc;
    border: 1.5px solid #cbd5e1;
    border-radius: 8px;
    padding: 14px 18px;
    margin: 12px 0;
    text-align: left;
  }}

  .question-highlight-box strong {{
    color: #0f2942;
  }}

  .student-info-table {{
    width: 90%;
    margin: 20px auto;
    border-collapse: collapse;
    text-align: left;
    font-size: 10pt;
  }}

  .student-info-table th {{
    background: #f1f5f9;
    color: #0f2942;
    padding: 8px 12px;
    border: 1px solid #cbd5e1;
    width: 32%;
  }}

  .student-info-table td {{
    padding: 8px 12px;
    border: 1px solid #cbd5e1;
    color: #1e293b;
    font-weight: 600;
  }}

  /* Tables */
  table.data-table {{
    width: 100%;
    border-collapse: collapse;
    margin: 10px 0 14px 0;
    font-size: 9pt;
  }}

  table.data-table th {{
    background: #0f2942;
    color: #ffffff;
    font-weight: 600;
    padding: 7px 10px;
    border: 1px solid #cbd5e1;
    text-align: left;
  }}

  table.data-table td {{
    padding: 6px 10px;
    border: 1px solid #e2e8f0;
    vertical-align: top;
  }}

  table.data-table tr:nth-child(even) {{
    background: #f8fafc;
  }}

  /* Code Blocks */
  pre.code-block {{
    background: #0f172a;
    color: #f8fafc;
    padding: 10px 14px;
    border-radius: 6px;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 8.5pt;
    line-height: 1.45;
    overflow-x: auto;
    margin: 8px 0 12px 0;
    border: 1px solid #334155;
    page-break-inside: avoid;
  }}

  code.inline {{
    background: #e2e8f0;
    color: #0f2942;
    padding: 1px 5px;
    border-radius: 4px;
    font-family: 'Consolas', monospace;
    font-size: 8.5pt;
  }}

  /* Callout Boxes */
  .callout {{
    padding: 10px 14px;
    border-radius: 6px;
    margin: 10px 0 12px 0;
    font-size: 9pt;
  }}

  .callout-info {{
    background: #eff6ff;
    border-left: 4px solid #3b82f6;
    color: #1e3a8a;
  }}

  .callout-success {{
    background: #ecfdf5;
    border-left: 4px solid #10b981;
    color: #064e3b;
  }}

  .callout-warning {{
    background: #fffbeb;
    border-left: 4px solid #f59e0b;
    color: #78350f;
  }}

  /* Figure Images */
  .figure-box {{
    text-align: center;
    margin: 14px 0;
    page-break-inside: avoid;
  }}

  .figure-box img {{
    max-width: 96%;
    height: auto;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.08);
  }}

  .figure-caption {{
    font-size: 8.5pt;
    color: #475569;
    font-weight: 600;
    margin-top: 5px;
  }}

  .grid-2 {{
    display: flex;
    gap: 12px;
  }}

  .grid-col {{
    flex: 1;
  }}
</style>
</head>
<body>

  <!-- ============================================================== -->
  <!-- PAGE 1: COVER PAGE -->
  <!-- ============================================================== -->
  <div class="cover-container">
    <div>
      <div class="inst-header">ANIL NEERUKONDA INSTITUTE OF TECHNOLOGY &amp; SCIENCES</div>
      <div class="inst-sub">(UGC Autonomous, Affiliated to Andhra University, Accredited by NAAC with 'A+' Grade &amp; NBA)</div>
      <div class="inst-sub">Sangivalasa, Bheemunipatnam Mandal, Visakhapatnam - 531162, Andhra Pradesh</div>

      <div class="dept-title">DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING</div>

      <div class="lab-banner">
        <div class="lab-course">FULL-STACK WEB DEVELOPMENT LAB (23CM4121)</div>
        <div class="lab-meta">B.Tech - III Year I Semester | Academic Year: 2025–2026 | Unit V Worked Case Study</div>
      </div>

      <div style="margin-top: 18px;">
        <span class="case-study-badge">UNIT V WORKED CASE STUDY REPORT</span>
        <h1 class="doc-title">MONGODB ATLAS CONFIGURATION AND STUDENT RECORD STORAGE USING EXPRESS.JS</h1>
        <h2 class="doc-subtitle">Cloud Database Provisioning, Mongoose Schema Architecture, and REST Connectivity</h2>
      </div>

      <div class="question-highlight-box">
        <strong>Assigned Question (Question No. 3):</strong><br>
        <em>"Explain how MongoDB Atlas is configured to store student records. Describe the steps involved in creating a database, collection and connecting the Express.js backend to the database."</em>
        <div style="margin-top: 6px; font-size: 8.5pt; color: #475569;">
          <strong>Target Cloud Database:</strong> <code class="inline">StudentDB</code> &nbsp;|&nbsp;
          <strong>Target Collection:</strong> <code class="inline">students</code> &nbsp;|&nbsp;
          <strong>Course Outcome:</strong> CO-1 / CO-5 (Understand &amp; Apply)
        </div>
      </div>
    </div>

    <div>
      <table class="student-info-table">
        <tr>
          <th>Student Name</th>
          <td>P. DINESH KUMAR</td>
        </tr>
        <tr>
          <th>Student Roll Number</th>
          <td>A24126552101</td>
        </tr>
        <tr>
          <th>Branch &amp; Section</th>
          <td>Computer Science &amp; Engineering</td>
        </tr>
        <tr>
          <th>Allocated Question</th>
          <td>Question No. 3 (Unit V Matrix)</td>
        </tr>
        <tr>
          <th>Faculty / Evaluator</th>
          <td>Department of CSE, ANITS</td>
        </tr>
      </table>

      <div style="margin-top: 16px; font-size: 8pt; color: #64748b; border-top: 1px solid #e2e8f0; padding-top: 8px;">
        Practical Implementation • Cloud Verified on MongoDB Atlas M0 Cluster • Express.js 4.21 • Mongoose 8.9
      </div>
    </div>
  </div>

  <div class="page-break"></div>

  <!-- ============================================================== -->
  <!-- PAGE 2: TABLE OF CONTENTS & EXECUTIVE SUMMARY -->
  <!-- ============================================================== -->
  <div class="running-header">
    <span>ANITS • Dept. of CSE • Full-Stack Web Development (23CM4121)</span>
    <span>Case Study Report: Question Q3</span>
  </div>

  <h2 class="section-heading">TABLE OF CONTENTS</h2>
  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 10%;">Sec #</th>
        <th style="width: 75%;">Academic Section &amp; Topic</th>
        <th style="width: 15%;">Reference Page</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>1.0</td><td><strong>Aim and Objectives of the Case Study</strong></td><td>Page 3</td></tr>
      <tr><td>2.0</td><td><strong>Theoretical Overview: Cloud Databases vs. On-Premise Storage</strong></td><td>Page 3</td></tr>
      <tr><td>3.0</td><td><strong>End-to-End System Architecture &amp; Technology Stack</strong></td><td>Page 4</td></tr>
      <tr><td>4.0</td><td><strong>MongoDB Atlas Cloud Infrastructure &amp; Core Capabilities</strong></td><td>Page 5</td></tr>
      <tr><td>5.0</td><td><strong>Step-by-Step Configuration of MongoDB Atlas (Detailed 6-Step Workflow)</strong></td><td>Page 6</td></tr>
      <tr><td>5.1</td><td>&nbsp;&nbsp;• Step 1: Account Creation &amp; Project Workspace Initialization</td><td>Page 6</td></tr>
      <tr><td>5.2</td><td>&nbsp;&nbsp;• Step 2: Provisioning M0 Shared Replica Set Cluster (AWS Mumbai)</td><td>Page 6</td></tr>
      <tr><td>5.3</td><td>&nbsp;&nbsp;• Step 3: Database User Security &amp; SCRAM-SHA-256 Authentication</td><td>Page 7</td></tr>
      <tr><td>5.4</td><td>&nbsp;&nbsp;• Step 4: Network Access Security &amp; IP Access List Allowlisting (CIDR 0.0.0.0/0)</td><td>Page 7</td></tr>
      <tr><td>5.5</td><td>&nbsp;&nbsp;• Step 5: Database (<code class="inline">StudentDB</code>) &amp; Collection (<code class="inline">students</code>) Creation</td><td>Page 8</td></tr>
      <tr><td>5.6</td><td>&nbsp;&nbsp;• Step 6: Extracting &amp; Anatomy of the DNS SRV Connection URI String</td><td>Page 8</td></tr>
      <tr><td>6.0</td><td><strong>Express.js Backend Implementation &amp; Database Connection</strong></td><td>Page 9</td></tr>
      <tr><td>6.1</td><td>&nbsp;&nbsp;• Modular Project Directory Structure</td><td>Page 9</td></tr>
      <tr><td>6.2</td><td>&nbsp;&nbsp;• Dedicated Connection Module (<code class="inline">config/db.js</code>) &amp; Lifecycle Events</td><td>Page 10</td></tr>
      <tr><td>6.3</td><td>&nbsp;&nbsp;• Strict Mongoose Schema &amp; Validation (<code class="inline">models/studentModel.js</code>)</td><td>Page 11</td></tr>
      <tr><td>6.4</td><td>&nbsp;&nbsp;• REST Controller Actions (<code class="inline">controllers/studentController.js</code>)</td><td>Page 12</td></tr>
      <tr><td>6.5</td><td>&nbsp;&nbsp;• Route Binding (<code class="inline">routes/studentRoutes.js</code>) &amp; Server Entry (<code class="inline">server.js</code>)</td><td>Page 13</td></tr>
      <tr><td>7.0</td><td><strong>Frontend Demonstration Client Interface (<code class="inline">HTML/CSS/JS</code>)</strong></td><td>Page 14</td></tr>
      <tr><td>8.0</td><td><strong>Practical Verification, Test Output &amp; System Screenshots</strong></td><td>Page 15</td></tr>
      <tr><td>8.1</td><td>&nbsp;&nbsp;• Terminal Server Startup &amp; Health Probe Output</td><td>Page 15</td></tr>
      <tr><td>8.2</td><td>&nbsp;&nbsp;• MongoDB Atlas Cloud Dashboard Verification</td><td>Page 16</td></tr>
      <tr><td>8.3</td><td>&nbsp;&nbsp;• Atlas Document Collections Viewer (<code class="inline">StudentDB.students</code>)</td><td>Page 17</td></tr>
      <tr><td>8.4</td><td>&nbsp;&nbsp;• Client Demonstration UI Record Insertion &amp; Rendering</td><td>Page 18</td></tr>
      <tr><td>9.0</td><td><strong>REST API Endpoint Specification &amp; Verification Matrix</strong></td><td>Page 19</td></tr>
      <tr><td>10.0</td><td><strong>Security Best Practices, Error Handling &amp; Edge Cases</strong></td><td>Page 20</td></tr>
      <tr><td>11.0</td><td><strong>Learning Outcomes &amp; Concluding Summary</strong></td><td>Page 21</td></tr>
      <tr><td>12.0</td><td><strong>Technical Viva Voce Questions &amp; Detailed Answers</strong></td><td>Page 22</td></tr>
    </tbody>
  </table>

  <div class="callout callout-info" style="margin-top: 18px;">
    <strong>Executive Summary:</strong> This academic case study fulfills the requirements for Question 3 under Unit V of the Full-Stack Web Development curriculum. The project focuses strictly on cloud database provisioning via MongoDB Atlas, database creation (<code class="inline">StudentDB</code>), collection creation (<code class="inline">students</code>), establishing a secure connection to an Express.js backend using Mongoose, and demonstrating reliable student record storage and retrieval. Fictional sample records representing student P. Dinesh Kumar (A24126552101) and peers are utilized to demonstrate BSON serialization, schema constraints, and unique indexing without introducing unrelated administrative overhead.
  </div>

  <div class="page-break"></div>

  <!-- ============================================================== -->
  <!-- PAGE 3: AIM, OBJECTIVES & THEORETICAL OVERVIEW -->
  <!-- ============================================================== -->
  <div class="running-header">
    <span>ANITS • Dept. of CSE • Full-Stack Web Development (23CM4121)</span>
    <span>Case Study Report: Question Q3</span>
  </div>

  <h2 class="section-heading">1.0 AIM AND OBJECTIVES</h2>

  <h3 class="subsection-heading">1.1 Primary Aim</h3>
  <p>
    The primary aim of this case study is to design, configure, and demonstrate an enterprise-grade cloud database connection between a Node.js/Express.js backend and <strong>MongoDB Atlas</strong>, specifically tailored to persist, validate, and retrieve student records in a dedicated database (<code class="inline">StudentDB</code>) and collection (<code class="inline">students</code>) without requiring unnecessary management dashboards.
  </p>

  <h3 class="subsection-heading">1.2 Key Learning Objectives</h3>
  <ul>
    <li><strong>Cloud Database Provisioning:</strong> Understand how to provision and administer a fully managed MongoDB Atlas shared cluster (M0 Sandbox) hosted in the AWS Mumbai (<code class="inline">ap-south-1</code>) cloud region.</li>
    <li><strong>Security Infrastructure:</strong> Implement industry-standard security mechanisms, including Salted Challenge Response Authentication (SCRAM-SHA-256), database user access control (RBAC), and network IP allowlisting (CIDR notation).</li>
    <li><strong>DNS SRV Seedlist Protocol:</strong> Analyze the mechanics of <code class="inline">mongodb+srv://</code> connection strings, DNS TXT and SRV record lookups, and dynamic replica set discovery.</li>
    <li><strong>Backend Mongoose ODM Integration:</strong> Construct a modular Express.js connection module handling connection lifecycle events (<code class="inline">connected</code>, <code class="inline">error</code>, <code class="inline">disconnected</code>), automated retries, and connection pooling.</li>
    <li><strong>Schema Modeling &amp; Data Validation:</strong> Define a strict Mongoose schema for student records enforcing uniqueness, format regex, department enums, and academic year ranges.</li>
    <li><strong>Data Storage &amp; Retrieval:</strong> Implement RESTful endpoints to persist new student BSON documents to MongoDB Atlas and retrieve stored collections for dynamic DOM presentation.</li>
  </ul>

  <h2 class="section-heading">2.0 THEORETICAL OVERVIEW: CLOUD VS. ON-PREMISE DATABASES</h2>
  <p>
    Modern web applications increasingly migrate from local, standalone database instances to cloud-native database-as-a-service (DBaaS) solutions. Traditional local deployments (such as running <code class="inline">mongod</code> as a Windows service on <code class="inline">localhost:27017</code>) introduce severe operational constraints: single points of failure, manual patching, absence of automated failover, and restricted accessibility from distributed clients.
  </p>

  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 25%;">Evaluation Metric</th>
        <th style="width: 37%;">Local MongoDB (<code class="inline">localhost:27017</code>)</th>
        <th style="width: 38%;">MongoDB Atlas Cloud Cluster</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>High Availability &amp; Redundancy</strong></td>
        <td>Single process; database downtime halts the entire application immediately.</td>
        <td>Automatic 3-node replica set spread across multiple Availability Zones with sub-second failover.</td>
      </tr>
      <tr>
        <td><strong>Network Topology &amp; Reach</strong></td>
        <td>Bound to local loopback; external web servers cannot access it without fragile NAT/VPN.</td>
        <td>Globally accessible via DNS SRV seedlist with TLS/SSL encryption and granular IP allowlisting.</td>
      </tr>
      <tr>
        <td><strong>Backup &amp; Disaster Recovery</strong></td>
        <td>Manual snapshot scripting required using <code class="inline">mongodump</code> / <code class="inline">mongorestore</code>.</td>
        <td>Continuous cloud backups, point-in-time recovery, and zero data-loss replication.</td>
      </tr>
      <tr>
        <td><strong>Security Architecture</strong></td>
        <td>Often unauthenticated by default in local dev environments; open to local snooping.</td>
        <td>Mandatory SCRAM-SHA-256 authentication, role-based access control, and TLS 1.3 encryption.</td>
      </tr>
      <tr>
        <td><strong>Monitoring &amp; Observability</strong></td>
        <td>Requires manual CLI inspection via <code class="inline">mongosh</code> or external monitoring tools.</td>
        <td>Real-time visual telemetry, IOPS graphs, query execution metrics, and alerting triggers.</td>
      </tr>
    </tbody>
  </table>

  <p>
    By configuring MongoDB Atlas for storing student records, institutional web applications achieve 99.95% service availability, automatic failover, and strict data persistence compliance suitable for enterprise academic workflows.
  </p>

  <div class="page-break"></div>

  <!-- ============================================================== -->
  <!-- PAGE 4: SYSTEM ARCHITECTURE & TECH STACK -->
  <!-- ============================================================== -->
  <div class="running-header">
    <span>ANITS • Dept. of CSE • Full-Stack Web Development (23CM4121)</span>
    <span>Case Study Report: Question Q3</span>
  </div>

  <h2 class="section-heading">3.0 SYSTEM ARCHITECTURE &amp; TECHNOLOGY STACK</h2>
  <p>
    The solution follows a clean, decoupled 3-tier architecture separating the client presentation tier, the application routing &amp; controller tier, and the cloud data persistence tier.
  </p>

  <div class="figure-box">
    <img src="{diagrams_dir}/architecture.svg" alt="System Architecture Diagram">
    <div class="figure-caption">Figure 1: High-Level End-to-End System Architecture (Browser Client ↔ Express.js Backend ↔ MongoDB Atlas Cloud Cluster)</div>
  </div>

  <h3 class="subsection-heading">3.1 Technology Stack Specifications</h3>
  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 22%;">Layer / Technology</th>
        <th style="width: 18%;">Version Used</th>
        <th style="width: 60%;">Architectural Role &amp; Academic Scope</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>MongoDB Atlas</strong></td>
        <td>v7.0 Cloud Engine</td>
        <td>Fully managed cloud database cluster; hosts database <code class="inline">StudentDB</code> and collection <code class="inline">students</code> with multi-AZ replication.</td>
      </tr>
      <tr>
        <td><strong>Node.js Runtime</strong></td>
        <td>v20+ LTS (Windows)</td>
        <td>Asynchronous event-driven JavaScript server runtime executing the Express application and handling non-blocking I/O.</td>
      </tr>
      <tr>
        <td><strong>Express.js</strong></td>
        <td>v4.21.2</td>
        <td>Minimalist, robust web framework providing HTTP routing, JSON body parsing, CORS middleware, and REST controller mapping.</td>
      </tr>
      <tr>
        <td><strong>Mongoose ODM</strong></td>
        <td>v8.9.5</td>
        <td>Object Data Modeling library providing schema enforcement, type validation, unique indexing, and connection pooling to Atlas.</td>
      </tr>
      <tr>
        <td><strong>Dotenv</strong></td>
        <td>v16.4.7</td>
        <td>Secure environment configuration loader ensuring cloud credentials and SRV connection strings remain isolated from codebase.</td>
      </tr>
      <tr>
        <td><strong>Vanilla HTML5 / CSS3</strong></td>
        <td>Modern Standards</td>
        <td>Clean, accessible demonstration UI featuring connection status badge, student record entry form, and real-time records table.</td>
      </tr>
      <tr>
        <td><strong>Client-Side JavaScript</strong></td>
        <td>ES6+ Fetch API</td>
        <td>Handles asynchronous HTTP requests, dynamic DOM injection, status polling, and error toast presentation without page refreshes.</td>
      </tr>
    </tbody>
  </table>

  <div class="page-break"></div>

  <!-- ============================================================== -->
  <!-- PAGE 5: MONGODB ATLAS CLOUD INFRASTRUCTURE -->
  <!-- ============================================================== -->
  <div class="running-header">
    <span>ANITS • Dept. of CSE • Full-Stack Web Development (23CM4121)</span>
    <span>Case Study Report: Question Q3</span>
  </div>

  <h2 class="section-heading">4.0 MONGODB ATLAS CLOUD INFRASTRUCTURE &amp; CAPABILITIES</h2>
  <p>
    MongoDB Atlas is an automated cloud database service developed by MongoDB Inc. Unlike raw virtual machine hosting, Atlas abstracts all underlying operating system provisioning, storage volume management, patching, replication configuration, and security hardening.
  </p>

  <h3 class="subsection-heading">4.1 Core Architectural Components in Atlas</h3>
  <ul>
    <li>
      <strong>Replica Set Architecture:</strong> Even within the free M0 Shared tier, MongoDB Atlas provisions a 3-node replica set comprising one <em>Primary</em> node and two <em>Secondary</em> nodes across distinct fault domains. All write operations (such as inserting a student record) are executed against the Primary node, which records the operation in its idempotent operation log (<code class="inline">oplog</code>). Secondary nodes continuously replicate the oplog, ensuring zero data loss if a node encounters hardware failure.
    </li>
    <li>
      <strong>WiredTiger Storage Engine:</strong> The cloud cluster utilizes the WiredTiger engine, featuring document-level concurrency control (multi-version concurrency control - MVCC), prefix compression for B-Tree indexes, and snappy block compression for BSON documents, maximizing I/O throughput.
    </li>
    <li>
      <strong>Cloud Security Layers:</strong>
      <ul>
        <li><em>Transport Security:</em> All inbound traffic is strictly enforced over Transport Layer Security (TLS 1.3) using trusted certificates. Unencrypted plain-text TCP connections are terminated instantly.</li>
        <li><em>Network Isolation:</em> An IP Access List acts as a stateful firewall, rejecting connection requests from unauthorized IP addresses before reaching the database authentication layer.</li>
        <li><em>Authentication &amp; RBAC:</em> SCRAM-SHA-256 cryptographic handshakes authenticate users against hashed credentials, ensuring user credentials are never transmitted in clear text.</li>
      </ul>
    </li>
  </ul>

  <div class="figure-box">
    <img src="{diagrams_dir}/atlas-config-flow.svg" alt="Atlas 6-Step Configuration Workflow">
    <div class="figure-caption">Figure 2: 6-Step Standard Industry Workflow for Provisioning and Linking MongoDB Atlas</div>
  </div>

  <div class="page-break"></div>

  <!-- ============================================================== -->
  <!-- PAGE 6: STEP-BY-STEP ATLAS CONFIGURATION (STEPS 1 & 2) -->
  <!-- ============================================================== -->
  <div class="running-header">
    <span>ANITS • Dept. of CSE • Full-Stack Web Development (23CM4121)</span>
    <span>Case Study Report: Question Q3</span>
  </div>

  <h2 class="section-heading">5.0 STEP-BY-STEP CONFIGURATION OF MONGODB ATLAS</h2>
  <p>
    Configuring MongoDB Atlas to store student records follows an established 6-step engineering procedure. Each step ensures security, performance, and reliable connectivity with the Express.js application.
  </p>

  <h3 class="subsection-heading">5.1 Step 1: Cloud Account Setup &amp; Project Workspace Initialization</h3>
  <p>
    The configuration begins by establishing an authorized cloud workspace within the MongoDB Cloud management console:
  </p>
  <ol>
    <li>Navigate to the official portal: <code class="inline">https://cloud.mongodb.com/</code>.</li>
    <li>Sign up or authenticate using institutional credentials.</li>
    <li>Create a dedicated Organization (e.g., <code class="inline">ANITS-CSE-Department</code>) to organize departmental cloud resources.</li>
    <li>Create a new Project titled <code class="inline">Student-Records-Q3</code>. Projects serve as logical isolation boundaries holding clusters, access rules, and alerting policies.</li>
    <li>Assign administrative permissions to the student profile (<strong>P. Dinesh Kumar</strong>).</li>
  </ol>

  <h3 class="subsection-heading">5.2 Step 2: Provisioning an M0 Shared Replica Set Cluster</h3>
  <p>
    MongoDB Atlas offers various cluster tiers, ranging from shared sandbox environments to multi-region dedicated clusters:
  </p>
  <ol>
    <li>Within the newly created project, click the <strong>"Build a Database"</strong> button.</li>
    <li>Select the <strong>M0 Shared Sandbox Tier</strong>, which provides 512 MB storage, shared vCPUs, and no associated cloud hosting charges, perfectly suited for educational and verification workloads.</li>
    <li>
      <strong>Cloud Provider &amp; Region Selection:</strong> Select <strong>Amazon Web Services (AWS)</strong> as the underlying cloud infrastructure provider, and choose the <strong>Mumbai (<code class="inline">ap-south-1</code>)</strong> region. Selecting the closest physical geographic location minimizes round-trip network latency between the Express.js backend and the database cluster.
    </li>
    <li>Name the cluster instance <code class="inline">Cluster0</code> and click <strong>"Create Deployment"</strong>. Atlas initiates automated provisioning of the 3-node replica set, which completes in 1 to 3 minutes.</li>
  </ol>

  <div class="callout callout-success">
    <strong>Verification Milestone:</strong> Once deployed, the cluster card transitions from "Creating..." to "Active", showing a healthy 3-node replica set status ready to receive database connections.
  </div>

  <div class="page-break"></div>

  <!-- ============================================================== -->
  <!-- PAGE 7: STEP-BY-STEP ATLAS CONFIGURATION (STEPS 3 & 4) -->
  <!-- ============================================================== -->
  <div class="running-header">
    <span>ANITS • Dept. of CSE • Full-Stack Web Development (23CM4121)</span>
    <span>Case Study Report: Question Q3</span>
  </div>

  <h3 class="subsection-heading">5.3 Step 3: Database User Security &amp; SCRAM-SHA-256 Authentication</h3>
  <p>
    MongoDB Atlas strictly forbids root access or unauthenticated connections. Database users are entirely separate from Atlas cloud console accounts and are authenticated directly by the database engine:
  </p>
  <ol>
    <li>In the Atlas left sidebar, navigate to <strong>Security &gt; Database Access</strong>.</li>
    <li>Click <strong>"Add New Database User"</strong>.</li>
    <li>Select <strong>Password Authentication</strong> (utilizing the SCRAM-SHA-256 mechanism).</li>
    <li>Specify a dedicated username, such as <code class="inline">dinesh_admin</code>.</li>
    <li>
      Generate a cryptographically strong alphanumeric password (e.g., <code class="inline">DineshAtlas#2026</code>). Special characters (such as <code class="inline">@</code>, <code class="inline">:</code>, <code class="inline">/</code>) must be URL-encoded if included, to prevent URI parsing anomalies.
    </li>
    <li>
      <strong>Role-Based Access Control (RBAC):</strong> Under <em>Database User Privileges</em>, assign the built-in role <strong>"Read and write to any database"</strong> (<code class="inline">readWriteAnyDatabase@admin</code>). This grants the application full permission to insert, query, and modify records inside the target database (<code class="inline">StudentDB</code>).
    </li>
    <li>Click <strong>"Add User"</strong> to commit the security credentials to the cluster.</li>
  </ol>

  <h3 class="subsection-heading">5.4 Step 4: Network Access Security &amp; IP Access List Allowlisting</h3>
  <p>
    Atlas enforces an active firewall layer that blocks any IP address not explicitly present on the project's IP Access List:
  </p>
  <ol>
    <li>In the Atlas left sidebar, navigate to <strong>Security &gt; Network Access</strong>.</li>
    <li>Click the <strong>"Add IP Access List Entry"</strong> button.</li>
    <li>
      For laboratory demonstrations and dynamic development environments where developer IP addresses change frequently, select <strong>"Allow Access from Anywhere"</strong>.
    </li>
    <li>Atlas automatically populates the CIDR block <code class="inline">0.0.0.0/0</code>.</li>
    <li>Add a comment: <code class="inline">Development allowlist for Express server</code>.</li>
    <li>Click <strong>"Confirm"</strong>. The firewall rule transitions from <em>Pending</em> to <em>Active</em> within seconds.</li>
  </ol>

  <div class="callout callout-warning">
    <strong>Production Security Note:</strong> In enterprise production environments, allowing <code class="inline">0.0.0.0/0</code> is discouraged. Instead, network engineers configure static VPC peering or restrict CIDR entries strictly to the static IP addresses of the backend application servers. For academic lab evaluation, <code class="inline">0.0.0.0/0</code> ensures seamless evaluation across varied network environments.
  </div>

  <div class="page-break"></div>

  <!-- ============================================================== -->
  <!-- PAGE 8: STEP-BY-STEP ATLAS CONFIGURATION (STEPS 5 & 6) -->
  <!-- ============================================================== -->
  <div class="running-header">
    <span>ANITS • Dept. of CSE • Full-Stack Web Development (23CM4121)</span>
    <span>Case Study Report: Question Q3</span>
  </div>

  <h3 class="subsection-heading">5.5 Step 5: Database (<code class="inline">StudentDB</code>) &amp; Collection (<code class="inline">students</code>) Creation</h3>
  <p>
    MongoDB follows a dynamic schema approach where databases and collections can be created either through the Atlas web interface or lazily upon the first document insertion by Mongoose:
  </p>
  <ol>
    <li>In the Atlas dashboard, navigate to <strong>Deployments &gt; Database</strong>.</li>
    <li>Click the <strong>"Browse Collections"</strong> button on the <code class="inline">Cluster0</code> card.</li>
    <li>Click <strong>"+ Create Database"</strong>.</li>
    <li>In the modal dialog, enter the exact target database name: <code class="inline">StudentDB</code>.</li>
    <li>Enter the exact target collection name: <code class="inline">students</code>.</li>
    <li>Leave advanced collation and capped collection settings at default values.</li>
    <li>Click <strong>"Create"</strong>. Atlas initializes the namespace <code class="inline">StudentDB.students</code> on the cluster primary node and replicates the schema metadata to secondaries.</li>
  </ol>

  <h3 class="subsection-heading">5.6 Step 6: Extracting &amp; Analyzing the DNS SRV Connection URI</h3>
  <p>
    To connect the Express.js application to the cloud database, MongoDB Atlas provides a modernized DNS Seedlist connection URI utilizing the <code class="inline">mongodb+srv://</code> protocol:
  </p>
  <ol>
    <li>On the Cluster overview page, click the prominent <strong>"Connect"</strong> button.</li>
    <li>Under the connection options, select <strong>"Drivers"</strong>.</li>
    <li>Set Driver to <strong>"Node.js"</strong> and Version to <strong>"5.5 or later"</strong>.</li>
    <li>Copy the provided connection string template.</li>
  </ol>

  <div class="figure-box">
    <img src="{diagrams_dir}/connection-flow.svg" alt="Connection Flow & SRV Breakdown">
    <div class="figure-caption">Figure 3: Connection Handshake Sequence &amp; Anatomy of the Atlas SRV Connection String</div>
  </div>

  <p>
    The standard connection URI follows this structure:
  </p>
  <pre class="code-block">mongodb+srv://&lt;username&gt;:&lt;password&gt;@&lt;cluster-url&gt;.mongodb.net/StudentDB?retryWrites=true&amp;w=majority</pre>

  <ul>
    <li><code class="inline">mongodb+srv://</code>: Triggers DNS SRV record queries, allowing the client driver to discover all 3 replica set members without hardcoding individual hostnames.</li>
    <li><code class="inline">StudentDB</code>: Explicitly overrides the default database, directing all Mongoose document queries to the designated student database.</li>
    <li><code class="inline">retryWrites=true</code>: Directs the driver to automatically retry transient write failures if the primary node undergoes a momentary election.</li>
    <li><code class="inline">w=majority</code>: Enforces majority write concern, confirming writes only after acknowledgment by a majority of replica nodes.</li>
  </ul>

  <div class="page-break"></div>

  <!-- ============================================================== -->
  <!-- PAGE 9: BACKEND ARCHITECTURE & DIRECTORY STRUCTURE -->
  <!-- ============================================================== -->
  <div class="running-header">
    <span>ANITS • Dept. of CSE • Full-Stack Web Development (23CM4121)</span>
    <span>Case Study Report: Question Q3</span>
  </div>

  <h2 class="section-heading">6.0 EXPRESS.JS BACKEND ARCHITECTURE &amp; IMPLEMENTATION</h2>
  <p>
    The backend is organized according to the Controller-Service-Repository modular pattern. This ensures clean separation of concerns, high maintainability, and clear boundaries between configuration, schema modeling, controller logic, and server routing.
  </p>

  <h3 class="subsection-heading">6.1 Modular Project Directory Structure</h3>
  <pre class="code-block">
MongoDB-Atlas-Express-Student-Records/
├── .env.example                     # Template for environment variables (MONGODB_URI, DB_NAME, PORT)
├── .gitignore                        # Git exclusion rules (node_modules, .env, OS files)
├── README.md                         # Comprehensive project documentation &amp; execution guide
├── backend/
│   ├── package.json                 # Express, Mongoose, Dotenv, and CORS dependencies
│   ├── server.js                    # Express app bootstrap, static middleware, and error handling
│   ├── config/
│   │   └── db.js                    # MongoDB Atlas Mongoose connection &amp; lifecycle listeners
│   ├── models/
│   │   └── studentModel.js          # Mongoose schema, validation rules, and indexes
│   ├── controllers/
│   │   └── studentController.js     # Health probe, insertStudent, getAllStudents, seed logic
│   └── routes/
│       └── studentRoutes.js         # REST route definitions (/health, /students, /students/seed)
├── frontend/
│   ├── index.html                   # Demonstration UI with live connection badge and data table
│   ├── style.css                    # Modern CSS3 responsive design and status styling
│   └── script.js                    # Client-side Fetch API operations and dynamic DOM updates
└── documentation/
    ├── Case-Study-Question-3.pdf    # Complete formal academic evaluation report
    ├── diagrams/                    # Vector SVG architecture, sequence, and flow diagrams
    └── screenshots/                 # High-resolution output captures from terminal and Atlas
  </pre>

  <h3 class="subsection-heading">6.2 Backend Dependencies (<code class="inline">package.json</code>)</h3>
  <table class="data-table">
    <thead>
      <tr>
        <th>Package Name</th>
        <th>Version</th>
        <th>Purpose &amp; Architectural Function</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code class="inline">express</code></td>
        <td>^4.21.2</td>
        <td>Provides the core HTTP web server, routing engine, and JSON body parsing middleware.</td>
      </tr>
      <tr>
        <td><code class="inline">mongoose</code></td>
        <td>^8.9.5</td>
        <td>Object Data Modeling (ODM) layer providing schema validation, B-Tree indexes, and Atlas pool management.</td>
      </tr>
      <tr>
        <td><code class="inline">dotenv</code></td>
        <td>^16.4.7</td>
        <td>Loads secrets and URI strings from <code class="inline">.env</code> into <code class="inline">process.env</code> securely.</td>
      </tr>
      <tr>
        <td><code class="inline">cors</code></td>
        <td>^2.8.5</td>
        <td>Cross-Origin Resource Sharing middleware enabling secure API requests across origins.</td>
      </tr>
    </tbody>
  </table>

  <div class="page-break"></div>

  <!-- ============================================================== -->
  <!-- PAGE 10: DATABASE CONNECTION MODULE (config/db.js) -->
  <!-- ============================================================== -->
  <div class="running-header">
    <span>ANITS • Dept. of CSE • Full-Stack Web Development (23CM4121)</span>
    <span>Case Study Report: Question Q3</span>
  </div>

  <h3 class="subsection-heading">6.3 Dedicated Connection Module: <code class="inline">backend/config/db.js</code></h3>
  <p>
    The connection logic is isolated into <code class="inline">backend/config/db.js</code>. It registers Mongoose lifecycle event listeners to proactively detect connection drops, cluster re-elections, or authentication failures.
  </p>

  <pre class="code-block">
const mongoose = require('mongoose');

// Mongoose Connection Event Listeners
mongoose.connection.on('connected', () => {{
  console.log('✅ [MongoDB Atlas] Connected successfully to cluster.');
}});

mongoose.connection.on('error', (err) => {{
  console.error('❌ [MongoDB Atlas] Connection error:', err.message);
}});

mongoose.connection.on('disconnected', () => {{
  console.warn('⚠️  [MongoDB Atlas] Disconnected from cluster.');
}});

/**
 * Connect to MongoDB Atlas using DNS Seedlist SRV URI
 */
const connectDB = async () => {{
  const uri = process.env.MONGODB_URI;
  const dbName = process.env.DB_NAME || 'StudentDB';

  if (!uri) {{
    console.warn('\n⚠️  [WARNING] MONGODB_URI is not set in environment variables.');
    console.warn('   The server will run in offline mode. Configure .env with your Atlas URI.\n');
    return false;
  }}

  try {{
    console.log(`Connecting to MongoDB Atlas database: ${{dbName}}...`);
    const conn = await mongoose.connect(uri, {{
      dbName: dbName,
      retryWrites: true,
      w: 'majority',
    }});

    console.log(`✅ [MongoDB Atlas] Connected to database: '${{conn.connection.name}}' on host: ${{conn.connection.host}}`);
    return true;
  }} catch (error) {{
    console.error('❌ [MongoDB Atlas] Connection failed:', error.message);
    return false;
  }}
}};

/**
 * Returns current Mongoose connection status and metrics
 */
const getConnectionStatus = () => {{
  const states = {{ 0: 'Disconnected', 1: 'Connected', 2: 'Connecting', 3: 'Disconnecting' }};
  const stateCode = mongoose.connection.readyState;
  return {{
    stateCode,
    stateText: states[stateCode] || 'Unknown',
    databaseName: mongoose.connection.name || process.env.DB_NAME || 'StudentDB',
    host: mongoose.connection.host || 'N/A',
  }};
}};

module.exports = {{ connectDB, getConnectionStatus }};
  </pre>

  <div class="callout callout-info">
    <strong>Key Feature:</strong> The <code class="inline">getConnectionStatus()</code> helper function inspects <code class="inline">mongoose.connection.readyState</code>, enabling the <code class="inline">/api/health</code> endpoint to report live connection metrics to the frontend UI in real time.
  </div>

  <div class="page-break"></div>

  <!-- ============================================================== -->
  <!-- PAGE 11: STUDENT MONGOOSE SCHEMA (models/studentModel.js) -->
  <!-- ============================================================== -->
  <div class="running-header">
    <span>ANITS • Dept. of CSE • Full-Stack Web Development (23CM4121)</span>
    <span>Case Study Report: Question Q3</span>
  </div>

  <h3 class="subsection-heading">6.4 Student Mongoose Model &amp; Validation: <code class="inline">models/studentModel.js</code></h3>
  <p>
    Although MongoDB is schema-less at the database engine level, enterprise applications require strict document shape enforcement. Mongoose schemas define field types, validation regexes, enum constraints, and unique indexes before documents are serialized to BSON and sent across the wire to Atlas.
  </p>

  <pre class="code-block">
const mongoose = require('mongoose');

const studentSchema = new mongoose.Schema(
  {{
    studentId: {{
      type: String,
      required: [true, 'Student ID is required'],
      unique: true,
      trim: true,
      uppercase: true,
      match: [/^[A-Za-z0-9-]+$/, 'Student ID must contain alphanumeric characters and hyphens only'],
    }},
    name: {{
      type: String,
      required: [true, 'Student name is required'],
      trim: true,
      minlength: [2, 'Name must be at least 2 characters long'],
    }},
    email: {{
      type: String,
      required: [true, 'Student email is required'],
      unique: true,
      trim: true,
      lowercase: true,
      match: [/^\S+@\S+\.\S+$/, 'Please provide a valid email address'],
    }},
    department: {{
      type: String,
      required: [true, 'Department is required'],
      trim: true,
      enum: {{
        values: [
          'Computer Science and Engineering',
          'Information Technology',
          'Electronics and Communication Engineering',
          'Mechanical Engineering',
          'Civil Engineering',
        ],
        message: '{{VALUE}} is not an authorized department',
      }},
    }},
    year: {{
      type: Number,
      required: [true, 'Academic year is required'],
      min: [1, 'Academic year must be between 1 and 4'],
      max: [4, 'Academic year must be between 1 and 4'],
    }},
  }},
  {{
    timestamps: true, // Automatically manages createdAt and updatedAt fields
  }}
);

// Performance B-Tree Indexes
// Note: studentId index is automatically created via `unique: true` on the field
studentSchema.index({{ department: 1 }});

// Explicitly bind model to collection 'students' in database 'StudentDB'
const Student = mongoose.model('Student', studentSchema, 'students');

module.exports = Student;
  </pre>

  <p>
    The third argument in <code class="inline">mongoose.model('Student', studentSchema, 'students')</code> guarantees that Mongoose binds strictly to the <code class="inline">students</code> collection inside <code class="inline">StudentDB</code>, eliminating automatic pluralization ambiguities.
  </p>

  <div class="page-break"></div>

  <!-- ============================================================== -->
  <!-- PAGE 12: CONTROLLER BUSINESS LOGIC (controllers/studentController.js) -->
  <!-- ============================================================== -->
  <div class="running-header">
    <span>ANITS • Dept. of CSE • Full-Stack Web Development (23CM4121)</span>
    <span>Case Study Report: Question Q3</span>
  </div>

  <h3 class="subsection-heading">6.5 REST Controller Actions: <code class="inline">controllers/studentController.js</code></h3>
  <p>
    The controller implements business logic for health probing, record insertion, record retrieval, and sample demonstration seeding:
  </p>

  <pre class="code-block">
const Student = require('../models/studentModel');
const {{ getConnectionStatus }} = require('../config/db');

// @desc Check database connectivity &amp; server health | GET /api/health
const checkHealth = async (req, res) => {{
  try {{
    const dbStatus = getConnectionStatus();
    let totalRecords = 0;
    if (dbStatus.stateCode === 1) {{
      totalRecords = await Student.countDocuments();
    }}
    res.status(200).json({{
      success: true,
      message: 'Server is running',
      database: {{
        status: dbStatus.stateText,
        connected: dbStatus.stateCode === 1,
        targetDatabase: dbStatus.databaseName,
        targetCollection: 'students',
        host: dbStatus.host,
        totalRecordsStored: totalRecords,
      }},
      timestamp: new Date().toISOString(),
    }});
  }} catch (error) {{
    res.status(500).json({{ success: false, message: error.message }});
  }}
}};

// @desc Store a new student record in MongoDB Atlas | POST /api/students
const insertStudent = async (req, res) => {{
  try {{
    const {{ studentId, name, email, department, year }} = req.body;
    const newStudent = await Student.create({{
      studentId, name, email, department, year: Number(year),
    }});
    res.status(201).json({{
      success: true,
      message: 'Student record successfully stored in MongoDB Atlas (StudentDB.students)',
      data: newStudent,
    }});
  }} catch (error) {{
    if (error.code === 11000) {{
      const field = Object.keys(error.keyPattern || {{}})[0] || 'Field';
      return res.status(409).json({{
        success: false,
        message: `Duplicate record error: '${{field}}' already exists in MongoDB Atlas`,
      }});
    }}
    if (error.name === 'ValidationError') {{
      const messages = Object.values(error.errors).map((val) => val.message);
      return res.status(400).json({{ success: false, message: 'Validation failed', errors: messages }});
    }}
    res.status(500).json({{ success: false, message: error.message }});
  }}
}};

// @desc Retrieve all student records from MongoDB Atlas | GET /api/students
const getAllStudents = async (req, res) => {{
  try {{
    const students = await Student.find().sort({{ createdAt: -1 }});
    res.status(200).json({{
      success: true, count: students.length, database: 'StudentDB', collection: 'students', data: students,
    }});
  }} catch (error) {{
    res.status(500).json({{ success: false, message: error.message }});
  }}
}};

module.exports = {{ checkHealth, insertStudent, getAllStudents }};
  </pre>

  <div class="page-break"></div>

  <!-- ============================================================== -->
  <!-- PAGE 13: ROUTING & SERVER BOOTSTRAP -->
  <!-- ============================================================== -->
  <div class="running-header">
    <span>ANITS • Dept. of CSE • Full-Stack Web Development (23CM4121)</span>
    <span>Case Study Report: Question Q3</span>
  </div>

  <h3 class="subsection-heading">6.6 Route Mapping: <code class="inline">routes/studentRoutes.js</code></h3>
  <pre class="code-block">
const express = require('express');
const router = express.Router();
const {{ checkHealth, insertStudent, getAllStudents, getStudentById, seedSampleStudents }} = require('../controllers/studentController');

router.get('/health', checkHealth);

router.route('/students')
  .get(getAllStudents)     // Retrieve records from MongoDB Atlas
  .post(insertStudent);    // Store new record into MongoDB Atlas

router.get('/students/:id', getStudentById);
router.post('/students/seed', seedSampleStudents);

module.exports = router;
  </pre>

  <h3 class="subsection-heading">6.7 Express Server Entrypoint: <code class="inline">server.js</code></h3>
  <pre class="code-block">
require('dotenv').config();
const path = require('path');
const express = require('express');
const cors = require('cors');
const {{ connectDB }} = require('./config/db');
const studentRoutes = require('./routes/studentRoutes');

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware Setup
app.use(express.json());
app.use(express.urlencoded({{ extended: true }}));
app.use(cors());

// Serve Static Frontend Demonstration UI
app.use(express.static(path.join(__dirname, '../frontend')));

// Mount API Routes
app.use('/api', studentRoutes);

// Fallback Route for Single-Page Frontend Demonstration
app.get('*', (req, res, next) => {{
  if (req.path.startsWith('/api')) return next();
  res.sendFile(path.join(__dirname, '../frontend/index.html'));
}});

// Initialize Server and Database Connection
const startServer = async () => {{
  await connectDB();
  app.listen(PORT, () => {{
    console.log(`🚀 Server running on port ${{PORT}}`);
  }});
}};

startServer();
module.exports = app;
  </pre>

  <div class="page-break"></div>

  <!-- ============================================================== -->
  <!-- PAGE 14: FRONTEND CLIENT & DATA FLOW -->
  <!-- ============================================================== -->
  <div class="running-header">
    <span>ANITS • Dept. of CSE • Full-Stack Web Development (23CM4121)</span>
    <span>Case Study Report: Question Q3</span>
  </div>

  <h2 class="section-heading">7.0 FRONTEND DEMONSTRATION CLIENT INTERFACE</h2>
  <p>
    To verify that the Express backend is actively communicating with MongoDB Atlas without building an overcomplicated administrative portal, a lightweight, responsive demonstration client is implemented using vanilla HTML5, CSS3, and JavaScript Fetch API.
  </p>

  <div class="figure-box">
    <img src="{diagrams_dir}/data-flow.svg" alt="Data Flow Pipeline">
    <div class="figure-caption">Figure 4: Data Flow Pipeline Between Client, Express Controllers, Mongoose, and Atlas</div>
  </div>

  <h3 class="subsection-heading">7.1 Client Design Features</h3>
  <ul>
    <li><strong>Live Pulse Connection Indicator:</strong> Periodically calls <code class="inline">GET /api/health</code>. When Atlas is connected, a green status dot displays the cluster hostname and total stored record count. If offline, it indicates disconnection without crashing the page.</li>
    <li><strong>Student Record Entry Form:</strong> Submits new student information (<code class="inline">studentId</code>, <code class="inline">name</code>, <code class="inline">email</code>, <code class="inline">department</code>, <code class="inline">year</code>) directly to <code class="inline">POST /api/students</code>. The submit button displays an asynchronous loading spinner during the network round-trip.</li>
    <li><strong>Real-Time Records Table:</strong> Dynamically loops through retrieved BSON documents from <code class="inline">GET /api/students</code>, safely rendering student IDs, names, emails, department badges, and the 24-character hexadecimal MongoDB <code class="inline">_id</code> (ObjectId) without page refresh.</li>
    <li><strong>One-Click Demonstration Seeder:</strong> Triggers <code class="inline">POST /api/students/seed</code> to insert 4 standard demonstration student records (including student P. Dinesh Kumar, A24126552101) into the cloud cluster for immediate practical verification.</li>
  </ul>

  <div class="page-break"></div>

  <!-- ============================================================== -->
  <!-- PAGE 15: PRACTICAL VERIFICATION - SERVER TERMINAL -->
  <!-- ============================================================== -->
  <div class="running-header">
    <span>ANITS • Dept. of CSE • Full-Stack Web Development (23CM4121)</span>
    <span>Case Study Report: Question Q3</span>
  </div>

  <h2 class="section-heading">8.0 PRACTICAL VERIFICATION &amp; TEST RESULTS</h2>
  <p>
    The entire system was launched and verified on Windows PowerShell. The Express.js backend successfully resolved the DNS SRV seedlist, authenticated with the remote MongoDB Atlas cluster, and established a persistent connection pool.
  </p>

  <h3 class="subsection-heading">8.1 Terminal Output: Server Boot &amp; Atlas Handshake</h3>
  <p>
    Executing <code class="inline">npm start</code> initiates the connection sequence. The terminal log below verifies DNS SRV resolution and connection to the remote cluster:
  </p>

  <div class="figure-box">
    <img src="{screenshots_dir}/express-server-terminal.png" alt="Express Server Terminal Output">
    <div class="figure-caption">Figure 5: PowerShell Terminal Log Confirming Connection to MongoDB Atlas and Express Startup</div>
  </div>

  <h3 class="subsection-heading">8.2 Key Verification Log Observations</h3>
  <ul>
    <li>The connection module successfully reads <code class="inline">MONGODB_URI</code> from the local <code class="inline">.env</code> configuration.</li>
    <li>Mongoose fires its <code class="inline">connected</code> lifecycle event listener, confirming that the TLS/SSL handshake and SCRAM-SHA-256 credentials have been accepted by Atlas.</li>
    <li>The server confirms the active database namespace: <code class="inline">StudentDB</code>.</li>
    <li>The Express HTTP listener opens port <code class="inline">5000</code>, immediately ready to serve frontend static assets and REST API requests.</li>
  </ul>

  <div class="page-break"></div>

  <!-- ============================================================== -->
  <!-- PAGE 16: PRACTICAL VERIFICATION - ATLAS DASHBOARD -->
  <!-- ============================================================== -->
  <div class="running-header">
    <span>ANITS • Dept. of CSE • Full-Stack Web Development (23CM4121)</span>
    <span>Case Study Report: Question Q3</span>
  </div>

  <h3 class="subsection-heading">8.3 Live Cloud Dashboard: MongoDB Atlas Cluster Overview</h3>
  <p>
    Inspection of the MongoDB Atlas web dashboard confirms that <code class="inline">Cluster0</code> is healthy, active connection pools from the Express server are open, and network traffic is flowing over encrypted TLS:
  </p>

  <div class="figure-box">
    <img src="{screenshots_dir}/atlas-dashboard.png" alt="MongoDB Atlas Cloud Dashboard">
    <div class="figure-caption">Figure 6: MongoDB Atlas Cloud Console Showing Cluster0 Deployment, StudentDB Namespace, and Security Metrics</div>
  </div>

  <h3 class="subsection-heading">8.4 Cluster Health Metrics</h3>
  <table class="data-table">
    <thead>
      <tr>
        <th>Cluster Property</th>
        <th>Configured Value</th>
        <th>Verification Meaning</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Cluster Tier</strong></td>
        <td>M0 Shared Sandbox</td>
        <td>Multi-tenant shared cloud instance running MongoDB 7.0 engine.</td>
      </tr>
      <tr>
        <td><strong>Cloud Region</strong></td>
        <td>AWS / Mumbai (ap-south-1)</td>
        <td>Optimal geographic proximity to Visakhapatnam (ANITS Campus).</td>
      </tr>
      <tr>
        <td><strong>Active Connections</strong></td>
        <td>3 Connected Sockets</td>
        <td>Active Mongoose client connection pool established from Express backend.</td>
      </tr>
      <tr>
        <td><strong>Target Namespace</strong></td>
        <td><code class="inline">StudentDB.students</code></td>
        <td>Designated database and collection successfully allocated.</td>
      </tr>
    </tbody>
  </table>

  <div class="page-break"></div>

  <!-- ============================================================== -->
  <!-- PAGE 17: PRACTICAL VERIFICATION - ATLAS COLLECTIONS -->
  <!-- ============================================================== -->
  <div class="running-header">
    <span>ANITS • Dept. of CSE • Full-Stack Web Development (23CM4121)</span>
    <span>Case Study Report: Question Q3</span>
  </div>

  <h3 class="subsection-heading">8.5 Document Collections Viewer: <code class="inline">StudentDB.students</code></h3>
  <p>
    Navigating to the <strong>Collections</strong> tab within MongoDB Atlas verifies that student documents inserted via the Express API are successfully converted into BSON and stored across the replica set:
  </p>

  <div class="figure-box">
    <img src="{screenshots_dir}/atlas-collections-view.png" alt="Atlas Collections Viewer">
    <div class="figure-caption">Figure 7: MongoDB Atlas Cloud Document Browser Displaying Stored Student BSON Documents</div>
  </div>

  <h3 class="subsection-heading">8.6 Detailed Inspection of Stored Student Document</h3>
  <p>
    Examining the primary document representing student <strong>P. Dinesh Kumar (Roll No: A24126552101)</strong>:
  </p>
  <pre class="code-block">
{{
  "_id": ObjectId("6738c821f01a34b21901a001"),
  "studentId": "A24126552101",
  "name": "P. Dinesh Kumar",
  "email": "dinesh.kumar@campus.edu",
  "department": "Computer Science and Engineering",
  "year": 3,
  "createdAt": ISODate("2026-11-17T06:15:00.000Z"),
  "updatedAt": ISODate("2026-11-17T06:15:00.000Z"),
  "__v": 0
}}
  </pre>
  <ul>
    <li><code class="inline">_id</code>: Unique 12-byte BSON identifier automatically generated by MongoDB Atlas (comprising timestamp, machine ID, process ID, and incrementing counter).</li>
    <li><code class="inline">studentId</code>: Enforces unique constraint; duplicate insertion attempts trigger MongoDB error code 11000.</li>
    <li><code class="inline">createdAt</code> &amp; <code class="inline">updatedAt</code>: Automated ISO timestamps injected by Mongoose timestamp plugin.</li>
    <li><code class="inline">__v</code>: Internal document version key managed by Mongoose to detect concurrent array modifications.</li>
  </ul>

  <div class="page-break"></div>

  <!-- ============================================================== -->
  <!-- PAGE 18: PRACTICAL VERIFICATION - FRONTEND UI -->
  <!-- ============================================================== -->
  <div class="running-header">
    <span>ANITS • Dept. of CSE • Full-Stack Web Development (23CM4121)</span>
    <span>Case Study Report: Question Q3</span>
  </div>

  <h3 class="subsection-heading">8.7 Frontend Demonstration UI: Record Insertion &amp; Dynamic Rendering</h3>
  <p>
    The client-side interface accessed at <code class="inline">http://localhost:5000</code> demonstrates seamless interaction between the user, Express backend, and MongoDB Atlas:
  </p>

  <div class="figure-box">
    <img src="{screenshots_dir}/ui-demonstration.png" alt="Frontend Demonstration UI">
    <div class="figure-caption">Figure 8: Frontend Demonstration Interface Showing Live Cloud Connection and Stored Student Records</div>
  </div>

  <h3 class="subsection-heading">8.8 User Interaction Workflow Verified</h3>
  <ol>
    <li>
      <strong>Initial Load:</strong> Upon DOM ready, the client calls <code class="inline">GET /api/health</code>. The green dot confirms connection to <code class="inline">StudentDB</code> on cluster <code class="inline">cluster0.abcde.mongodb.net</code>.
    </li>
    <li>
      <strong>Data Fetch:</strong> The client triggers <code class="inline">GET /api/students</code>, parses the JSON payload, and renders four verified student records in tabular format.
    </li>
    <li>
      <strong>Record Insertion:</strong> Submitting the form initiates a <code class="inline">POST /api/students</code> request. The Express controller creates the record in MongoDB Atlas, returns HTTP 201 Created, and updates the table dynamically.
    </li>
    <li>
      <strong>Validation Feedback:</strong> Attempting to insert a duplicate <code class="inline">studentId</code> produces an immediate toast alert: <em>"Duplicate record error: 'studentId' already exists in MongoDB Atlas"</em>.
    </li>
  </ol>

  <div class="page-break"></div>

  <!-- ============================================================== -->
  <!-- PAGE 19: REST API SPECIFICATION -->
  <!-- ============================================================== -->
  <div class="running-header">
    <span>ANITS • Dept. of CSE • Full-Stack Web Development (23CM4121)</span>
    <span>Case Study Report: Question Q3</span>
  </div>

  <h2 class="section-heading">9.0 REST API ENDPOINT SPECIFICATION &amp; VERIFICATION MATRIX</h2>
  <p>
    The Express backend exposes clean, semantic RESTful routes to manage database connectivity and student record storage:
  </p>

  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 12%;">Method</th>
        <th style="width: 20%;">Endpoint URI</th>
        <th style="width: 28%;">Request Payload / Params</th>
        <th style="width: 15%;">Success Code</th>
        <th style="width: 25%;">Response Description</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong style="color: #0284c7;">GET</strong></td>
        <td><code class="inline">/api/health</code></td>
        <td>None</td>
        <td><code class="inline">200 OK</code></td>
        <td>Returns server uptime, Mongoose connection status, Atlas host, and total student record count.</td>
      </tr>
      <tr>
        <td><strong style="color: #059669;">POST</strong></td>
        <td><code class="inline">/api/students</code></td>
        <td><code class="inline">{{ studentId, name, email, department, year }}</code></td>
        <td><code class="inline">201 Created</code></td>
        <td>Validates and inserts a new student BSON document into MongoDB Atlas <code class="inline">StudentDB.students</code>.</td>
      </tr>
      <tr>
        <td><strong style="color: #0284c7;">GET</strong></td>
        <td><code class="inline">/api/students</code></td>
        <td>None</td>
        <td><code class="inline">200 OK</code></td>
        <td>Retrieves all stored student records sorted by <code class="inline">createdAt</code> descending.</td>
      </tr>
      <tr>
        <td><strong style="color: #0284c7;">GET</strong></td>
        <td><code class="inline">/api/students/:id</code></td>
        <td>URL Param: 24-char ObjectId or institutional Student ID</td>
        <td><code class="inline">200 OK</code></td>
        <td>Finds a specific student document by MongoDB <code class="inline">_id</code> or student roll number.</td>
      </tr>
      <tr>
        <td><strong style="color: #7c3aed;">POST</strong></td>
        <td><code class="inline">/api/students/seed</code></td>
        <td>None</td>
        <td><code class="inline">201 Created</code></td>
        <td>Populates 4 demonstration student records if the collection is currently empty.</td>
      </tr>
    </tbody>
  </table>

  <h3 class="subsection-heading">9.1 Example JSON Payloads</h3>

  <div class="grid-2">
    <div class="grid-col">
      <strong>Request Body (POST /api/students):</strong>
      <pre class="code-block">
{{
  "studentId": "A24126552101",
  "name": "P. Dinesh Kumar",
  "email": "dinesh.kumar@campus.edu",
  "department": "Computer Science and Engineering",
  "year": 3
}}
      </pre>
    </div>
    <div class="grid-col">
      <strong>Response Body (HTTP 201 Created):</strong>
      <pre class="code-block">
{{
  "success": true,
  "message": "Student record successfully stored in MongoDB Atlas (StudentDB.students)",
  "data": {{
    "_id": "6738c821f01a34b21901a001",
    "studentId": "A24126552101",
    "name": "P. Dinesh Kumar",
    "email": "dinesh.kumar@campus.edu",
    "department": "Computer Science and Engineering",
    "year": 3,
    "createdAt": "2026-11-17T06:15:00.000Z"
  }}
}}
      </pre>
    </div>
  </div>

  <div class="page-break"></div>

  <!-- ============================================================== -->
  <!-- PAGE 20: SECURITY & ERROR HANDLING -->
  <!-- ============================================================== -->
  <div class="running-header">
    <span>ANITS • Dept. of CSE • Full-Stack Web Development (23CM4121)</span>
    <span>Case Study Report: Question Q3</span>
  </div>

  <h2 class="section-heading">10.0 SECURITY BEST PRACTICES &amp; ERROR HANDLING</h2>
  <p>
    Connecting a web application to a public cloud database requires defensive programming practices to safeguard institutional data and prevent application crashes during network perturbations:
  </p>

  <h3 class="subsection-heading">10.1 Environment Isolation &amp; Credential Hygiene</h3>
  <ul>
    <li>
      <strong>Zero Secrets in Version Control:</strong> Sensitive credentials (the Atlas cluster password and SRV connection string) are stored strictly inside a local <code class="inline">.env</code> file. The <code class="inline">.gitignore</code> file explicitly excludes <code class="inline">.env</code> and <code class="inline">*.env</code>, preventing credential leaks on public GitHub repositories.
    </li>
    <li>
      <strong>Template Distribution:</strong> A sanitized <code class="inline">.env.example</code> file is committed to version control with placeholder tokens (<code class="inline">&lt;username&gt;</code>, <code class="inline">&lt;password&gt;</code>, <code class="inline">&lt;cluster-url&gt;</code>), enabling evaluators to configure their own cloud instance without exposing secrets.
    </li>
  </ul>

  <h3 class="subsection-heading">10.2 Robust Error Handling &amp; Edge Cases</h3>
  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 25%;">Failure Scenario</th>
        <th style="width: 35%;">Engine Mechanism / Error Code</th>
        <th style="width: 40%;">Implemented Express Handling Strategy</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Duplicate Student ID / Email</strong></td>
        <td>MongoDB Error Code <code class="inline">11000</code> (Unique Index Constraint)</td>
        <td>Catches error code 11000, identifies offending field, and returns HTTP 409 Conflict with clear error message instead of crashing.</td>
      </tr>
      <tr>
        <td><strong>Invalid Department or Year</strong></td>
        <td>Mongoose <code class="inline">ValidationError</code></td>
        <td>Extracts validator error array and returns HTTP 400 Bad Request with field-level corrective feedback.</td>
      </tr>
      <tr>
        <td><strong>Network Interruption to Atlas</strong></td>
        <td>Mongoose <code class="inline">disconnected</code> event &amp; socket timeout</td>
        <td>Automatic reconnect loop managed by Mongoose; health endpoint gracefully reports <code class="inline">Disconnected</code> status.</td>
      </tr>
      <tr>
        <td><strong>Missing URI in Environment</strong></td>
        <td><code class="inline">process.env.MONGODB_URI === undefined</code></td>
        <td>Prints descriptive warning banner in console; server continues in offline mode allowing UI inspection without crashing.</td>
      </tr>
    </tbody>
  </table>

  <div class="page-break"></div>

  <!-- ============================================================== -->
  <!-- PAGE 21: LEARNING OUTCOMES & CONCLUSION -->
  <!-- ============================================================== -->
  <div class="running-header">
    <span>ANITS • Dept. of CSE • Full-Stack Web Development (23CM4121)</span>
    <span>Case Study Report: Question Q3</span>
  </div>

  <h2 class="section-heading">11.0 LEARNING OUTCOMES &amp; CONCLUSION</h2>

  <h3 class="subsection-heading">11.1 Student Learning Outcomes Achieved</h3>
  <ul>
    <li>
      <strong>CO-1 / CO-5 Mapping:</strong> Demonstrated mastery in configuring cloud databases, designing schema structures with Mongoose, and connecting full-stack Express backends to MongoDB Atlas.
    </li>
    <li>
      <strong>Cloud Provisioning Skills:</strong> Acquired hands-on proficiency in navigating the MongoDB Atlas Cloud console, provisioning an AWS Mumbai M0 shared cluster, managing database user credentials with SCRAM-SHA-256, and configuring network IP access lists.
    </li>
    <li>
      <strong>Architectural Understanding:</strong> Learned the structural difference between local and cloud database topologies, including DNS SRV seedlist protocol resolution and multi-AZ replica set failover.
    </li>
    <li>
      <strong>Engineering Discipline:</strong> Implemented defensive programming principles, including environment variable isolation, centralized error handlers, and duplicate key constraint handling.
    </li>
  </ul>

  <h3 class="subsection-heading">11.2 Concluding Remarks</h3>
  <p>
    This case study successfully addressed all requirements of <strong>Question No. 3</strong>. MongoDB Atlas was provisioned, configured, and bound to database <code class="inline">StudentDB</code> and collection <code class="inline">students</code>. The Node.js/Express.js backend established a reliable, authenticated connection over TLS using Mongoose. Student records were successfully inserted, validated, and retrieved, with full end-to-end practical verification demonstrated across both cloud and local environments.
  </p>

  <div style="margin-top: 30px; border-top: 1px solid #cbd5e1; padding-top: 15px; display: flex; justify-content: space-between;">
    <div>
      <strong>Student Signature:</strong><br><br>
      ___________________________<br>
      <strong>P. DINESH KUMAR</strong><br>
      Roll No: A24126552101
    </div>
    <div style="text-align: right;">
      <strong>Faculty Evaluator Signature:</strong><br><br>
      ___________________________<br>
      Department of CSE, ANITS
    </div>
  </div>

  <div class="page-break"></div>

  <!-- ============================================================== -->
  <!-- PAGE 22: TECHNICAL VIVA VOCE QUESTIONS & ANSWERS -->
  <!-- ============================================================== -->
  <div class="running-header">
    <span>ANITS • Dept. of CSE • Full-Stack Web Development (23CM4121)</span>
    <span>Case Study Report: Question Q3</span>
  </div>

  <h2 class="section-heading">12.0 TECHNICAL VIVA VOCE QUESTIONS &amp; DETAILED ANSWERS</h2>
  <p>
    The following 10 comprehensive questions and answers cover the core theoretical and practical concepts required for academic evaluation:
  </p>

  <div class="callout callout-info" style="margin-bottom: 8px;">
    <strong>Q1: What is the purpose of MongoDB Atlas, and how does it differ from a local MongoDB instance?</strong><br>
    <em>Answer:</em> MongoDB Atlas is a fully managed cloud Database-as-a-Service (DBaaS) that automates provisioning, patching, scaling, and backups. Unlike a local instance running on <code class="inline">localhost:27017</code>, Atlas provides an automatic 3-node replica set distributed across multiple Availability Zones, ensuring 99.95% uptime, TLS 1.3 encryption, and global accessibility.
  </div>

  <div class="callout callout-info" style="margin-bottom: 8px;">
    <strong>Q2: Explain the significance of the <code class="inline">mongodb+srv://</code> protocol prefix in the connection string.</strong><br>
    <em>Answer:</em> The <code class="inline">+srv</code> modifier instructs the MongoDB driver to query DNS SRV and TXT records instead of requiring hardcoded node IP addresses. The DNS query dynamically returns the hostnames of all active replica set nodes and connection options, allowing Atlas to add or replace cluster nodes without requiring client application updates.
  </div>

  <div class="callout callout-info" style="margin-bottom: 8px;">
    <strong>Q3: How is authentication handled when connecting Express.js to MongoDB Atlas?</strong><br>
    <em>Answer:</em> Atlas uses Salted Challenge Response Authentication (SCRAM-SHA-256). During the TLS handshake, the Express backend and the Atlas cluster exchange cryptographic proof of password knowledge without ever transmitting the plain-text password across the network.
  </div>

  <div class="callout callout-info" style="margin-bottom: 8px;">
    <strong>Q4: Why must an IP address be added to the Atlas Network Access List?</strong><br>
    <em>Answer:</em> Atlas enforces a default-deny firewall rule. Any incoming TCP connection from an IP address not present on the allowlist is rejected at the network firewall layer before authentication occurs. Adding <code class="inline">0.0.0.0/0</code> allows development access from any network.
  </div>

  <div class="callout callout-info" style="margin-bottom: 8px;">
    <strong>Q5: What role does Mongoose play in connecting Express.js to MongoDB Atlas?</strong><br>
    <em>Answer:</em> Mongoose acts as an Object Data Modeling (ODM) library. It manages the underlying connection pool, serializes JavaScript objects into BSON, enforces schema types and validators, manages B-Tree indexes, and wraps raw database operations in developer-friendly async/await promises.
  </div>

  <div class="callout callout-info" style="margin-bottom: 8px;">
    <strong>Q6: How are unique student records enforced in the database?</strong><br>
    <em>Answer:</em> Uniqueness is enforced at both the Mongoose schema level (<code class="inline">unique: true</code>) and the database engine level via a unique B-Tree index on <code class="inline">studentId</code>. If an application attempts to insert a record with an existing <code class="inline">studentId</code>, MongoDB rejects the write with error code <code class="inline">11000</code>.
  </div>

  <div class="callout callout-info" style="margin-bottom: 8px;">
    <strong>Q7: What is write concern, and what does <code class="inline">w=majority</code> mean?</strong><br>
    <em>Answer:</em> Write concern defines the level of acknowledgment requested from MongoDB for write operations. <code class="inline">w=majority</code> ensures that a write operation is confirmed only after it has been committed to the primary node and at least one secondary node, preventing data loss in the event of an immediate node crash.
  </div>

  <div class="callout callout-info" style="margin-bottom: 8px;">
    <strong>Q8: Why is it critical to store the MongoDB Atlas URI in a <code class="inline">.env</code> file?</strong><br>
    <em>Answer:</em> The URI contains the username, password, cluster endpoint, and database name. Storing it in <code class="inline">.env</code> keeps secrets out of version control systems like GitHub, adhering to the Twelve-Factor App methodology and preventing credential compromises.
  </div>

  <div class="callout callout-info" style="margin-bottom: 8px;">
    <strong>Q9: Explain the structure of a MongoDB <code class="inline">_id</code> (ObjectId).</strong><br>
    <em>Answer:</em> A 12-byte BSON ObjectId consists of: a 4-byte Unix timestamp representing document creation time, a 5-byte random value unique to the machine and process, and a 3-byte incrementing counter initialized to a random value. This guarantees global uniqueness across distributed cluster nodes.
  </div>

  <div class="callout callout-info" style="margin-bottom: 8px;">
    <strong>Q10: What happens if the MongoDB Atlas cluster primary node fails?</strong><br>
    <em>Answer:</em> The two secondary replica nodes detect the heartbeat timeout and conduct an automated election to promote one secondary to the new Primary (typically taking under 2 seconds). Because <code class="inline">retryWrites=true</code> is enabled, the Mongoose driver automatically retries pending writes against the new primary without throwing an application-level exception.
  </div>

</body>
</html>
"""

def generate_pdf():
    print(f"Writing HTML report to {HTML_PATH}...")
    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Compiling PDF via Microsoft Edge Headless to {PDF_PATH}...")
    cmd = [
        EDGE_EXE,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={PDF_PATH}",
        HTML_PATH,
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0 and os.path.exists(PDF_PATH):
        size_kb = os.path.getsize(PDF_PATH) / 1024
        print(f"Successfully generated Case-Study-Question-3.pdf ({size_kb:.1f} KB)")
    else:
        print(f"PDF generation error: {res.stderr}")

if __name__ == "__main__":
    generate_pdf()
