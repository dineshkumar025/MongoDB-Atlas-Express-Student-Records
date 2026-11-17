/**
 * Express Student Routes: Map HTTP verbs and URIs to Controller Actions
 * 
 * Case Study Question Q3: Student Record Storage in MongoDB Atlas
 * Student: P. Dinesh Kumar (A24126552101)
 */

const express = require('express');
const router = express.Router();
const {
  checkHealth,
  insertStudent,
  getAllStudents,
  getStudentById,
  seedSampleStudents,
} = require('../controllers/studentController');

// Health Check Route
router.get('/health', checkHealth);

// Core Student Record Storage & Retrieval Routes
router.route('/students')
  .get(getAllStudents)     // Retrieve records from MongoDB Atlas
  .post(insertStudent);    // Store new record into MongoDB Atlas

// Single Student Record Route
router.get('/students/:id', getStudentById);

// Demonstration Seeding Route
router.post('/students/seed', seedSampleStudents);

module.exports = router;
