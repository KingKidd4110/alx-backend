#!/usr/bin/yarn dev
import { createQueue } from 'kue';

const queue = createQueue({name: 'push_notification_code'});

const job = queue.create('push_notification_code', {
    phoneNumber: '0790669459',
    message: 'Account registered',
  });

  job

  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed attempt', () => {
    console.log('Notification job failed');
  });
job.save();

job
  .on('enqueue', () => {
    console.log('Notification job created:', job.id);
  })
