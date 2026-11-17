/**
 * Student Controller: Handles business logic for storing and retrieving records
 * 
 * Case Study Question Q3: Student Record Storage in MongoDB Atlas
 * Student: P. Dinesh Kumar (A24126552101)
 */

const Student = require('../models/studentModel');
const { getConnectionStatus } = require('../config/db');

/**
 * @desc    Check database connectivity & server health
 * @route   GET /api/health
 */
const checkHealth = async (req, res) => {
  try {
    const dbStatus = getConnectionStatus();
    let totalRecords = 0;
    if (dbStatus.stateCode === 1) {
      totalRecords = await Student.countDocuments();
    }

    res.status(200).json({
      success: true,
      message: 'Server is running',
      database: {
        status: dbStatus.stateText,
        connected: dbStatus.stateCode === 1,
        targetDatabase: dbStatus.databaseName,
        targetCollection: 'students',
        host: dbStatus.host,
        totalRecordsStored: totalRecords,
      },
      timestamp: new Date().toISOString(),
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'Health check encountered an internal error',
      error: error.message,
    });
  }
};

/**
 * @desc    Store a new student record in MongoDB Atlas
 * @route   POST /api/students
 */
const insertStudent = async (req, res) => {
  try {
    const { studentId, name, email, department, year } = req.body;

    // Create and persist document to MongoDB Atlas
    const newStudent = await Student.create({
      studentId,
      name,
      email,
      department,
      year: Number(year),
    });

    res.status(201).json({
      success: true,
      message: 'Student record successfully stored in MongoDB Atlas (StudentDB.students)',
      data: newStudent,
    });
  } catch (error) {
    // Handle MongoDB unique index constraint violations (code 11000)
    if (error.code === 11000) {
      const field = Object.keys(error.keyPattern || {})[0] || 'Field';
      return res.status(409).json({
        success: false,
        message: `Duplicate record error: '${field}' already exists in MongoDB Atlas`,
      });
    }

    // Handle Mongoose schema validation errors
    if (error.name === 'ValidationError') {
      const messages = Object.values(error.errors).map((val) => val.message);
      return res.status(400).json({
        success: false,
        message: 'Validation failed',
        errors: messages,
      });
    }

    res.status(500).json({
      success: false,
      message: 'Failed to store student record in MongoDB Atlas',
      error: error.message,
    });
  }
};

/**
 * @desc    Retrieve all student records from MongoDB Atlas
 * @route   GET /api/students
 */
const getAllStudents = async (req, res) => {
  try {
    const students = await Student.find().sort({ createdAt: -1 });

    res.status(200).json({
      success: true,
      count: students.length,
      database: 'StudentDB',
      collection: 'students',
      data: students,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'Unable to retrieve records from MongoDB Atlas',
      error: error.message,
    });
  }
};

/**
 * @desc    Retrieve a single student record by MongoDB ObjectId or studentId
 * @route   GET /api/students/:id
 */
const getStudentById = async (req, res) => {
  try {
    const { id } = req.params;
    let student = null;

    if (id.match(/^[0-9a-fA-F]{24}$/)) {
      student = await Student.findById(id);
    } else {
      student = await Student.findOne({ studentId: id.toUpperCase() });
    }

    if (!student) {
      return res.status(404).json({
        success: false,
        message: 'Student record not found in MongoDB Atlas',
      });
    }

    res.status(200).json({
      success: true,
      data: student,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'Error searching for student record',
      error: error.message,
    });
  }
};

/**
 * @desc    Seed initial demonstration student records if collection is empty
 * @route   POST /api/students/seed
 */
const seedSampleStudents = async (req, res) => {
  try {
    const count = await Student.countDocuments();
    if (count > 0) {
      return res.status(200).json({
        success: true,
        message: `Collection already contains ${count} records. Seeding skipped.`,
      });
    }

    const sampleRecords = [
      {
        studentId: 'A24126552101',
        name: 'P. Dinesh Kumar',
        email: 'dinesh.kumar@campus.edu',
        department: 'Computer Science and Engineering',
        year: 3,
      },
      {
        studentId: 'A24126552072',
        name: 'Priya Sharma',
        email: 'priya.sharma@campus.edu',
        department: 'Electronics and Communication Engineering',
        year: 2,
      },
      {
        studentId: 'A24126552085',
        name: 'Rahul Verma',
        email: 'rahul.verma@campus.edu',
        department: 'Mechanical Engineering',
        year: 4,
      },
      {
        studentId: 'A24126552093',
        name: 'Ananya Iyer',
        email: 'ananya.iyer@campus.edu',
        department: 'Computer Science and Engineering',
        year: 1,
      },
    ];

    const inserted = await Student.insertMany(sampleRecords);

    res.status(201).json({
      success: true,
      message: 'Successfully seeded 4 demonstration student records into MongoDB Atlas',
      count: inserted.length,
      data: inserted,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'Failed to seed sample records',
      error: error.message,
    });
  }
};

module.exports = {
  checkHealth,
  insertStudent,
  getAllStudents,
  getStudentById,
  seedSampleStudents,
};
