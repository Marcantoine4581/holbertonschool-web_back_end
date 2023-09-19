import kue from 'kue';

const queue = kue.createQueue();

const jobData = queue.create('push_notification_code', {
  phoneNumber: '+33612358544',
  message: 'Hello World',
}).save((error) => {
  if (!error) console.log(`Notification job created: ${jobData.id}`);
});

jobData.on('complete', () => {
  console.log('Notification job completed');
});

jobData.on('failed', () => {
  console.log('Notification job failed');
});
