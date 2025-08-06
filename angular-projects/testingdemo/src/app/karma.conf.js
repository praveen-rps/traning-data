module.exports = function(config) {
config.set({
// Base path for resolving files and exclude patterns
basePath: '',

// Testing frameworks to use (e.g., Jasmine, Mocha)
frameworks: ['mocha', 'chai'],

// Files or patterns to load in the browser
files: [
'src/**/*.js', // Source files
'test/**/*.spec.js' // Test files
],

// Files or patterns to exclude
exclude: [],

// Preprocessors to apply to files before serving them
preprocessors: {
'src/**/*.js': ['coverage'] // Example: Generate coverage reports
},

// Test result reporters (e.g., progress, coverage)
reporters: ['progress', 'coverage'],

// Web server port
port: 9876,

// Enable/disable colors in the output
colors: true,

// Logging level (LOG_DISABLE, LOG_ERROR, LOG_WARN, LOG_INFO, LOG_DEBUG)
logLevel: config.LOG_INFO,

// Automatically watch files and re-run tests on changes
autoWatch: true,

// Browsers to launch for testing
browsers: ['Chrome'],

// Continuous Integration mode: if true, runs tests and exits
singleRun: false,

// Concurrency level: how many browsers to start simultaneously
concurrency: Infinity
});
};