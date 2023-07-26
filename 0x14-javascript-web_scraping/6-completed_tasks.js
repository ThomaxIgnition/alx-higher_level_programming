#!/usr/bin/env node

const request = require('request');

// Function to fetch the tasks from the API URL
function fetchTasks(apiURL) {
  return new Promise((resolve, reject) => {
    request(apiURL, { json: true }, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(`Failed to fetch data. Status code: ${response.statusCode}`);
      } else {
        resolve(body);
      }
    });
  });
}

// Function to compute the number of completed tasks per user ID
function computeCompletedTasks(tasks) {
  const completedTasksCount = {};

  tasks.forEach((task) => {
    if (task.completed) {
      if (completedTasksCount[task.userId]) {
        completedTasksCount[task.userId]++;
      } else {
        completedTasksCount[task.userId] = 1;
      }
    }
  });

  return completedTasksCount;
}

// Main function
async function main() {
  try {
    const apiURL = process.argv[2];

    if (!apiURL) {
      console.error('Error: API URL not provided.');
      return;
    }

    const tasks = await fetchTasks(apiURL);
    const completedTasksCount = computeCompletedTasks(tasks);

    console.log(completedTasksCount);
  } catch (error) {
    console.error('Error:', error);
  }
}

// Call the main function
main();
