/**
 * Database Connection Module: MongoDB Atlas Connectivity via Mongoose
 * 
 * Case Study Question Q3: Explaining and configuring MongoDB Atlas connection
 * Target Database: StudentDB
 * Student: P. Dinesh Kumar (A24126552101)
 */

const mongoose = require('mongoose');

// Mongoose Connection Event Listeners
mongoose.connection.on('connected', () => {
  console.log(' [MongoDB Atlas] Connected successfully to cluster.');
});

mongoose.connection.on('error', (err) => {
  console.error(' [MongoDB Atlas] Connection error:', err.message);
});

mongoose.connection.on('disconnected', () => {
  console.warn(' [MongoDB Atlas] Disconnected from cluster.');
});

/**
 * Connect to MongoDB Atlas using DNS Seedlist SRV URI
 */
const connectDB = async () => {
  const uri = process.env.MONGODB_URI;
  const dbName = process.env.DB_NAME || 'StudentDB';

  if (!uri) {
    console.warn('\n⚠️  [WARNING] MONGODB_URI is not set in environment variables.');
    console.warn('   The server will run in offline mode. Configure .env with your Atlas URI to enable persistence.\n');
    return false;
  }

  try {
    console.log(`Connecting to MongoDB Atlas database: ${dbName}...`);
    const conn = await mongoose.connect(uri, {
      dbName: dbName,
      retryWrites: true,
      w: 'majority',
    });

    console.log(`✅ [MongoDB Atlas] Connected to database: '${conn.connection.name}' on host: ${conn.connection.host}`);
    return true;
  } catch (error) {
    console.error('❌ [MongoDB Atlas] Connection failed:', error.message);
    // In production, do not immediately exit so health check can report status
    return false;
  }
};

/**
 * Returns current Mongoose connection status and metrics
 */
const getConnectionStatus = () => {
  const states = {
    0: 'Disconnected',
    1: 'Connected',
    2: 'Connecting',
    3: 'Disconnecting',
  };
  const stateCode = mongoose.connection.readyState;
  return {
    stateCode,
    stateText: states[stateCode] || 'Unknown',
    databaseName: mongoose.connection.name || process.env.DB_NAME || 'StudentDB',
    host: mongoose.connection.host || 'N/A',
  };
};

module.exports = { connectDB, getConnectionStatus };
