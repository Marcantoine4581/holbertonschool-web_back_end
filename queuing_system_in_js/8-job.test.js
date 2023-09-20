import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job';

const queue = kue.createQueue();

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account',
  },
];

describe('createPushNotificationsJobs', () => {
  before(function () {
    queue.testMode.enter();
  });

  afterEach(function () {
    queue.testMode.clear();
  });

  after(function () {
    queue.testMode.exit();
  });

  it('display an error message if jobs is not an array', () => {
    expect(() => {
      createPushNotificationsJobs('Hello', queue);
    }).to.throw('Jobs is not an array');
    expect(() => {
      createPushNotificationsJobs(1, queue);
    }).to.throw('Jobs is not an array');
    expect(() => {
      createPushNotificationsJobs({name: 'John'}, queue);
    }).to.throw('Jobs is not an array');
    expect(() => {
      createPushNotificationsJobs(queue);
    }).to.throw('Jobs is not an array');
    expect(() => {
      createPushNotificationsJobs();
    }).to.throw('Jobs is not an array');
  });

  it('create two new jobs to the queue', () => {
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
    console.log(queue.testMode.jobs[0].id);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data.phoneNumber).to.equal('4153518780');
    expect(Number(queue.testMode.jobs[1].id))
      .to.be.above(Number(queue.testMode.jobs[0].id));
  });
});
