/**
 * Student Mongoose Model and Schema Definition
 * 
 * Target Database: StudentDB
 * Target Collection: students
 * Student: P. Dinesh Kumar (A24126552101)
 */

const mongoose = require('mongoose');

const studentSchema = new mongoose.Schema(
  {
    studentId: {
      type: String,
      required: [true, 'Student ID is required'],
      unique: true,
      trim: true,
      uppercase: true,
      match: [/^[A-Za-z0-9-]+$/, 'Student ID must contain alphanumeric characters and hyphens only'],
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
      match: [/^\S+@\S+\.\S+$/, 'Please provide a valid email address'],
    },
    department: {
      type: String,
      required: [true, 'Department is required'],
      trim: true,
      enum: {
        values: [
          'Computer Science and Engineering',
          'Information Technology',
          'Electronics and Communication Engineering',
          'Mechanical Engineering',
          'Civil Engineering',
        ],
        message: '{VALUE} is not an authorized department',
      },
    },
    year: {
      type: Number,
      required: [true, 'Academic year is required'],
      min: [1, 'Academic year must be between 1 and 4'],
      max: [4, 'Academic year must be between 1 and 4'],
    },
  },
  {
    timestamps: true, // Automatically manages createdAt and updatedAt timestamps
  }
);

// Performance B-Tree Indexes
// Note: unique index on studentId is automatically created via `unique: true`
studentSchema.index({ department: 1 });

// Explicitly bind model to collection 'students'
const Student = mongoose.model('Student', studentSchema, 'students');

module.exports = Student;

