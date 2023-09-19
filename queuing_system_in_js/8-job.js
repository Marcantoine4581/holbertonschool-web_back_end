function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw Error('Jobs is not an array');
  }
  jobs.forEach((job) => {
    const notification3 = queue.create('push_notification_code_3', job).save((error) => {
      if (!error) console.log(`Notification job created: ${notification3.id}`);
    });

    notification3.on('complete', () => {
      console.log(`Notification job ${notification3.id} completed`);
    });

    notification3.on('failed', (error) => {
      console.log(`Notification job ${notification3.id} failed: ${error.message}`);
    });

    notification3.on('progress', (progress) => {
      console.log(`Notification job ${notification3.id} ${progress}% complete`);
    });
  });
}

export default createPushNotificationsJobs;
