/**
 * Main Application Server Entrypoint
 * 
 * Project: MONGODB ATLAS CONFIGURATION AND STUDENT RECORD STORAGE USING EXPRESS.JS
 * Case Study Question Q3 | Unit V: MongoDB and Deploying Applications
 * Course: Full-Stack Web Development (23CM4121)
 * Institution: Anil Neerukonda Institute of Technology & Sciences (ANITS)
 * Student: P. Dinesh Kumar (Roll No: A24126552101)
 */

require('dotenv').config();
const path = require('path');
const express = require('express');
const cors = require('cors');
const { connectDB } = require('./config/db');
const studentRoutes = require('./routes/studentRoutes');

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware Setup
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cors());

// Serve Static Frontend Demonstration UI
app.use(express.static(path.join(__dirname, '../frontend')));

// Mount API Routes
app.use('/api', studentRoutes);

// Fallback Route for Single-Page Frontend Demonstration
app.get('*', (req, res, next) => {
  if (req.path.startsWith('/api')) {
    return next();
  }
  res.sendFile(path.join(__dirname, '../frontend/index.html'));
});

// 404 Route Handler for undefined API routes
app.use((req, res) => {
  res.status(404).json({
    success: false,
    message: `API Route '${req.originalUrl}' not found`,
  });
});

// Centralized Error Handling Middleware
app.use((err, req, res, next) => {
  console.error('Server Unhandled Error:', err.stack);
  res.status(500).json({
    success: false,
    message: 'Internal server error encountered',
    error: process.env.NODE_ENV === 'production' ? null : err.message,
  });
});

/**
 * Initialize Server and Database Connection
 */
const startServer = async () => {
  // Connect to MongoDB Atlas (Database: StudentDB)
  await connectDB();

  // Start Express HTTP listener
  app.listen(PORT, () => {
    console.log(`\n================================================================`);
    console.log(` 🚀 SERVER RUNNING AT: http://localhost:${PORT}`);
    console.log(` 📊 DEMONSTRATION UI: http://localhost:${PORT}/`);
    console.log(` 🩺 HEALTH ENDPOINT : http://localhost:${PORT}/api/health`);
    console.log(` 📚 STUDENTS API    : http://localhost:${PORT}/api/students`);
    console.log(`================================================================\n`);
  });
};

startServer();

module.exports = app;
