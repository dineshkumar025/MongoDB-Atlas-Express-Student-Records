/**
 * Frontend Client Script: Handles dynamic UI interactions and REST API calls
 * 
 * Case Study Question Q3: MongoDB Atlas Configuration & Student Record Storage
 * Student: P. Dinesh Kumar (A24126552101)
 */

document.addEventListener('DOMContentLoaded', () => {
  // DOM Elements
  const statusDot = document.getElementById('statusDot');
  const statusText = document.getElementById('statusText');
  const statusHost = document.getElementById('statusHost');
  const recordCountBadge = document.getElementById('recordCountBadge');
  const btnCheckHealth = document.getElementById('btnCheckHealth');
  const alertBox = document.getElementById('alertBox');
  const alertMessage = document.getElementById('alertMessage');
  const alertClose = document.getElementById('alertClose');

  const studentForm = document.getElementById('studentForm');
  const btnSubmit = document.getElementById('btnSubmit');
  const btnSeed = document.getElementById('btnSeed');
  const btnRefresh = document.getElementById('btnRefresh');

  const loadingState = document.getElementById('loadingState');
  const tableContainer = document.getElementById('tableContainer');
  const emptyState = document.getElementById('emptyState');
  const studentTableBody = document.getElementById('studentTableBody');

  // Display alert notification toast
  function showAlert(message, type = 'success') {
    alertBox.className = `alert-box alert-${type}`;
    alertMessage.textContent = message;
    alertBox.style.display = 'flex';

    // Auto-hide after 5 seconds
    setTimeout(() => {
      alertBox.style.display = 'none';
    }, 5000);
  }

  alertClose.addEventListener('click', () => {
    alertBox.style.display = 'none';
  });

  // Check Database & Server Health
  async function checkDatabaseHealth() {
    statusDot.className = 'status-dot';
    statusText.textContent = 'Checking MongoDB Atlas connection...';
    statusHost.textContent = 'Connecting...';

    try {
      const response = await fetch('/api/health');
      const data = await response.json();

      if (data.database && data.database.connected) {
        statusDot.className = 'status-dot connected';
        statusText.textContent = `Connected to ${data.database.targetDatabase}`;
        statusHost.textContent = data.database.host || 'MongoDB Atlas Cloud Cluster';
        recordCountBadge.textContent = data.database.totalRecordsStored || 0;
      } else {
        statusDot.className = 'status-dot disconnected';
        statusText.textContent = data.database ? data.database.status : 'Disconnected';
        statusHost.textContent = 'Atlas URI not connected';
      }
    } catch (err) {
      statusDot.className = 'status-dot disconnected';
      statusText.textContent = 'Server Offline';
      statusHost.textContent = 'Backend unreachable';
    }
  }

  // Load and Render Stored Student Records
  async function loadStudentRecords() {
    loadingState.style.display = 'flex';
    tableContainer.style.display = 'none';
    emptyState.style.display = 'none';

    try {
      const response = await fetch('/api/students');
      const result = await response.json();

      loadingState.style.display = 'none';

      if (result.success && Array.isArray(result.data) && result.data.length > 0) {
        studentTableBody.innerHTML = '';
        recordCountBadge.textContent = result.data.length;

        result.data.forEach((student) => {
          const row = document.createElement('tr');
          row.innerHTML = `
            <td><strong>${escapeHtml(student.studentId)}</strong></td>
            <td>${escapeHtml(student.name)}</td>
            <td><a href="mailto:${escapeHtml(student.email)}">${escapeHtml(student.email)}</a></td>
            <td><span class="dept-tag">${escapeHtml(student.department)}</span></td>
            <td><span class="year-badge">Year ${escapeHtml(student.year.toString())}</span></td>
            <td><code class="object-id">${escapeHtml(student._id || 'N/A')}</code></td>
          `;
          studentTableBody.appendChild(row);
        });

        tableContainer.style.display = 'block';
      } else {
        recordCountBadge.textContent = '0';
        emptyState.style.display = 'block';
      }
    } catch (err) {
      loadingState.style.display = 'none';
      showAlert('Failed to fetch records from server: ' + err.message, 'error');
      emptyState.style.display = 'block';
    }
  }

  // Handle Form Submission (Insert Student Record)
  studentForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const studentId = document.getElementById('studentId').value.trim();
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const department = document.getElementById('department').value;
    const year = document.getElementById('year').value;

    if (!studentId || !name || !email || !department || !year) {
      showAlert('Please fill in all required fields.', 'warning');
      return;
    }

    btnSubmit.disabled = true;
    btnSubmit.textContent = 'Storing in Atlas...';

    try {
      const response = await fetch('/api/students', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ studentId, name, email, department, year }),
      });

      const data = await response.json();

      if (response.ok && data.success) {
        showAlert(`Student '${data.data.name}' stored successfully in MongoDB Atlas!`, 'success');
        studentForm.reset();
        await loadStudentRecords();
        await checkDatabaseHealth();
      } else {
        const errorMsg = data.message || (data.errors ? data.errors.join(', ') : 'Failed to store record');
        showAlert(errorMsg, 'error');
      }
    } catch (err) {
      showAlert('Network error while connecting to Express backend: ' + err.message, 'error');
    } finally {
      btnSubmit.disabled = false;
      btnSubmit.textContent = '💾 Save to MongoDB Atlas';
    }
  });

  // Handle Seed Records Button
  btnSeed.addEventListener('click', async () => {
    btnSeed.disabled = true;
    btnSeed.textContent = 'Seeding...';

    try {
      const response = await fetch('/api/students/seed', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
      });
      const data = await response.json();

      if (response.ok && data.success) {
        showAlert(data.message, 'success');
        await loadStudentRecords();
        await checkDatabaseHealth();
      } else {
        showAlert(data.message || 'Seeding unsuccessful', 'warning');
      }
    } catch (err) {
      showAlert('Error during seeding: ' + err.message, 'error');
    } finally {
      btnSeed.disabled = false;
      btnSeed.textContent = '🌱 Seed Sample Records';
    }
  });

  // Health Check & Refresh Event Listeners
  btnCheckHealth.addEventListener('click', () => {
    checkDatabaseHealth();
    showAlert('Checking MongoDB Atlas connection status...', 'info');
  });

  btnRefresh.addEventListener('click', () => {
    loadStudentRecords();
    checkDatabaseHealth();
  });

  // Helper function to escape HTML
  function escapeHtml(str) {
    if (!str) return '';
    return str
      .toString()
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  // Initial Load on Page Mount
  checkDatabaseHealth();
  loadStudentRecords();
});
