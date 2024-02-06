import redis from 'redis';
import util from 'util';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error('Redis client not connected to the server: ', error);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  try {
    const value = await client.get(schoolName);
    console.log(value);
  } catch (err) {
    console.error(err);
  }


const displaySchoolValuePromise = util.promisify(displaySchoolValue);



displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFranscisco', '100');
displaySchoolValue('HolbertonSanFranscisco');
